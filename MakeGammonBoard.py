'''
MakeGammonBoard
  --Making any situation figure of backgammon game.--

MIT License

Copyright (c) 2021 Masanori Hirata(ch-suginami)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

from PIL import Image, ImageDraw, ImageFont

import sys
import string
import datetime

top_p = [chr(ord("a")+i) for i in range(16)]
bottom_p = [chr(ord("A")+i) for i in range(16)]
num_image = "number/"
POINTS = 25
WIDTH = 1420
HEIGHT = 1200
L_MARGIN = 10
T_MARGIN = 100
BLACK = (0, 0, 0)
CH_GRAY = (179, 179, 179)
WHITE = (255, 255, 255)
BOARD_GREY = (77, 77, 77)
RADIUS = 80
PNT_WIDTH = 100
LR_MARGIN = 20
MARGIN = (PNT_WIDTH - RADIUS) // 2
GNU_POS = 10
GNU_MATCH = 9

# font information
font_coords = ImageFont.truetype('SourceHanSans-Normal.otf', 68)
font_num = ImageFont.truetype('SourceHanSans-Normal.otf', 40)

def encode_base64(num):
    BASE64_LIST = []
    for i in string.ascii_uppercase:
        BASE64_LIST.append(i)
    for i in string.ascii_lowercase:
        BASE64_LIST.append(i)
    for i in range(0, 10):
        BASE64_LIST.append(str(i))
    BASE64_LIST.append("+")
    BASE64_LIST.append("/")
    return BASE64_LIST[num]


def decode_base64(let):
    BASE64_LIST = []
    for i in string.ascii_uppercase:
        BASE64_LIST.append(i)
    for i in string.ascii_lowercase:
        BASE64_LIST.append(i)
    for i in range(0, 10):
        BASE64_LIST.append(str(i))
    BASE64_LIST.append("+")
    BASE64_LIST.append("/")
    return (str(bin(BASE64_LIST.index(let)))[2:]).zfill(6)


def draw_base(drawing):
    # each positions
    for i in range(6):
        if i % 2 == 0:
            drawing.polygon((L_MARGIN + i*PNT_WIDTH, T_MARGIN, L_MARGIN + (i+1)*PNT_WIDTH - PNT_WIDTH//2, HEIGHT //2-PNT_WIDTH//2, L_MARGIN + (i+1)*PNT_WIDTH, T_MARGIN), fill=WHITE, outline=BLACK)
            drawing.polygon((L_MARGIN + i*PNT_WIDTH + (WIDTH-LR_MARGIN)//2, T_MARGIN, L_MARGIN + (i+1)*PNT_WIDTH + WIDTH//2 - PNT_WIDTH//2, HEIGHT//2-PNT_WIDTH//2, L_MARGIN + (i+1)*PNT_WIDTH + WIDTH//2, T_MARGIN), fill=WHITE, outline=BLACK)
            drawing.polygon((L_MARGIN + (i+1)*PNT_WIDTH, HEIGHT - T_MARGIN, L_MARGIN + (i+2)*PNT_WIDTH - 50, HEIGHT //2+PNT_WIDTH//2, L_MARGIN + (i+2)*PNT_WIDTH, HEIGHT - T_MARGIN), fill=WHITE, outline=BLACK)
            drawing.polygon((L_MARGIN + (i+1)*PNT_WIDTH + (WIDTH-LR_MARGIN)//2, HEIGHT - T_MARGIN, L_MARGIN + (i+2)*PNT_WIDTH + WIDTH//2 - PNT_WIDTH //2, HEIGHT//2+PNT_WIDTH//2, L_MARGIN + (i+2)*PNT_WIDTH + 700, HEIGHT - T_MARGIN), fill=WHITE, outline=BLACK)
        else:
            drawing.polygon((L_MARGIN + i*PNT_WIDTH, T_MARGIN, L_MARGIN + (i+1)*PNT_WIDTH - PNT_WIDTH//2, HEIGHT // 2-PNT_WIDTH//2, L_MARGIN + (i+1)*PNT_WIDTH, T_MARGIN), fill=BOARD_GREY, outline=BLACK)
            drawing.polygon((L_MARGIN + i*PNT_WIDTH + (WIDTH-LR_MARGIN)//2, T_MARGIN, L_MARGIN + (i+1)*PNT_WIDTH + WIDTH//2 - PNT_WIDTH//2, HEIGHT//2-PNT_WIDTH//2, L_MARGIN + (i+1)*PNT_WIDTH + WIDTH//2, T_MARGIN), fill=BOARD_GREY, outline=BLACK)
            drawing.polygon((L_MARGIN + (i-1)*PNT_WIDTH, HEIGHT - T_MARGIN, L_MARGIN + i*PNT_WIDTH - PNT_WIDTH//2, HEIGHT // 2+PNT_WIDTH//2, L_MARGIN + i*PNT_WIDTH, HEIGHT - T_MARGIN), fill=BOARD_GREY, outline=BLACK)
            drawing.polygon((L_MARGIN + (i-1)*PNT_WIDTH + (WIDTH-LR_MARGIN)//2, HEIGHT - T_MARGIN, L_MARGIN + i*PNT_WIDTH + WIDTH//2 - PNT_WIDTH//2, HEIGHT//2+PNT_WIDTH//2, L_MARGIN + i*PNT_WIDTH + WIDTH//2, HEIGHT - T_MARGIN), fill=BOARD_GREY, outline=BLACK)

    # base rectangle
    drawing.rectangle((L_MARGIN, T_MARGIN, WIDTH - L_MARGIN, HEIGHT - T_MARGIN), outline=BLACK, width=5)

    # Goal line inside up to down
    drawing.line((WIDTH - PNT_WIDTH, T_MARGIN, WIDTH - PNT_WIDTH, HEIGHT - T_MARGIN), fill=BLACK, width=5)

    # center lines
    drawing.line((L_MARGIN + (WIDTH-LR_MARGIN)//2 - PNT_WIDTH, T_MARGIN, L_MARGIN + WIDTH//2 - PNT_WIDTH, HEIGHT - T_MARGIN), fill=BLACK, width=5)
    drawing.line((L_MARGIN + (WIDTH-LR_MARGIN)//2, T_MARGIN, L_MARGIN + WIDTH//2, HEIGHT - T_MARGIN), fill=BLACK, width=5)

    # for cube area
    drawing.line((WIDTH - PNT_WIDTH, T_MARGIN + PNT_WIDTH, WIDTH - L_MARGIN, T_MARGIN + PNT_WIDTH), fill=BLACK, width=5)
    drawing.line((WIDTH - PNT_WIDTH - L_MARGIN, HEIGHT - PNT_WIDTH - T_MARGIN, WIDTH - L_MARGIN, HEIGHT - PNT_WIDTH - T_MARGIN), fill=BLACK, width=5)
    drawing.line((L_MARGIN + WIDTH - PNT_WIDTH, T_MARGIN + HEIGHT//2, L_MARGIN + WIDTH, T_MARGIN + HEIGHT//2), fill=BLACK, width=5)

    # for center cube
    drawing.line((L_MARGIN + (WIDTH-LR_MARGIN)//2-PNT_WIDTH, HEIGHT//2-PNT_WIDTH//2, L_MARGIN + (WIDTH-LR_MARGIN)//2, HEIGHT//2-PNT_WIDTH//2), fill=BLACK, width=5)
    drawing.line((L_MARGIN + (WIDTH-LR_MARGIN)//2-PNT_WIDTH, HEIGHT//2+PNT_WIDTH//2,L_MARGIN + (WIDTH-LR_MARGIN)//2, HEIGHT//2+PNT_WIDTH//2), fill=BLACK, width=5)

    return drawing


def print_circle(pos, num, own, im, drawing):
    if pos == 0:
        drawing.ellipse(((WIDTH-LR_MARGIN)//2-PNT_WIDTH+MARGIN, HEIGHT*3//4-PNT_WIDTH//2+MARGIN, (WIDTH-LR_MARGIN) // 2-MARGIN, HEIGHT*3//4+PNT_WIDTH//2-MARGIN), fill=CH_GRAY, outline=BLACK, width=3)
        num_im = Image.open(num_image + str(num) + ".png")
        im.paste(num_im, ((WIDTH-LR_MARGIN)//2-PNT_WIDTH+MARGIN, HEIGHT * 3//4-PNT_WIDTH//2+MARGIN), mask=num_im)
    if 0 < pos and pos < 7:
        for i in range(num):
            if i > 4:
#                drawing = drawing.text((WIDTH + L_MARGIN -PNT_WIDTH*(pos+1) + MARGIN, HEIGHT-RADIUS*5), str(num), font = font_num, fill = BLACK)
                num_im = Image.open(num_image + str(num) + ".png")
                im.paste(num_im, (WIDTH-PNT_WIDTH*(pos+1) + MARGIN, HEIGHT-RADIUS*5), mask=num_im)
                break
            if own == "b":
                drawing.ellipse((WIDTH-PNT_WIDTH*(pos+1)+MARGIN, HEIGHT-RADIUS*(i+1), WIDTH -
                                PNT_WIDTH*pos-MARGIN, HEIGHT-RADIUS*i), fill=WHITE, outline=BLACK, width=3)
            elif own == "t":
                drawing.ellipse((WIDTH-PNT_WIDTH*(pos+1)+MARGIN, HEIGHT-RADIUS*(i+1), WIDTH -
                                PNT_WIDTH*pos-MARGIN, HEIGHT-RADIUS*i), fill=CH_GRAY, outline=BLACK, width=3)
            else:
                print("Something wrong!")
                dummy = input()
                sys.exit()
    elif 7 <= pos and pos < 13:
        for i in range(num):
            if i > 4:
                num_im = Image.open(num_image + str(num) + ".png")
                im.paste(num_im, (WIDTH//2-(pos-5)*PNT_WIDTH +
                                MARGIN, HEIGHT-RADIUS*5), mask=num_im)
                break
            if own == "b":
                drawing.ellipse((WIDTH//2-(pos-5)*PNT_WIDTH+MARGIN, HEIGHT-RADIUS*(i+1), WIDTH//2-(
                    pos-6)*PNT_WIDTH-MARGIN, HEIGHT-RADIUS*i), fill=WHITE, outline=BLACK, width=3)
            elif own == "t":
                drawing.ellipse((WIDTH//2-(pos-5)*PNT_WIDTH+MARGIN, HEIGHT-RADIUS*(i+1), WIDTH//2-(
                    pos-6)*PNT_WIDTH-MARGIN, HEIGHT-RADIUS*i), fill=CH_GRAY, outline=BLACK, width=3)
            else:
                print("Something wrong!")
                dummy = input()
                sys.exit()
    elif 13 <= pos and pos < 19:
        for i in range(num):
            if i > 4:
                num_im = Image.open(num_image + str(num) + ".png")
                im.paste(num_im, ((pos-13)*PNT_WIDTH +
                                MARGIN, RADIUS*4), mask=num_im)
                break
            if own == "b":
                drawing.ellipse(((pos-13)*PNT_WIDTH+MARGIN, RADIUS*i, (pos-12) *
                                PNT_WIDTH-MARGIN, RADIUS*(i+1)), fill=WHITE, outline=BLACK, width=3)
            elif own == "t":
                drawing.ellipse(((pos-13)*PNT_WIDTH+MARGIN, RADIUS*i, (pos-12) *
                                PNT_WIDTH-MARGIN, RADIUS*(i+1)), fill=CH_GRAY, outline=BLACK, width=3)
            else:
                print("Something wrong!")
                dummy = input()
                sys.exit()
    elif 19 <= pos and pos < 25:
        for i in range(num):
            if i > 4:
                num_im = Image.open(num_image + str(num) + ".png")
                im.paste(num_im, (WIDTH//2+(pos-19)*PNT_WIDTH +
                                MARGIN, RADIUS*4), mask=num_im)
                break
            if own == "b":
                drawing.ellipse((WIDTH//2+(pos-19)*PNT_WIDTH+MARGIN, RADIUS*i, WIDTH//2+(
                    pos-18)*PNT_WIDTH-MARGIN, RADIUS*(i+1)), fill=WHITE, outline=BLACK, width=3)
            elif own == "t":
                drawing.ellipse((WIDTH//2+(pos-19)*PNT_WIDTH+MARGIN, RADIUS*i, WIDTH//2+(
                    pos-18)*PNT_WIDTH-MARGIN, RADIUS*(i+1)), fill=CH_GRAY, outline=BLACK, width=3)
            else:
                print("Something wrong!")
                dummy = input()
                sys.exit()
    elif pos == 25:
        drawing.ellipse((WIDTH//2-PNT_WIDTH+MARGIN, HEIGHT//4-PNT_WIDTH//2+MARGIN, WIDTH //
                        2-MARGIN, HEIGHT//4+PNT_WIDTH//2-MARGIN), fill=WHITE, outline=BLACK, width=3)
        num_im = Image.open(num_image + str(num) + ".png")
        im.paste(num_im, (WIDTH//2-PNT_WIDTH+MARGIN, HEIGHT //
                        4-PNT_WIDTH//2+MARGIN), mask=num_im)
    return drawing


def draw_pos(XGID, im, drawing):
    top_num = 15
    bottom_num = 15
    for i in range(26):
        if XGID[0][i] == "-":
            pass
        else:
            if XGID[0][i] in top_p:
                ch_num = top_p.index(XGID[0][i]) + 1
                top_num -= ch_num
                drawing = print_circle(i, ch_num, "t", im, drawing)
            elif XGID[0][i] in bottom_p:
                ch_num = bottom_p.index(XGID[0][i]) + 1
                bottom_num -= ch_num
                drawing = print_circle(i, ch_num, "b", im, drawing)
            else:
                print("Error at XGID positions.")
                dummy = input()
                sys.exit()
    if top_num < 0:
        print("Too small checkers for the top-player!")
        dummy = input()
        sys.exit()
    elif bottom_num < 0:
        print("Too small checkers for the bottom-player!")
        dummy = input()
        sys.exit()
    else:
        if top_num > 0:
            drawing.ellipse((WIDTH-PNT_WIDTH+MARGIN, HEIGHT//4, WIDTH-MARGIN,
                            HEIGHT//4+RADIUS), fill=CH_GRAY, outline=BLACK, width=3)
            num_im = Image.open(num_image + str(top_num) + ".png")
            im.paste(num_im, (WIDTH-PNT_WIDTH+MARGIN, HEIGHT//4), mask=num_im)
        if bottom_num > 0:
            drawing.ellipse((WIDTH-PNT_WIDTH+MARGIN, HEIGHT//2+PNT_WIDTH+RADIUS, WIDTH -
                            MARGIN, HEIGHT//2+PNT_WIDTH+2*RADIUS), fill=WHITE, outline=BLACK, width=3)
            num_im = Image.open(num_image + str(bottom_num) + ".png")
            im.paste(num_im, (WIDTH-PNT_WIDTH+MARGIN, HEIGHT //
                            2+PNT_WIDTH+RADIUS), mask=num_im)
    return drawing


def draw_cube(XGID, im, drawing):
    if int(XGID[3]) == 1:
        cube_num = 2**(int(XGID[1]))
        # show double
        if XGID[4] == "DD":
            cube_num = 2**(int(XGID[1])+1)
            d_dice = Image.open(num_image + str(cube_num) + ".png")
            d_dice = d_dice.rotate(180)
            drawing.rectangle((int(2.5*PNT_WIDTH)+MARGIN, HEIGHT//2-PNT_WIDTH//2+MARGIN, int(2.5*PNT_WIDTH) +
                            RADIUS+MARGIN, HEIGHT//2-PNT_WIDTH//2+RADIUS+MARGIN), fill=WHITE, outline=BLACK, width=5)
            im.paste(d_dice, (int(2.5*PNT_WIDTH)+MARGIN, HEIGHT //
                            2-PNT_WIDTH//2+MARGIN), mask=d_dice)
            return drawing
        if int(XGID[2]) == 1:
            num_im = Image.open(num_image + str(cube_num) + ".png")
            im.paste(num_im, (WIDTH-PNT_WIDTH+MARGIN,
                            HEIGHT-PNT_WIDTH+MARGIN), mask=num_im)
            return drawing
        elif int(XGID[2]) == -1:
            num_im = Image.open(num_image + str(cube_num) + ".png")
            num_im = num_im.rotate(180)
            im.paste(num_im, (WIDTH-PNT_WIDTH+MARGIN, MARGIN), mask=num_im)
            return drawing
        elif int(XGID[2]) == 0:
            num_im = Image.open(num_image + "64.png")
            num_im = num_im.rotate(90)
            im.paste(num_im, (WIDTH//2-PNT_WIDTH+MARGIN, HEIGHT //
                            2-PNT_WIDTH//2+MARGIN), mask=num_im)
            return drawing
    elif int(XGID[3]) == -1:
        cube_num = 2**(int(XGID[1]))
        if XGID[4] == "DD":
            cube_num = 2**(int(XGID[1])+1)
            d_dice = Image.open(num_image + str(cube_num) + ".png")
            drawing.rectangle((WIDTH//2+int(2.5*PNT_WIDTH)+MARGIN, HEIGHT//2-PNT_WIDTH//2+MARGIN, WIDTH//2+int(
                2.5*PNT_WIDTH)+RADIUS+MARGIN, HEIGHT//2-PNT_WIDTH//2+RADIUS+MARGIN), fill=WHITE, outline=BLACK, width=5)
            im.paste(d_dice, (WIDTH//2+int(2.5*PNT_WIDTH)+MARGIN,
                            HEIGHT//2-PNT_WIDTH//2+MARGIN), mask=d_dice)
            return drawing
        if int(XGID[2]) == 1:
            num_im = Image.open(num_image + str(cube_num) + ".png")
            im.paste(num_im, (WIDTH-PNT_WIDTH+MARGIN,
                            HEIGHT-PNT_WIDTH+MARGIN), mask=num_im)
            return drawing
        elif int(XGID[2]) == -1:
            num_im = Image.open(num_image + str(cube_num) + ".png")
            num_im = num_im.rotate(180)
            im.paste(num_im, (WIDTH-PNT_WIDTH+MARGIN, MARGIN), mask=num_im)
            return drawing
        elif int(XGID[2]) == 0:
            num_im = Image.open(num_image + "64.png")
            num_im = num_im.rotate(90)
            im.paste(num_im, (WIDTH//2-PNT_WIDTH+MARGIN, HEIGHT //
                            2-PNT_WIDTH//2+MARGIN), mask=num_im)
            return drawing
    else:
        print("Doubling cube Error")
        dummy = input()
        sys.exit()


def draw_dice(XGID, im, drawing):
    if int(XGID[3]) == 1:
        # no cide
        if XGID[4] == "00":
            return drawing
        # doubling -> pass
        elif XGID[4] == "DD":
            return drawing
        dice1 = XGID[4][0]
        dice2 = XGID[4][1]
        if not (0 < int(dice1) and int(dice1) < 7):
            print("Error: Cube1 number.")
            dummy = input()
            sys.exit()
        if not (0 < int(dice2) and int(dice2) < 7):
            print("Error: Cube2 number.")
            dummy = input()
            sys.exit()
        dice1_im = Image.open(num_image + "dice_" + dice1 + ".png")
        dice2_im = Image.open(num_image + "dice_" + dice2 + ".png")
        drawing.rectangle((WIDTH//2+2*PNT_WIDTH+MARGIN, HEIGHT//2-PNT_WIDTH//2+MARGIN, WIDTH//2 +
                        2*PNT_WIDTH+RADIUS+MARGIN, HEIGHT//2-PNT_WIDTH//2+RADIUS+MARGIN), outline=BLACK, width=5)
        drawing.rectangle((WIDTH//2+3*PNT_WIDTH+MARGIN, HEIGHT//2-PNT_WIDTH//2+MARGIN, WIDTH//2 +
                        3*PNT_WIDTH+RADIUS+MARGIN, HEIGHT//2-PNT_WIDTH//2+RADIUS+MARGIN), outline=BLACK, width=5)
        im.paste(dice1_im, (WIDTH//2+2*PNT_WIDTH+MARGIN,
                            HEIGHT//2-PNT_WIDTH//2+MARGIN), mask=dice1_im)
        im.paste(dice2_im, (WIDTH//2+3*PNT_WIDTH+MARGIN,
                            HEIGHT//2-PNT_WIDTH//2+MARGIN), mask=dice2_im)
        return drawing
    elif int(XGID[3]) == -1:
        if XGID[4] == "00":
            return drawing
        # doubling -> pass
        elif XGID[4] == "DD":
            return drawing
        dice1 = XGID[4][0]
        dice2 = XGID[4][1]
        if not (0 < int(dice1) and int(dice1) < 7):
            print("Error: Cube1 number.")
            dummy = input()
            sys.exit()
        if not (0 < int(dice2) and int(dice2) < 7):
            print("Error: Cube2 number.")
            dummy = input()
            sys.exit()
        dice1_im = Image.open(num_image + "dice_" + dice1 + ".png")
        dice2_im = Image.open(num_image + "dice_" + dice2 + ".png")
        drawing.rectangle((2*PNT_WIDTH+MARGIN, HEIGHT//2-PNT_WIDTH//2+MARGIN, 2*PNT_WIDTH+RADIUS +
                        MARGIN, HEIGHT//2-PNT_WIDTH//2+RADIUS+MARGIN), fill=CH_GRAY, outline=BLACK, width=5)
        drawing.rectangle((3*PNT_WIDTH+MARGIN, HEIGHT//2-PNT_WIDTH//2+MARGIN, 3*PNT_WIDTH+RADIUS +
                        MARGIN, HEIGHT//2-PNT_WIDTH//2+RADIUS+MARGIN), fill=CH_GRAY, outline=BLACK, width=5)
        im.paste(dice1_im, (2*PNT_WIDTH+MARGIN, HEIGHT //
                            2-PNT_WIDTH//2+MARGIN), mask=dice1_im)
        im.paste(dice2_im, (3*PNT_WIDTH+MARGIN, HEIGHT //
                            2-PNT_WIDTH//2+MARGIN), mask=dice2_im)
        return drawing
    else:
        print("Error: Tern incorrect.")
        dummy = input()
        sys.exit()


def gnubg2posID(gnu):
    #  new_bgID = [_ for _ in range(GNU_POS)]
    encoded_ID = [_ for _ in range(14)]
#  hex_ID = ""
    binary_str = ""
    bgID = [gnu[0:8], gnu[8:16], gnu[16:24], gnu[24:32], gnu[32:40],
            gnu[40:48], gnu[48:56], gnu[56:64], gnu[64:72], gnu[72:80]]
    for i in range(GNU_POS):
        bgID[i] = "".join(list(reversed(bgID[i])))
#    new_bgID[i] = hex(int(str(bgID[i]), 2))
#  for i in range(GNU_POS):
#    if len(new_bgID[i]) == 4:
#      hex_ID += new_bgID[i][2:4]
#    else:
#      hex_ID += "0" + new_bgID[i][2]
    for i in range(GNU_POS):
        bin_num = "".join(bgID)
    encoded_ID = [int(bin_num[0:6], 2), int(bin_num[6:12], 2), int(bin_num[12:18], 2), int(bin_num[18:24], 2), int(bin_num[24:30], 2), int(bin_num[30:36], 2), int(bin_num[36:42], 2), int(
        bin_num[42:48], 2), int(bin_num[48:54], 2), int(bin_num[54:60], 2), int(bin_num[60:66], 2), int(bin_num[66:72], 2), int(bin_num[72:78], 2), int(bin_num[78:] + "0000", 2)]
    for i in range(14):
        binary_str += encode_base64(encoded_ID[i])
    return binary_str


def gnubg2matchID(gnu):
    encoded_ID = [_ for _ in range(14)]
    binary_str = ""
    bgID = [gnu[0:8], gnu[8:16], gnu[16:24], gnu[24:32], gnu[32:40],
            gnu[40:48], gnu[48:56], gnu[56:64], (gnu[64:67] + "000000")]
    for i in range(GNU_MATCH):
        bgID[i] = "".join(list(reversed(bgID[i])))
    bin_num = "".join(bgID)
    encoded_ID = [int(bin_num[0:6], 2), int(bin_num[6:12], 2), int(bin_num[12:18], 2), int(bin_num[18:24], 2), int(bin_num[24:30], 2), int(bin_num[30:36], 2), int(
        bin_num[36:42], 2), int(bin_num[42:48], 2), int(bin_num[48:54], 2), int(bin_num[54:60], 2), int(bin_num[60:66], 2), int(bin_num[66:73], 2)]
    for i in range(12):
        binary_str += encode_base64(encoded_ID[i])
    return binary_str


def posID2XGID(gnu):
    binary_str = ""
    turn = False
    pos_checker = ["" for _ in range(POINTS+1)]
    oppo_checker = [0 for _ in range(POINTS)]
    your_checker = [0 for _ in range(POINTS)]
    for i in range(len(gnu)):
        binary_str += decode_base64(gnu[i])
    bgID = [binary_str[0:8], binary_str[8:16], binary_str[16:24], binary_str[24:32], binary_str[32:40],
            binary_str[40:48], binary_str[48:56], binary_str[56:64], binary_str[64:72], binary_str[72:80]]
    for i in range(GNU_POS):
        bgID[i] = "".join(list(reversed(bgID[i])))
    bin_num = "".join(bgID)
    pos = 0
    cnt = 0
    while True:
        if pos == POINTS:
            pos = 0
            turn = True
        if int(bin_num[cnt]) == 0:
            pos += 1
            cnt += 1
        else:
            while int(bin_num[cnt]):
                if not turn:
                    oppo_checker[pos] += 1
                else:
                    your_checker[pos] += 1
                cnt += 1
            cnt += 1
            pos += 1
        if cnt == len(bin_num):
            break
    for i in range(POINTS):
        if your_checker[i]:
            pos_checker[i+1] = bottom_p[your_checker[i]-1]
    for i in range(POINTS):
        if oppo_checker[i]:
            pos_checker[POINTS-i-1] = top_p[oppo_checker[i]-1]
    for i in range(POINTS+1):
        if not pos_checker[i]:
            pos_checker[i] = "-"
    pos_checker = "".join(pos_checker) + ":"
    return pos_checker


def matchID2XGID(gnu):
    binary_str = ""
    score_str = ""
    for i in range(len(gnu)):
        binary_str += decode_base64(gnu[i])
    bgID = [binary_str[0:8], binary_str[8:16], binary_str[16:24], binary_str[24:32],
            binary_str[32:40], binary_str[40:48], binary_str[48:56], binary_str[56:64], binary_str[64:]]
    for i in range(GNU_MATCH):
        bgID[i] = "".join(list(reversed(bgID[i])))
    bin_num = "".join(bgID)

    cube = '0b' + "".join(list(reversed(bin_num[0:4])))
    cube = int(cube, 0)
    cube_own = bin_num[4:6]
    turn = int(bin_num[6])
    craw = bin_num[7]
#  cond = bin_num[8:11]
#  cube_judge = bin_num[11]
    double = int(bin_num[12])
#  resign = bin_num[13:15]
    dice1 = '0b' + "".join(list(reversed(bin_num[15:18])))
    dice1 = int(dice1, 0)
    dice2 = '0b' + "".join(list(reversed(bin_num[18:21])))
    dice2 = int(dice2, 0)
    m_length = '0b' + "".join(list(reversed(bin_num[21:36])))
    m_length = int(m_length, 0)
    score_you = '0b' + "".join(list(reversed(bin_num[36:51])))
    score_you = int(score_you, 0)
    score_oppo = '0b' + "".join(list(reversed(bin_num[51:66])))
    score_oppo = int(score_oppo, 0)

    score_str += str(cube) + ":"

    if cube_own == "11":
        score_str += "0:"
    elif cube_own == "01":
        score_str += "1:"
    elif cube_own == "00":
        score_str += "-1:"

    if turn == 0:
        score_str += "-1:"
    else:
        score_str += "1:"

    if double:
        score_str += "DD:"
    else:
        score_str += str(dice1) + str(dice2) + ":"

    score_str += str(score_you) + ":" + str(score_oppo) + ":"

    score_str += str(craw) + ":"

    score_str += str(m_length) + ":"

    score_str += "9"

    return score_str


XGID = ""

print(f'Input ID:')
inputID = input()

im = Image.new('RGB', (WIDTH, HEIGHT), WHITE)
draw = ImageDraw.Draw(im)

judge = inputID.split(":")

if inputID[0:5] == "XGID=":
    XGID = inputID[5:]
elif inputID[0:5] == "bgID=":
    judge = inputID[5:].split(":")
    XGID = posID2XGID(judge[0])
    XGID += matchID2XGID(judge[1])
    judge = XGID.split(":")
    if judge[3] == "-1":
        rev_pos = "".join(list(reversed(judge[0])))
        judge[0] = rev_pos.swapcase()
    XGID = ":".join(judge)
elif len(judge) == 2:
    XGID = posID2XGID(judge[0])
    XGID += matchID2XGID(judge[1])
    judge = XGID.split(":")
    if judge[3] == "-1":
        rev_pos = "".join(list(reversed(judge[0])))
        judge[0] = rev_pos.swapcase()
    XGID = ":".join(judge)
elif len(judge) == 10:
    XGID = inputID
else:
    print("ID形式を指定してください([XGID] or [bgID]")
    sys.exit("Error: Turn Incorrect.")

XGID = XGID.split(":")

draw = draw_base(draw)
draw = draw_pos(XGID, im, draw)
draw = draw_cube(XGID, im, draw)
draw = draw_dice(XGID, im, draw)

'''
if int(XGID[3]) == 1:
    im_base = Image.open(num_image + "pos.png")
    im_base.paste(im, (0, PNT_WIDTH))
elif int(XGID[3]) == -1:
    im_base = Image.open(num_image + "pos2.png")
    im_base.paste(im, (0, PNT_WIDTH))
else:
    print("Error: Turn incorrect.")
    sys.exit()
'''

f_out = datetime.datetime.now()
f_out = f_out.strftime('%Y%m%d-%H%M%S') + '.png'
im.save("sample.png")

you = int(XGID[5])
oppo = int(XGID[6])
craw = int(XGID[7])
length = int(XGID[8])
pnt_you = length - you
pnt_oppo = length - oppo

if pnt_you == 1 and not craw:
    craw = "Post Crawfold"
elif pnt_oppo == 1 and not craw:
    craw = "Post Crawfold"

if craw:
    craw = "Crawfold"
else:
    craw = ""

print(f'Match: {length} Point(s).   Score: {you}({pnt_you} away) - {oppo}({pnt_oppo} away) {craw}')
print(f"Output Completed!")
dummy = input()

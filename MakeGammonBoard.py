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

from re import I
from PIL import Image, ImageDraw, ImageFont

import sys
import os
import string

top_p = [chr(ord("a")+i) for i in range(16)]
bottom_p = [chr(ord("A")+i) for i in range(16)]
#num_image = "number/"
POINTS = 25
WIDTH = 1420
HEIGHT = 1300
L_MARGIN = 10
T_MARGIN = 100
BLACK = (0, 0, 0, 255)
CH_GRAY = (179, 179, 179, 255)
WHITE = (255, 255, 255, 255)
BOARD_GREY = (77, 77, 77, 255)
CLEAR = (255, 255, 255, 0)
RADIUS = 80
PNT_WIDTH = 100
LR_MARGIN = 20
BT_MARGIN = 200
MARGIN = (PNT_WIDTH - RADIUS) // 2
POS_T_MARGIN = 5
POS_L_MARGIN = 68
POS_L2_MARGIN = 20
GNU_POS = 10
GNU_MATCH = 9

# font information
font_coords = ImageFont.truetype('SourceHanSans-Normal.otf', 72)
font_num = ImageFont.truetype('SourceHanSans-Normal.otf', 56)
font_info = ImageFont.truetype('SourceHanSans-Normal.otf', 40)


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

# drawing base lines


def draw_base(drawing):
    # each positions with marble
    for i in range(6):
        if i % 2 == 0:
            drawing.polygon((L_MARGIN + i*PNT_WIDTH, T_MARGIN, L_MARGIN + (i+1)*PNT_WIDTH - PNT_WIDTH//2,
                             HEIGHT // 2 - PNT_WIDTH//2, L_MARGIN + (i+1)*PNT_WIDTH, T_MARGIN), fill=WHITE, outline=BLACK)
            drawing.polygon((L_MARGIN + i*PNT_WIDTH + (WIDTH - LR_MARGIN)//2, T_MARGIN, L_MARGIN + (i+1)*PNT_WIDTH + (WIDTH-LR_MARGIN)//2 -
                             PNT_WIDTH//2, HEIGHT//2-PNT_WIDTH//2, L_MARGIN + (i+1)*PNT_WIDTH + (WIDTH-LR_MARGIN)//2, T_MARGIN), fill=WHITE, outline=BLACK)
            drawing.polygon((L_MARGIN + (i+1)*PNT_WIDTH, HEIGHT - BT_MARGIN, L_MARGIN + (i+2)*PNT_WIDTH - PNT_WIDTH //
                             2, HEIGHT // 2 + PNT_WIDTH//2, L_MARGIN + (i+2)*PNT_WIDTH, HEIGHT - BT_MARGIN), fill=WHITE, outline=BLACK)
            drawing.polygon((L_MARGIN + (i+1)*PNT_WIDTH + (WIDTH - LR_MARGIN)//2, HEIGHT - BT_MARGIN, L_MARGIN + (i+2)*PNT_WIDTH + (WIDTH - LR_MARGIN)//2 -
                             PNT_WIDTH // 2, HEIGHT//2 + PNT_WIDTH//2, L_MARGIN + (i+2)*PNT_WIDTH + (WIDTH - LR_MARGIN)//2, HEIGHT - BT_MARGIN), fill=WHITE, outline=BLACK)
        else:
            drawing.polygon((L_MARGIN + i*PNT_WIDTH, T_MARGIN, L_MARGIN + (i+1)*PNT_WIDTH - PNT_WIDTH//2,
                             HEIGHT // 2-PNT_WIDTH//2, L_MARGIN + (i+1)*PNT_WIDTH, T_MARGIN), fill=BOARD_GREY, outline=BLACK)
            drawing.polygon((L_MARGIN + i*PNT_WIDTH + (WIDTH-LR_MARGIN)//2, T_MARGIN, L_MARGIN + (i+1)*PNT_WIDTH + (WIDTH-LR_MARGIN)//2 -
                             PNT_WIDTH//2, HEIGHT//2-PNT_WIDTH//2, L_MARGIN + (i+1)*PNT_WIDTH + (WIDTH-LR_MARGIN)//2, T_MARGIN), fill=BOARD_GREY, outline=BLACK)
            drawing.polygon((L_MARGIN + (i-1)*PNT_WIDTH, HEIGHT - BT_MARGIN, L_MARGIN + i*PNT_WIDTH - PNT_WIDTH//2,
                             HEIGHT // 2+PNT_WIDTH//2, L_MARGIN + i*PNT_WIDTH, HEIGHT - BT_MARGIN), fill=BOARD_GREY, outline=BLACK)
            drawing.polygon((L_MARGIN + (i-1)*PNT_WIDTH + (WIDTH-LR_MARGIN)//2, HEIGHT - BT_MARGIN, L_MARGIN + i*PNT_WIDTH + (WIDTH-LR_MARGIN)//2 -
                             PNT_WIDTH//2, HEIGHT//2+PNT_WIDTH//2, L_MARGIN + i*PNT_WIDTH + (WIDTH - LR_MARGIN)//2, HEIGHT - BT_MARGIN), fill=BOARD_GREY, outline=BLACK)

    # base rectangle
    drawing.rectangle((L_MARGIN, T_MARGIN, WIDTH - L_MARGIN,
                       HEIGHT - BT_MARGIN), outline=BLACK, width=5)

    # Goal line inside up to down
    drawing.line((WIDTH - PNT_WIDTH - L_MARGIN, T_MARGIN, WIDTH -
                  PNT_WIDTH - L_MARGIN, HEIGHT - BT_MARGIN), fill=BLACK, width=5)

    # center lines
    drawing.line((L_MARGIN + (WIDTH-LR_MARGIN)//2 - PNT_WIDTH, T_MARGIN, L_MARGIN +
                  (WIDTH-LR_MARGIN)//2 - PNT_WIDTH, HEIGHT - BT_MARGIN), fill=BLACK, width=5)
    drawing.line((L_MARGIN + (WIDTH-LR_MARGIN)//2, T_MARGIN, L_MARGIN +
                  (WIDTH-LR_MARGIN)//2, HEIGHT - BT_MARGIN), fill=BLACK, width=5)

    # for taking cube areas
    drawing.line((WIDTH - PNT_WIDTH - L_MARGIN, T_MARGIN + PNT_WIDTH,
                  WIDTH - L_MARGIN, T_MARGIN + PNT_WIDTH), fill=BLACK, width=5)
    drawing.line((WIDTH - PNT_WIDTH - L_MARGIN, HEIGHT - PNT_WIDTH - BT_MARGIN,
                  WIDTH - L_MARGIN, HEIGHT - PNT_WIDTH - BT_MARGIN), fill=BLACK, width=5)
    drawing.line((WIDTH - PNT_WIDTH - L_MARGIN, HEIGHT//2,
                  WIDTH - L_MARGIN, HEIGHT//2), fill=BLACK, width=5)

    # for center cube
    drawing.line((L_MARGIN + (WIDTH-LR_MARGIN)//2-PNT_WIDTH, HEIGHT//2-PNT_WIDTH//2,
                  L_MARGIN + (WIDTH-LR_MARGIN)//2, HEIGHT//2-PNT_WIDTH//2), fill=BLACK, width=5)
    drawing.line((L_MARGIN + (WIDTH-LR_MARGIN)//2-PNT_WIDTH, HEIGHT//2+PNT_WIDTH//2,
                  L_MARGIN + (WIDTH-LR_MARGIN)//2, HEIGHT//2+PNT_WIDTH//2), fill=BLACK, width=5)

    return drawing

# drawing top and bottom coordination numbers


def draw_coords(drawing, turn):
    for i in range(1, 7):
        if turn == 'b':
            drawing.text((WIDTH - L_MARGIN - i*PNT_WIDTH - POS_L_MARGIN, HEIGHT -
                          BT_MARGIN - MARGIN), str(i), font=font_coords, fill=BLACK)
        else:
            drawing.text((WIDTH - L_MARGIN - i*PNT_WIDTH - POS_L_MARGIN,
                          POS_T_MARGIN), str(i), font=font_coords, fill=BLACK)
    for i in range(7, 10):
        if turn == 'b':
            drawing.text(((WIDTH - LR_MARGIN) // 2 + L_MARGIN - (i-6)*PNT_WIDTH - POS_L_MARGIN,
                          HEIGHT - BT_MARGIN - MARGIN), str(i), font=font_coords, fill=BLACK)
        else:
            drawing.text(((WIDTH - LR_MARGIN) // 2 + L_MARGIN - (i-6)*PNT_WIDTH -
                          POS_L_MARGIN, POS_T_MARGIN), str(i), font=font_coords, fill=BLACK)
    for i in range(10, 13):
        if turn == 'b':
            drawing.text(((WIDTH-LR_MARGIN) // 2 + L_MARGIN - (i-6)*PNT_WIDTH - POS_L_MARGIN -
                          POS_L2_MARGIN, HEIGHT - BT_MARGIN - MARGIN), str(i), font=font_coords, fill=BLACK)
        else:
            drawing.text(((WIDTH-LR_MARGIN) // 2 + L_MARGIN - (i-6)*PNT_WIDTH - POS_L_MARGIN -
                          POS_L2_MARGIN, POS_T_MARGIN), str(i), font=font_coords, fill=BLACK)
    for i in range(13, 19):
        if turn == 'b':
            drawing.text(((i-13)*PNT_WIDTH + POS_L2_MARGIN,
                          POS_T_MARGIN), str(i), font=font_coords, fill=BLACK)
        else:
            drawing.text(((i-13)*PNT_WIDTH + POS_L2_MARGIN, HEIGHT -
                          BT_MARGIN - MARGIN), str(i), font=font_coords, fill=BLACK)
    for i in range(19, 25):
        if turn == 'b':
            drawing.text(((WIDTH-LR_MARGIN) // 2 + L_MARGIN + (i-18)*PNT_WIDTH - POS_L_MARGIN -
                          POS_L2_MARGIN, POS_T_MARGIN), str(i), font=font_coords, fill=BLACK)
        else:
            drawing.text(((WIDTH-LR_MARGIN) // 2 + L_MARGIN + (i-18)*PNT_WIDTH - POS_L_MARGIN -
                          POS_L2_MARGIN, HEIGHT - BT_MARGIN - MARGIN), str(i), font=font_coords, fill=BLACK)
    return drawing

# drawing checkers


def print_circle(pos, num, own, drawing):
    # on the bar
    if pos == 0:
        if num >= 10:
            drawing.ellipse(((WIDTH-LR_MARGIN)//2 - PNT_WIDTH + MARGIN + L_MARGIN, HEIGHT*3//4 - RADIUS//2 - T_MARGIN // 3, (WIDTH -
                                                                                                                         LR_MARGIN) // 2 - MARGIN + L_MARGIN, HEIGHT*3//4 + RADIUS//2 - T_MARGIN // 3), fill=CH_GRAY, outline=BLACK, width=3)
            drawing.text(((WIDTH - LR_MARGIN)//2 - PNT_WIDTH//2 - MARGIN*2,
                      HEIGHT*3//4 - MARGIN * 8), str(num), font=font_num, fill=BLACK)
        else:
            drawing.ellipse(((WIDTH-LR_MARGIN)//2 - PNT_WIDTH + MARGIN + L_MARGIN, HEIGHT*3//4 - RADIUS//2 - T_MARGIN // 3, (WIDTH -
                                                                                                                         LR_MARGIN) // 2 - MARGIN + L_MARGIN, HEIGHT*3//4 + RADIUS//2 - T_MARGIN // 3), fill=CH_GRAY, outline=BLACK, width=3)
            drawing.text(((WIDTH - LR_MARGIN)//2 - PNT_WIDTH // 2 - MARGIN // 2,
                      HEIGHT*3//4 - MARGIN * 8), str(num), font=font_num, fill=BLACK)
    # right bottom
    if 0 < pos < 7:
        for i in range(num):
            if own == "b":
                drawing.ellipse((WIDTH - PNT_WIDTH*(pos+1) + MARGIN - L_MARGIN, HEIGHT-RADIUS*(i+1) - BT_MARGIN, WIDTH -
                                 PNT_WIDTH*pos - MARGIN - L_MARGIN, HEIGHT-RADIUS*i - BT_MARGIN), fill=WHITE, outline=BLACK, width=3)
            elif own == "t":
                drawing.ellipse((WIDTH - PNT_WIDTH*(pos+1) + MARGIN - L_MARGIN, HEIGHT-RADIUS*(i+1) - BT_MARGIN, WIDTH -
                                 PNT_WIDTH*pos - MARGIN - L_MARGIN, HEIGHT - RADIUS*i - BT_MARGIN), fill=CH_GRAY, outline=BLACK, width=3)
            else:
                print("Error: Wrong at making right-bottom.")
                dummy = input()
                sys.exit()
            if 3 < i:
                if 10 <= num:
                    drawing.text((WIDTH - PNT_WIDTH*(pos+1) + L_MARGIN, HEIGHT -
                              BT_MARGIN - RADIUS*5 - MARGIN // 3), str(num), font=font_num, fill=BLACK)
                    break
                else:
                    drawing.text((WIDTH - PNT_WIDTH*(pos+1) + L_MARGIN, HEIGHT -
                              BT_MARGIN - RADIUS*5 - MARGIN // 3), str(num), font=font_num, fill=BLACK)
                    break
    # left bottom
    elif 7 <= pos < 13:
        for i in range(num):
            if own == "b":
                drawing.ellipse(((WIDTH-LR_MARGIN)//2 - (pos-5)*PNT_WIDTH + MARGIN + L_MARGIN, HEIGHT - BT_MARGIN - RADIUS*(i+1), (WIDTH -
                                                                                                                                   LR_MARGIN)//2 - (pos-6)*PNT_WIDTH - MARGIN + L_MARGIN, HEIGHT - RADIUS*i - BT_MARGIN), fill=WHITE, outline=BLACK, width=3)
            elif own == "t":
                drawing.ellipse(((WIDTH-LR_MARGIN)//2 - (pos-5)*PNT_WIDTH + MARGIN + L_MARGIN, HEIGHT - BT_MARGIN - RADIUS*(i+1), (WIDTH -
                                                                                                                                   LR_MARGIN)//2 - (pos-6)*PNT_WIDTH - MARGIN + L_MARGIN, HEIGHT - RADIUS*i - BT_MARGIN), fill=CH_GRAY, outline=BLACK, width=3)
            else:
                print("Error: Wrong at making left-bottom.")
                dummy = input()
                sys.exit()
            if 3 < i:
                if 10 <= num:
                    drawing.text(((WIDTH - LR_MARGIN) // 2 - PNT_WIDTH * (pos-6) - L_MARGIN - MARGIN * 6,
                              HEIGHT - BT_MARGIN - RADIUS*5 - MARGIN // 3), str(num), font=font_num, fill=BLACK)
                    break
                else:
                    drawing.text(((WIDTH - LR_MARGIN) // 2 - PNT_WIDTH * (pos-6) - L_MARGIN - MARGIN * 4.6,
                              HEIGHT - BT_MARGIN - RADIUS*5 - MARGIN // 3), str(num), font=font_num, fill=BLACK)
                    break
    # top left
    elif 13 <= pos < 19:
        for i in range(num):
            if own == "b":
                drawing.ellipse(((pos-13)*PNT_WIDTH + MARGIN + L_MARGIN, RADIUS*i + T_MARGIN, (pos-12) *
                                 PNT_WIDTH - MARGIN + L_MARGIN, RADIUS*(i+1) + T_MARGIN), fill=WHITE, outline=BLACK, width=3)
            elif own == "t":
                drawing.ellipse(((pos-13)*PNT_WIDTH + MARGIN + L_MARGIN, RADIUS*i + T_MARGIN, (pos-12) *
                                 PNT_WIDTH - MARGIN + L_MARGIN, RADIUS*(i+1) + T_MARGIN), fill=CH_GRAY, outline=BLACK, width=3)
            else:
                print("Error: Wrong at making left-upper.")
                dummy = input()
                sys.exit()
            if 3 < i:
                if 10 <= num:
                    drawing.text((L_MARGIN + PNT_WIDTH * (pos - 13) + MARGIN * 2, T_MARGIN +
                              RADIUS*4 - MARGIN // 4), str(num), font=font_num, fill=BLACK)
                    break
                else:
                    drawing.text((L_MARGIN + PNT_WIDTH * (pos - 13) + MARGIN * 3.5, T_MARGIN +
                              RADIUS*4 - MARGIN // 4), str(num), font=font_num, fill=BLACK)
                    break
    # top right
    elif 19 <= pos < 25:
        for i in range(num):
            if own == "b":
                drawing.ellipse(((WIDTH - LR_MARGIN)//2 + (pos-19)*PNT_WIDTH + MARGIN + L_MARGIN, RADIUS*i + T_MARGIN, (WIDTH - LR_MARGIN) //
                                 2 + (pos-18)*PNT_WIDTH - MARGIN + L_MARGIN, RADIUS*(i+1) + T_MARGIN), fill=WHITE, outline=BLACK, width=3)
            elif own == "t":
                drawing.ellipse(((WIDTH - LR_MARGIN)//2 + (pos-19)*PNT_WIDTH + MARGIN + L_MARGIN, RADIUS*i + T_MARGIN, (WIDTH - LR_MARGIN) //
                                 2 + (pos-18)*PNT_WIDTH - MARGIN + L_MARGIN, RADIUS*(i+1) + T_MARGIN), fill=CH_GRAY, outline=BLACK, width=3)
            else:
                print("Error: Wrong at making right-upper")
                dummy = input()
                sys.exit()
            if 3 < i:
                if 10 <= num:
                    drawing.text(((WIDTH - LR_MARGIN)//2 + (pos-19)*PNT_WIDTH + POS_L2_MARGIN + MARGIN, T_MARGIN + RADIUS*4 - MARGIN // 4), str(num), font=font_num, fill=BLACK)
                    break
                else:
                    drawing.text(((WIDTH - LR_MARGIN)//2 + (pos-19)*PNT_WIDTH + POS_L2_MARGIN * 2 +
                              MARGIN//2, T_MARGIN + RADIUS*4 - MARGIN // 4), str(num), font=font_num, fill=BLACK)
                    break

    # on the bar
    elif pos == 25:
        if num >= 10:
            drawing.ellipse(((WIDTH-LR_MARGIN)//2 - PNT_WIDTH + MARGIN + L_MARGIN, HEIGHT//4 - RADIUS//2 - T_MARGIN * 3 // 4,
                        (WIDTH-LR_MARGIN) // 2 - MARGIN + L_MARGIN, HEIGHT//4 + RADIUS//2 - T_MARGIN * 3 // 4), fill=WHITE, outline=BLACK, width=3)
            drawing.text(((WIDTH - LR_MARGIN)//2 - PNT_WIDTH//2 - MARGIN*2, HEIGHT//4 - MARGIN * 12), str(num), font=font_num, fill=BLACK)
        else:
            drawing.ellipse(((WIDTH-LR_MARGIN)//2 - PNT_WIDTH + MARGIN + L_MARGIN, HEIGHT//4 - RADIUS//2 - T_MARGIN * 3 // 4,
                        (WIDTH-LR_MARGIN) // 2 - MARGIN + L_MARGIN, HEIGHT//4 + RADIUS//2 - T_MARGIN * 3 // 4), fill=WHITE, outline=BLACK, width=3)
            drawing.text(((WIDTH - LR_MARGIN)//2 - PNT_WIDTH // 2 - MARGIN, HEIGHT//4 - MARGIN * 12), str(num), font=font_num, fill=BLACK)
    return drawing

# putting checkers by XGID


def draw_pos(XGID, im, drawing):
    top_num = 15
    bottom_num = 15
    for i in range(26):
        if XGID[0][i] == "-":
            continue
        else:
            if XGID[0][i] in top_p:
                ch_num = top_p.index(XGID[0][i]) + 1
                top_num -= ch_num
                drawing = print_circle(i, ch_num, "t", drawing)
            elif XGID[0][i] in bottom_p:
                ch_num = bottom_p.index(XGID[0][i]) + 1
                bottom_num -= ch_num
                drawing = print_circle(i, ch_num, "b", drawing)
            else:
                return "Error at XGID positions."
    # detecting Errors about number of checkers
    if top_num < 0:
        return "Error: Too small checkers for the top-player!"
    elif bottom_num < 0:
        return "Error: Too small checkers for the bottom-player!"
    # putting checkers off the game
    else:
        if top_num > 0:
            if top_num >= 10:
                drawing.ellipse((WIDTH - PNT_WIDTH - L_MARGIN + MARGIN, HEIGHT//4, WIDTH - PNT_WIDTH -
                            L_MARGIN + MARGIN + RADIUS, HEIGHT//4 + RADIUS), fill=CH_GRAY, outline=BLACK, width=3)
                drawing.text((WIDTH - L_MARGIN - MARGIN*8, HEIGHT //
                            4 - MARGIN//2), str(top_num), font=font_num, fill=BLACK)
            else:
                drawing.ellipse((WIDTH - PNT_WIDTH - L_MARGIN + MARGIN, HEIGHT//4, WIDTH - PNT_WIDTH -
                            L_MARGIN + MARGIN + RADIUS, HEIGHT//4 + RADIUS), fill=CH_GRAY, outline=BLACK, width=3)
                drawing.text((WIDTH - L_MARGIN - MARGIN*6.5, HEIGHT //
                            4 - MARGIN//2), str(top_num), font=font_num, fill=BLACK)
        if bottom_num > 0:
            if bottom_num >= 10:
                drawing.ellipse((WIDTH - PNT_WIDTH - L_MARGIN + MARGIN, HEIGHT*3//4 - PNT_WIDTH - MARGIN*4, WIDTH - PNT_WIDTH -
                            L_MARGIN + MARGIN + RADIUS, HEIGHT*3//4 + RADIUS - PNT_WIDTH - MARGIN*4), fill=WHITE, outline=BLACK, width=3)
                drawing.text((WIDTH - L_MARGIN - MARGIN*8, HEIGHT*3//4 - PNT_WIDTH -
                            MARGIN*4.5), str(bottom_num), font=font_num, fill=BLACK)
            else:
                drawing.ellipse((WIDTH - PNT_WIDTH - L_MARGIN + MARGIN, HEIGHT*3//4 - PNT_WIDTH - MARGIN*4, WIDTH - PNT_WIDTH -
                            L_MARGIN + MARGIN + RADIUS, HEIGHT*3//4 + RADIUS - PNT_WIDTH - MARGIN*4), fill=WHITE, outline=BLACK, width=3)
                drawing.text((WIDTH - L_MARGIN - MARGIN*6.5, HEIGHT*3//4 - PNT_WIDTH -
                            MARGIN*4.5), str(bottom_num), font=font_num, fill=BLACK)
    return drawing

# drawing rolling cubes


def draw_cube(XGID, im, drawing):
    if int(XGID[3]) == 1:
        cube_num = 2**(int(XGID[1]))
        # show double
        if XGID[4] == "DD":
            cube_num = 2**(int(XGID[1])+1)
            d_cube = Image.new('RGBA', (PNT_WIDTH*2 // 3, PNT_WIDTH), CLEAR)
            d_cube_draw = ImageDraw.Draw(d_cube)
            d_cube_draw.text((0, 0), str(cube_num), font=font_num, fill=BLACK)
            d_cube = d_cube.rotate(180)
            drawing.rectangle((int(2.5*PNT_WIDTH)+MARGIN + L_MARGIN, HEIGHT//2-PNT_WIDTH//2+MARGIN, int(2.5*PNT_WIDTH) +
                               RADIUS+MARGIN + L_MARGIN, HEIGHT//2-PNT_WIDTH//2+RADIUS+MARGIN), fill=CLEAR, outline=BLACK, width=5)
            if cube_num < 10:
                im.paste(d_cube, (int(PNT_WIDTH*2.4) + MARGIN + L_MARGIN,
                                  HEIGHT//2 - PNT_WIDTH//2 - int(MARGIN*0.5)), mask=d_cube)
            else:
                im.paste(d_cube, (int(PNT_WIDTH*2) + int(MARGIN*6.5) + L_MARGIN,
                                  HEIGHT//2 - PNT_WIDTH//2 - int(MARGIN*0.5)), mask=d_cube)
            return drawing
        # on the  bottom player
        if int(XGID[2]) == 1:
            d_cube = Image.new('RGBA', (PNT_WIDTH, PNT_WIDTH), CLEAR)
            d_cube_draw = ImageDraw.Draw(d_cube)
            d_cube_draw.text((0, 0), str(cube_num),
                             font=font_coords, fill=BLACK)
            if cube_num < 10:
                im.paste(d_cube, (WIDTH - PNT_WIDTH + int(MARGIN * 2.25),
                                  HEIGHT - BT_MARGIN - PNT_WIDTH - int(MARGIN*0.5)), mask=d_cube)
            else:
                im.paste(d_cube, (WIDTH - PNT_WIDTH, HEIGHT -
                                  BT_MARGIN - PNT_WIDTH - int(MARGIN*0.5)), mask=d_cube)
            return drawing
        # on the top player
        elif int(XGID[2]) == -1:
            d_cube = Image.new('RGBA', (PNT_WIDTH, PNT_WIDTH), CLEAR)
            d_cube_draw = ImageDraw.Draw(d_cube)
            d_cube_draw.text((0, 0), str(cube_num),
                             font=font_coords, fill=BLACK)
            d_cube = d_cube.rotate(180)
            if cube_num < 10:
                im.paste(d_cube, (WIDTH - PNT_WIDTH - int(MARGIN * 4),
                                  T_MARGIN + MARGIN), mask=d_cube)
            else:
                im.paste(d_cube, (WIDTH - PNT_WIDTH -
                                  int(MARGIN * 2.1), T_MARGIN + MARGIN), mask=d_cube)
            return drawing
        # doubling cube is on the center position
        elif int(XGID[2]) == 0:
            d_cube = Image.new('RGBA', (PNT_WIDTH, PNT_WIDTH), CLEAR)
            d_cube_draw = ImageDraw.Draw(d_cube)
            d_cube_draw.text((0, 0), str(64), font=font_coords, fill=BLACK)
            d_cube = d_cube.rotate(90)
            im.paste(d_cube, (PNT_WIDTH * 6 + int(MARGIN*0.4),
                              HEIGHT // 2 - MARGIN * 6), mask=d_cube)
            return drawing
    elif int(XGID[3]) == -1:
        cube_num = 2**(int(XGID[1]))
        # show double
        if XGID[4] == "DD":
            cube_num = 2**(int(XGID[1])+1)
            drawing.rectangle((WIDTH//2+int(2.5*PNT_WIDTH)+MARGIN, HEIGHT//2-PNT_WIDTH//2+MARGIN, WIDTH//2+int(
                2.5*PNT_WIDTH)+RADIUS+MARGIN, HEIGHT//2-PNT_WIDTH//2+RADIUS+MARGIN), fill=WHITE, outline=BLACK, width=5)
            if cube_num < 10:
                drawing.text(((WIDTH-LR_MARGIN) // 2 + int(PNT_WIDTH*3) - int(MARGIN*1.4) + L_MARGIN,
                              HEIGHT//2 - PNT_WIDTH//2 + int(MARGIN*0.75)), str(cube_num), font=font_num, fill=BLACK)
            else:
                drawing.text(((WIDTH-LR_MARGIN) // 2 + int(PNT_WIDTH*2.6) + int(MARGIN) + L_MARGIN,
                              HEIGHT//2 - PNT_WIDTH//2 + int(MARGIN*0.8)), str(cube_num), font=font_num, fill=BLACK)
            return drawing
        # on the bottom player
        if int(XGID[2]) == 1:
            d_cube = Image.new('RGBA', (PNT_WIDTH, PNT_WIDTH), CLEAR)
            d_cube_draw = ImageDraw.Draw(d_cube)
            d_cube_draw.text((0, 0), str(cube_num),
                             font=font_coords, fill=BLACK)
            if cube_num < 10:
                im.paste(d_cube, (WIDTH - PNT_WIDTH + int(MARGIN * 2.25),
                                  HEIGHT - BT_MARGIN - PNT_WIDTH - int(MARGIN*0.5)), mask=d_cube)
            else:
                im.paste(d_cube, (WIDTH - PNT_WIDTH, HEIGHT -
                                  BT_MARGIN - PNT_WIDTH - int(MARGIN*0.5)), mask=d_cube)
            return drawing
        # on the top player
        elif int(XGID[2]) == -1:
            d_cube = Image.new('RGBA', (PNT_WIDTH, PNT_WIDTH), CLEAR)
            d_cube_draw = ImageDraw.Draw(d_cube)
            d_cube_draw.text((0, 0), str(cube_num),
                             font=font_coords, fill=BLACK)
            d_cube = d_cube.rotate(180)
            if cube_num < 10:
                im.paste(d_cube, (WIDTH - PNT_WIDTH - int(MARGIN * 4),
                                  T_MARGIN + MARGIN), mask=d_cube)
            else:
                im.paste(d_cube, (WIDTH - PNT_WIDTH -
                                  int(MARGIN * 2.1), T_MARGIN + MARGIN), mask=d_cube)
            return drawing
        # doubling cube is on the center
        elif int(XGID[2]) == 0:
            d_cube = Image.new('RGBA', (PNT_WIDTH, PNT_WIDTH), CLEAR)
            d_cube_draw = ImageDraw.Draw(d_cube)
            d_cube_draw.text((0, 0), str(64), font=font_coords, fill=BLACK)
            d_cube = d_cube.rotate(90)
            im.paste(d_cube, (PNT_WIDTH * 6 + int(MARGIN*0.4),
                              HEIGHT // 2 - MARGIN * 6), mask=d_cube)
            return drawing
    # Error exceptions
    else:
        return "Error: Doubling cube incorrect"

# functions for making normal cube


def dice_make(num, order):
    SPACE = 20
    DOTS = 16
    DIFF = 2
    if order == 'b':
        dice = Image.new('RGBA', (PNT_WIDTH - SPACE + DIFF,
                                  PNT_WIDTH - SPACE + DIFF), WHITE)
    else:
        dice = Image.new('RGBA', (PNT_WIDTH - SPACE + DIFF,
                                  PNT_WIDTH - SPACE + DIFF), CH_GRAY)
    dice_draw = ImageDraw.Draw(dice)
    dice_draw.rectangle(
        (0, 0, PNT_WIDTH - SPACE, PNT_WIDTH - SPACE), outline=BLACK, width=5)
    if num == 1:
        dice_draw.ellipse(((PNT_WIDTH - SPACE) // 2 - DOTS//2, (PNT_WIDTH - SPACE) // 2 - DOTS // 2,
                           (PNT_WIDTH - SPACE) // 2 + DOTS // 2, (PNT_WIDTH - SPACE) // 2 + DOTS // 2), fill=BLACK)
    elif num == 2:
        dice_draw.ellipse(((PNT_WIDTH - SPACE) // 4 - DOTS//2, (PNT_WIDTH - SPACE) // 4 - DOTS // 2,
                           (PNT_WIDTH - SPACE) // 4 + DOTS // 2, (PNT_WIDTH - SPACE) // 4 + DOTS // 2), fill=BLACK)
        dice_draw.ellipse(((PNT_WIDTH - SPACE) * 3 // 4 - DOTS//2, (PNT_WIDTH - SPACE) * 3 // 4 - DOTS // 2,
                           (PNT_WIDTH - SPACE) * 3 // 4 + DOTS // 2, (PNT_WIDTH - SPACE) * 3 // 4 + DOTS // 2), fill=BLACK)
    elif num == 3:
        dice_draw.ellipse(((PNT_WIDTH - SPACE) // 2 - DOTS//2, (PNT_WIDTH - SPACE) // 2 - DOTS // 2,
                           (PNT_WIDTH - SPACE) // 2 + DOTS // 2, (PNT_WIDTH - SPACE) // 2 + DOTS // 2), fill=BLACK)
        dice_draw.ellipse(((PNT_WIDTH - SPACE) // 4 - DOTS//2, (PNT_WIDTH - SPACE) * 3 // 4 - DOTS // 2,
                           (PNT_WIDTH - SPACE) // 4 + DOTS // 2, (PNT_WIDTH - SPACE) * 3 // 4 + DOTS // 2), fill=BLACK)
        dice_draw.ellipse(((PNT_WIDTH - SPACE) * 3 // 4 - DOTS//2, (PNT_WIDTH - SPACE) // 4 - DOTS // 2,
                           (PNT_WIDTH - SPACE) * 3 // 4 + DOTS // 2, (PNT_WIDTH - SPACE) // 4 + DOTS // 2), fill=BLACK)
    elif num == 4:
        dice_draw.ellipse(((PNT_WIDTH - SPACE) // 4 - DOTS//2, (PNT_WIDTH - SPACE) // 4 - DOTS // 2,
                           (PNT_WIDTH - SPACE) // 4 + DOTS // 2, (PNT_WIDTH - SPACE) // 4 + DOTS // 2), fill=BLACK)
        dice_draw.ellipse(((PNT_WIDTH - SPACE) * 3 // 4 - DOTS//2, (PNT_WIDTH - SPACE) // 4 - DOTS // 2,
                           (PNT_WIDTH - SPACE) * 3 // 4 + DOTS // 2, (PNT_WIDTH - SPACE) // 4 + DOTS // 2), fill=BLACK)
        dice_draw.ellipse(((PNT_WIDTH - SPACE) // 4 - DOTS//2, (PNT_WIDTH - SPACE) * 3 // 4 - DOTS // 2,
                           (PNT_WIDTH - SPACE) // 4 + DOTS // 2, (PNT_WIDTH - SPACE) * 3 // 4 + DOTS // 2), fill=BLACK)
        dice_draw.ellipse(((PNT_WIDTH - SPACE) * 3 // 4 - DOTS//2, (PNT_WIDTH - SPACE) * 3 // 4 - DOTS // 2,
                           (PNT_WIDTH - SPACE) * 3 // 4 + DOTS // 2, (PNT_WIDTH - SPACE) * 3 // 4 + DOTS // 2), fill=BLACK)
    elif num == 5:
        dice_draw.ellipse(((PNT_WIDTH - SPACE) // 2 - DOTS//2, (PNT_WIDTH - SPACE) // 2 - DOTS // 2,
                           (PNT_WIDTH - SPACE) // 2 + DOTS // 2, (PNT_WIDTH - SPACE) // 2 + DOTS // 2), fill=BLACK)
        dice_draw.ellipse(((PNT_WIDTH - SPACE) // 4 - DOTS//2, (PNT_WIDTH - SPACE) // 4 - DOTS // 2,
                           (PNT_WIDTH - SPACE) // 4 + DOTS // 2, (PNT_WIDTH - SPACE) // 4 + DOTS // 2), fill=BLACK)
        dice_draw.ellipse(((PNT_WIDTH - SPACE) * 3 // 4 - DOTS//2, (PNT_WIDTH - SPACE) // 4 - DOTS // 2,
                           (PNT_WIDTH - SPACE) * 3 // 4 + DOTS // 2, (PNT_WIDTH - SPACE) // 4 + DOTS // 2), fill=BLACK)
        dice_draw.ellipse(((PNT_WIDTH - SPACE) // 4 - DOTS//2, (PNT_WIDTH - SPACE) * 3 // 4 - DOTS // 2,
                           (PNT_WIDTH - SPACE) // 4 + DOTS // 2, (PNT_WIDTH - SPACE) * 3 // 4 + DOTS // 2), fill=BLACK)
        dice_draw.ellipse(((PNT_WIDTH - SPACE) * 3 // 4 - DOTS//2, (PNT_WIDTH - SPACE) * 3 // 4 - DOTS // 2,
                           (PNT_WIDTH - SPACE) * 3 // 4 + DOTS // 2, (PNT_WIDTH - SPACE) * 3 // 4 + DOTS // 2), fill=BLACK)
    elif num == 6:
        dice_draw.ellipse(((PNT_WIDTH - SPACE) // 4 - DOTS//2, (PNT_WIDTH - SPACE) // 4 - DOTS // 2,
                           (PNT_WIDTH - SPACE) // 4 + DOTS // 2, (PNT_WIDTH - SPACE) // 4 + DOTS // 2), fill=BLACK)
        dice_draw.ellipse(((PNT_WIDTH - SPACE) * 3 // 4 - DOTS//2, (PNT_WIDTH - SPACE) // 4 - DOTS // 2,
                           (PNT_WIDTH - SPACE) * 3 // 4 + DOTS // 2, (PNT_WIDTH - SPACE) // 4 + DOTS // 2), fill=BLACK)
        dice_draw.ellipse(((PNT_WIDTH - SPACE) // 4 - DOTS//2, (PNT_WIDTH - SPACE) * 3 // 4 - DOTS // 2,
                           (PNT_WIDTH - SPACE) // 4 + DOTS // 2, (PNT_WIDTH - SPACE) * 3 // 4 + DOTS // 2), fill=BLACK)
        dice_draw.ellipse(((PNT_WIDTH - SPACE) // 2 - DOTS//2, (PNT_WIDTH - SPACE) // 4 - DOTS // 2,
                           (PNT_WIDTH - SPACE) // 2 + DOTS // 2, (PNT_WIDTH - SPACE) // 4 + DOTS // 2), fill=BLACK)
        dice_draw.ellipse(((PNT_WIDTH - SPACE) * 3 // 4 - DOTS//2, (PNT_WIDTH - SPACE) * 3 // 4 - DOTS // 2,
                           (PNT_WIDTH - SPACE) * 3 // 4 + DOTS // 2, (PNT_WIDTH - SPACE) * 3 // 4 + DOTS // 2), fill=BLACK)
        dice_draw.ellipse(((PNT_WIDTH - SPACE) // 2 - DOTS//2, (PNT_WIDTH - SPACE) * 3 // 4 - DOTS // 2,
                           (PNT_WIDTH - SPACE) // 2 + DOTS // 2, (PNT_WIDTH - SPACE) * 3 // 4 + DOTS // 2), fill=BLACK)
    # Error Exceptions
    else:
        return "Error: Dice Error"
    return dice

# drawing dice


def draw_dice(XGID, im, drawing):
    if int(XGID[3]) == 1:
        # no dide
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
        dice1_im = dice_make(int(dice1), 'b')
        dice2_im = dice_make(int(dice2), 'b')
        im.paste(dice1_im, (WIDTH//2+2*PNT_WIDTH+MARGIN,
                            HEIGHT//2-PNT_WIDTH//2+MARGIN), mask=dice1_im)
        im.paste(dice2_im, (WIDTH//2+3*PNT_WIDTH+MARGIN,
                            HEIGHT//2-PNT_WIDTH//2+MARGIN), mask=dice2_im)
        return drawing
    elif int(XGID[3]) == -1:
        # no dice
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
        dice1_im = dice_make(int(dice1), 't')
        dice2_im = dice_make(int(dice2), 't')
        im.paste(dice1_im, (2*PNT_WIDTH+MARGIN, HEIGHT //
                            2-PNT_WIDTH//2+MARGIN), mask=dice1_im)
        im.paste(dice2_im, (3*PNT_WIDTH+MARGIN, HEIGHT //
                            2-PNT_WIDTH//2+MARGIN), mask=dice2_im)
        return drawing
    # Error Exceptions
    else:
        print("Error: Turn incorrect.")
        dummy = input()
        sys.exit()

# converting gnubg position information to posID


def gnubg2posID(gnu):
    encoded_ID = [_ for _ in range(14)]
    binary_str = ""
    bgID = [gnu[0:8], gnu[8:16], gnu[16:24], gnu[24:32], gnu[32:40],
            gnu[40:48], gnu[48:56], gnu[56:64], gnu[64:72], gnu[72:80]]
    for i in range(GNU_POS):
        bgID[i] = "".join(list(reversed(bgID[i])))
    for i in range(GNU_POS):
        bin_num = "".join(bgID)
    encoded_ID = [int(bin_num[0:6], 2), int(bin_num[6:12], 2), int(bin_num[12:18], 2), int(bin_num[18:24], 2), int(bin_num[24:30], 2), int(bin_num[30:36], 2), int(bin_num[36:42], 2), int(
        bin_num[42:48], 2), int(bin_num[48:54], 2), int(bin_num[54:60], 2), int(bin_num[60:66], 2), int(bin_num[66:72], 2), int(bin_num[72:78], 2), int(bin_num[78:] + "0000", 2)]
    for i in range(14):
        binary_str += encode_base64(encoded_ID[i])
    return binary_str

# converting gnubg match information to matchID


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

# converting posID to XGID


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

# converting matchID to XGID


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
    elif cube_own == "10":
        score_str += "1:"
    elif cube_own == "00":
        score_str += "-1:"
    else:
        print("Cube Pos Error!")
        sys.exit()

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


def main():
    args = sys.argv
    if len(args) != 2:
        print("Illegal Number of Arguments!")
        sys.exit()

    XGID = ""

    with open(args[1], 'r') as f:
        num = int(f.readline())
        for qnum in range(num):
            inputID = f.readline()

            inputID = inputID.replace('\n', '')

            im = Image.new('RGB', (WIDTH, HEIGHT), WHITE)
            draw = ImageDraw.Draw(im)

            judge = inputID.split(":")

            if inputID[0:5] == "XGID=":
                XGID = inputID[5:]
                if judge[3] == "-1":
                    judge[3] = "1"
                    if judge[2] == "-1":
                        judge[2] = "1"
                    elif judge[2] == "1":
                        judge[2] = "-1"
                    judge[5], judge[6] = judge[6], judge[5]
                    rev_pos = "".join(list(reversed(judge[0])))
                    judge[0] = rev_pos.swapcase()
                    XGID = ":".join(judge)
            elif inputID[0:5] == "bgID=":
                judge = inputID[5:].split(":")
                XGID = posID2XGID(judge[0])
                XGID += matchID2XGID(judge[1])
                judge = XGID.split(":")
                if judge[3] == "-1":
                    judge[3] = "1"
                    if judge[2] == "-1":
                        judge[2] = "1"
                    elif judge[2] == "1":
                        judge[2] = "-1"
                    judge[5], judge[6] = judge[6], judge[5]
                    rev_pos = "".join(list(reversed(judge[0])))
                    judge[0] = rev_pos.swapcase()
                XGID = ":".join(judge)
            elif len(judge) == 2:
                XGID = posID2XGID(judge[0])
                XGID += matchID2XGID(judge[1])
                judge = XGID.split(":")
                if judge[3] == "-1":
                    judge[3] = "1"
                    if judge[2] == "-1":
                        judge[2] = "1"
                    elif judge[2] == "1":
                        judge[2] = "-1"
                    judge[5], judge[6] = judge[6], judge[5]
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

            if int(XGID[3]) == 1:
                draw = draw_coords(draw, 'b')
            elif int(XGID[3]) == -1:
                draw = draw_coords(draw, 't')
            else:
                print("Error: Turn incorrect.")
                sys.exit()

            f_base = os.path.splitext(os.path.basename(args[1]))[0]

            if qnum == 0:
                f_out = 'Q' + f_base + '.png'
            else:
                f_out = 'A' + f_base + '_' + str(qnum) + '.png'

            oppo = int(XGID[5])
            you = int(XGID[6])
            craw = int(XGID[7])
            length = int(XGID[8])
            pnt_you = length - you
            pnt_oppo = length - oppo

            if craw:
                craw = "[Crawford]"
            else:
                if pnt_you == 1 and length != 1:
                    craw = "[Post Crawford]"
                elif pnt_oppo == 1 and length != 1:
                    craw = "[Post Crawford]"
                else:
                    craw = ""

            text_info = f'Match: {length} Point(s).  Score: Bottom {oppo}({pnt_oppo} away) - {you}({pnt_you} away) Top {craw}'
            draw.text((L_MARGIN, HEIGHT - T_MARGIN),
                      text_info, font=font_info, fill=BLACK)

            im.save(f_out)

            print(f'{f_out} Output Completed')


if __name__ == '__main__':
    main()

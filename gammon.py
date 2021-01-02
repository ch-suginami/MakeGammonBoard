from PIL import Image,ImageDraw

import sys
import string

top_p = [chr(ord("a")+i) for i in range(16)]
bottom_p = [chr(ord("A")+i) for i in range(16)]
num_image = "number/"
WIDTH = 1400
HEIGHT = 1000
BLACK = (0, 0, 0)
CH_GRAY = (179, 179, 179)
WHITE = (255, 255, 255)
BOARD_GREY = (77, 77, 77)
RADIUS = 80
PNT_WIDTH = 100
MARGIN = (PNT_WIDTH -RADIUS) // 2

def draw_base(drawing):
  # each positions
  for i in range(6):
    if i % 2 == 0:
      drawing.polygon((i*PNT_WIDTH, 0, (i+1)*PNT_WIDTH - PNT_WIDTH//2, HEIGHT//2-PNT_WIDTH//2, (i+1)*PNT_WIDTH, 0), fill = WHITE, outline = BLACK)
      drawing.polygon((i*PNT_WIDTH + WIDTH//2, 0, (i+1)*PNT_WIDTH + WIDTH//2 - PNT_WIDTH//2, HEIGHT//2-PNT_WIDTH//2, (i+1)*PNT_WIDTH + WIDTH//2, 0), fill = WHITE, outline = BLACK)
      drawing.polygon(((i+1)*PNT_WIDTH, HEIGHT, (i+2)*PNT_WIDTH - 50, HEIGHT//2+PNT_WIDTH//2, (i+2)*PNT_WIDTH, HEIGHT), fill = WHITE, outline = BLACK)
      drawing.polygon(((i+1)*PNT_WIDTH + WIDTH//2, HEIGHT, (i+2)*PNT_WIDTH + WIDTH//2 - PNT_WIDTH//2, HEIGHT//2+PNT_WIDTH//2, (i+2)*PNT_WIDTH + 700, HEIGHT), fill = WHITE, outline = BLACK)
    else:
      drawing.polygon((i*PNT_WIDTH, 0, (i+1)*PNT_WIDTH - PNT_WIDTH//2, HEIGHT//2-PNT_WIDTH//2, (i+1)*PNT_WIDTH, 0), fill = BOARD_GREY, outline = BLACK)
      drawing.polygon((i*PNT_WIDTH + WIDTH//2, 0, (i+1)*PNT_WIDTH + WIDTH//2 - PNT_WIDTH//2, HEIGHT//2-PNT_WIDTH//2, (i+1)*PNT_WIDTH + WIDTH//2, 0), fill = BOARD_GREY, outline = BLACK)
      drawing.polygon(((i-1)*PNT_WIDTH, HEIGHT, i*PNT_WIDTH - PNT_WIDTH//2, HEIGHT//2+PNT_WIDTH//2, i*PNT_WIDTH, HEIGHT), fill = BOARD_GREY, outline = BLACK)
      drawing.polygon(((i-1)*PNT_WIDTH + WIDTH//2, HEIGHT, i*PNT_WIDTH + WIDTH//2 - PNT_WIDTH//2, HEIGHT//2+PNT_WIDTH//2, i*PNT_WIDTH + WIDTH//2, HEIGHT), fill = BOARD_GREY, outline = BLACK)

  # base rectangle
  drawing.rectangle((0, 0, WIDTH, HEIGHT), outline = BLACK, width = 5)

  # Goal line
  drawing.line((WIDTH - PNT_WIDTH, 0, WIDTH - PNT_WIDTH, HEIGHT), fill = BLACK, width = 5)

  # center lines
  drawing.line((WIDTH//2 - PNT_WIDTH, 0, WIDTH//2 - PNT_WIDTH, HEIGHT), fill = BLACK, width = 5)
  drawing.line((WIDTH//2, 0, WIDTH//2, HEIGHT), fill = BLACK, width = 5)

  # for cube area
  drawing.line((WIDTH - PNT_WIDTH, PNT_WIDTH, WIDTH, PNT_WIDTH), fill = BLACK, width = 5)
  drawing.line((WIDTH - PNT_WIDTH, HEIGHT-PNT_WIDTH, WIDTH, HEIGHT-PNT_WIDTH), fill = BLACK, width = 5)
  drawing.line((WIDTH - PNT_WIDTH, HEIGHT//2, WIDTH, HEIGHT//2), fill = BLACK, width = 5)

  # for center cube
  drawing.line((WIDTH//2-PNT_WIDTH, HEIGHT//2-PNT_WIDTH//2, WIDTH//2, HEIGHT//2-PNT_WIDTH//2), fill = BLACK, width = 5)
  drawing.line((WIDTH//2-PNT_WIDTH, HEIGHT//2+PNT_WIDTH//2, WIDTH//2, HEIGHT//2+PNT_WIDTH//2), fill = BLACK, width = 5)

  return drawing

def print_circle(pos, num, own, im, drawing):
  if pos == 0:
    drawing.ellipse((WIDTH//2-PNT_WIDTH+MARGIN, HEIGHT*3//4-PNT_WIDTH//2+MARGIN, WIDTH//2-MARGIN, HEIGHT*3//4+PNT_WIDTH//2-MARGIN), fill = CH_GRAY, outline = BLACK, width = 3)
    num_im = Image.open(num_image + str(num) + ".png")
    im.paste(num_im, (WIDTH//2-PNT_WIDTH+MARGIN, HEIGHT*3//4-PNT_WIDTH//2+MARGIN), mask = num_im)
  if 0 < pos and pos < 7:
    for i in range(num):
      if i > 4:
        num_im = Image.open(num_image + str(num) + ".png")
        im.paste(num_im, (WIDTH-PNT_WIDTH*(pos+1)+MARGIN, HEIGHT-RADIUS*5), mask = num_im)
        break
      if own == "b":
        drawing.ellipse((WIDTH-PNT_WIDTH*(pos+1)+MARGIN, HEIGHT-RADIUS*(i+1), WIDTH-PNT_WIDTH*pos-MARGIN, HEIGHT-RADIUS*i), fill = WHITE, outline = BLACK, width = 3)
      elif own == "t":
        drawing.ellipse((WIDTH-PNT_WIDTH*(pos+1)+MARGIN, HEIGHT-RADIUS*(i+1), WIDTH-PNT_WIDTH*pos-MARGIN, HEIGHT-RADIUS*i), fill = CH_GRAY, outline = BLACK, width = 3)
      else:
        print("Something wrong!")
        sys.exit()
  elif 7 <= pos and pos < 13:
    for i in range(num):
      if i > 4:
        num_im = Image.open(num_image + str(num) + ".png")
        im.paste(num_im, (WIDTH//2-(pos-5)*PNT_WIDTH+MARGIN, HEIGHT-RADIUS*5), mask = num_im)
        break
      if own == "b":
        drawing.ellipse((WIDTH//2-(pos-5)*PNT_WIDTH+MARGIN, HEIGHT-RADIUS*(i+1), WIDTH//2-(pos-6)*PNT_WIDTH-MARGIN, HEIGHT-RADIUS*i), fill = WHITE, outline = BLACK, width = 3)
      elif own == "t":
        drawing.ellipse((WIDTH//2-(pos-5)*PNT_WIDTH+MARGIN, HEIGHT-RADIUS*(i+1), WIDTH//2-(pos-6)*PNT_WIDTH-MARGIN, HEIGHT-RADIUS*i), fill = CH_GRAY, outline = BLACK, width = 3)
      else:
        print("Something wrong!")
        sys.exit()
  elif 13 <= pos and pos < 19:
    for i in range(num):
      if i > 4:
        num_im = Image.open(num_image + str(num) + ".png")
        im.paste(num_im, ((pos-13)*PNT_WIDTH+MARGIN, RADIUS*4), mask = num_im)
        break
      if own == "b":
        drawing.ellipse(((pos-13)*PNT_WIDTH+MARGIN, RADIUS*i, (pos-12)*PNT_WIDTH-MARGIN, RADIUS*(i+1)), fill = WHITE, outline = BLACK, width = 3)
      elif own == "t":
        drawing.ellipse(((pos-13)*PNT_WIDTH+MARGIN, RADIUS*i, (pos-12)*PNT_WIDTH-MARGIN, RADIUS*(i+1)), fill = CH_GRAY, outline = BLACK, width = 3)
      else:
        print("Something wrong!")
        sys.exit()
  elif 19 <= pos and pos < 25:
    for i in range(num):
      if i > 4:
        num_im = Image.open(num_image + str(num) + ".png")
        im.paste(num_im, (WIDTH//2+(pos-19)*PNT_WIDTH+MARGIN, RADIUS*4), mask = num_im)
        break
      if own == "b":
        drawing.ellipse((WIDTH//2+(pos-19)*PNT_WIDTH+MARGIN, RADIUS*i, WIDTH//2+(pos-18)*PNT_WIDTH-MARGIN, RADIUS*(i+1)), fill = WHITE, outline = BLACK, width = 3)
      elif own == "t":
        drawing.ellipse((WIDTH//2+(pos-19)*PNT_WIDTH+MARGIN, RADIUS*i, WIDTH//2+(pos-18)*PNT_WIDTH-MARGIN, RADIUS*(i+1)), fill = CH_GRAY, outline = BLACK, width = 3)
      else:
        print("Something wrong!")
        sys.exit()
  elif pos == 25:
    drawing.ellipse((WIDTH//2-PNT_WIDTH+MARGIN, HEIGHT//4-PNT_WIDTH//2+MARGIN, WIDTH//2-MARGIN, HEIGHT//4+PNT_WIDTH//2-MARGIN), fill = WHITE, outline = BLACK, width = 3)
    num_im = Image.open(num_image + str(num) + ".png")
    im.paste(num_im, (WIDTH//2-PNT_WIDTH+MARGIN, HEIGHT//4-PNT_WIDTH//2+MARGIN), mask = num_im)
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
        sys.exit()
  if top_num < 0:
    print("Too small checkers for the top-player!")
  elif bottom_num < 0:
    print("Too small checkers for the bottom-player!")
  else:
    if top_num > 0:
      drawing.ellipse((WIDTH-PNT_WIDTH+MARGIN, HEIGHT//4, WIDTH-MARGIN, HEIGHT//4+RADIUS), fill = CH_GRAY, outline = BLACK, width = 3)
      num_im = Image.open(num_image + str(top_num) + ".png")
      im.paste(num_im, (WIDTH-PNT_WIDTH+MARGIN, HEIGHT//4), mask = num_im)
    if bottom_num > 0:
      drawing.ellipse((WIDTH-PNT_WIDTH+MARGIN, HEIGHT//2+PNT_WIDTH+RADIUS, WIDTH-MARGIN, HEIGHT//2+PNT_WIDTH+2*RADIUS), fill = WHITE, outline = BLACK, width = 3)
      num_im = Image.open(num_image + str(bottom_num) + ".png")
      im.paste(num_im, (WIDTH-PNT_WIDTH+MARGIN, HEIGHT//2+PNT_WIDTH+RADIUS), mask = num_im)
  return drawing

def draw_cube(XGID, im, drawing):
  if int(XGID[2]) == 0:
    num_im = Image.open(num_image + "64.png")
    num_im = num_im.rotate(90)
    im.paste(num_im, (WIDTH//2-PNT_WIDTH+MARGIN, HEIGHT//2-PNT_WIDTH//2+MARGIN), mask = num_im)
    return drawing
  elif int(XGID[2]) == 1:
    cube_num = 2**(int(XGID[1]))
    num_im = Image.open(num_image + str(cube_num) + ".png")
    im.paste(num_im, (WIDTH-PNT_WIDTH+MARGIN, HEIGHT-PNT_WIDTH+MARGIN), mask = num_im)
    return drawing
  elif int(XGID[2]) == -1:
    cube_num = 2**(int(XGID[1]))
    num_im = Image.open(num_image + str(cube_num) + ".png")
    num_im = num_im.rotate(180)
    im.paste(num_im, (WIDTH-PNT_WIDTH+MARGIN, MARGIN), mask = num_im)
    return drawing
  else:
    print("Doubling cube Error")
    sys.exit()

def draw_dice(XGID, im, drawing):
  if int(XGID[3]) == 1:
    if XGID[4] == "00":
      return drawing
    dice1 = XGID[4][0]
    dice2 = XGID[4][1]
    if not (0 < int(dice1) and int(dice1) < 7):
      print("Cube1 number Error")
      sys.exit()
    if not (0 < int(dice2) and int(dice2) < 7):
      print("Cube2 number Error")
      sys.exit()
    dice1_im = Image.open(num_image + "dice_" + dice1 + ".png")
    dice2_im = Image.open(num_image + "dice_" + dice2 + ".png")
    drawing.rectangle((WIDTH//2+2*PNT_WIDTH+MARGIN, HEIGHT//2-PNT_WIDTH//2+MARGIN, WIDTH//2+2*PNT_WIDTH+RADIUS+MARGIN, HEIGHT//2-PNT_WIDTH//2+RADIUS+MARGIN), outline = BLACK, width = 5)
    drawing.rectangle((WIDTH//2+3*PNT_WIDTH+MARGIN, HEIGHT//2-PNT_WIDTH//2+MARGIN, WIDTH//2+3*PNT_WIDTH+RADIUS+MARGIN, HEIGHT//2-PNT_WIDTH//2+RADIUS+MARGIN), outline = BLACK, width = 5)
    im.paste(dice1_im, (WIDTH//2+2*PNT_WIDTH+MARGIN, HEIGHT//2-PNT_WIDTH//2+MARGIN), mask = dice1_im)
    im.paste(dice2_im, (WIDTH//2+3*PNT_WIDTH+MARGIN, HEIGHT//2-PNT_WIDTH//2+MARGIN), mask = dice2_im)
    return drawing
  elif int(XGID[3]) == -1:
    if XGID[4] == "00":
      return drawing
    dice1 = XGID[4][0]
    dice2 = XGID[4][1]
    if not (0 < int(dice1) and int(dice1) < 7):
      print("Cube1 number Error")
      sys.exit()
    if not (0 < int(dice2) and int(dice2) < 7):
      print("Cube2 number Error")
      sys.exit()
    dice1_im = Image.open(num_image + "dice_" + dice1 + ".png")
    dice2_im = Image.open(num_image + "dice_" + dice2 + ".png")
    drawing.rectangle((2*PNT_WIDTH+MARGIN, HEIGHT//2-PNT_WIDTH//2+MARGIN, 2*PNT_WIDTH+RADIUS+MARGIN, HEIGHT//2-PNT_WIDTH//2+RADIUS+MARGIN), fill = CH_GRAY, outline = BLACK, width = 5)
    drawing.rectangle((3*PNT_WIDTH+MARGIN, HEIGHT//2-PNT_WIDTH//2+MARGIN, 3*PNT_WIDTH+RADIUS+MARGIN, HEIGHT//2-PNT_WIDTH//2+RADIUS+MARGIN), fill = CH_GRAY, outline = BLACK, width = 5)
    im.paste(dice1_im, (2*PNT_WIDTH+MARGIN, HEIGHT//2-PNT_WIDTH//2+MARGIN), mask = dice1_im)
    im.paste(dice2_im, (3*PNT_WIDTH+MARGIN, HEIGHT//2-PNT_WIDTH//2+MARGIN), mask = dice2_im)
    return drawing
  else:
    print("Turn Error")
    sys.exit()

im = Image.new('RGB',(WIDTH, HEIGHT), WHITE)
draw = ImageDraw.Draw(im)

args = sys.argv

if len(args) != 2:
  print("Must input XGID!")
  sys.exit()

XGID = args[1]

if XGID[0:5] == "XGID=":
  XGID = XGID[5:]

XGID = XGID.split(":")

# checking correct XGID
if len(XGID) != 10:
  print("Incorrect XGID!")
  sys.exit()

draw = draw_base(draw)
draw = draw_pos(XGID, im, draw)
draw = draw_cube(XGID, im, draw)
draw = draw_dice(XGID, im, draw)

im_base = Image.open(num_image + "pos.png")
im_base.paste(im, (0, PNT_WIDTH))

im_base.save("gammon.png", quality = 95)

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
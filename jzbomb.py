'''
jzbomb.py

Takes every image in the folder it's run from and modifies it for continuous reposting
on sites where they compare image data to prevent the image from being posted.

Can only be defeated with AI.

'''
import PIL
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import random

BORDERS = True
WATERMARK = True
WATERMARK = 'sadcode#6826\nselling the set uwu'
FONT = 'C:/Users/Sue/AppData/Local/Microsoft/Windows/Fonts/CATHSGBR.TTF'
FONTSIZE = 120
WM_OPACITY = 255
def read_image(path):
    try:
        image = PIL.Image.open(path)
        return image
    except Exception as e:
        print(e)

destdir = '.'

print("Reading directory...")
files = [ f for f in os.listdir(destdir) if os.path.isfile(os.path.join(destdir,f)) ]

print(str(len(files)) + " images found.")

if not os.path.exists("jzbomb"):
    os.mkdir('jzbomb')
for fname in files:
    print("Altering " + fname)
    img = read_image(fname).convert('RGBA')
    draw = ImageDraw.Draw(img)

    if BORDERS:
        # Draw top border fuzz
        for i in range(0, img.size[0]):
            img.putpixel((i,0), (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))

        # Draw bottom border fuzz
        for i in range(0, img.size[0]):
            img.putpixel((i,img.size[1] - 1), (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))

        # Draw left border fuzz
        for i in range(0, img.size[1]):
            img.putpixel((0,i), (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))

        # Draw right border fuzz
        for i in range(0, img.size[1]):
            img.putpixel((img.size[0]-1,i), (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))

    del draw

    if WATERMARK:
        txt = Image.new('RGBA', img.size, (255,255,255,0))
        fnt = ImageFont.truetype(FONT, FONTSIZE)
        d = ImageDraw.Draw(txt)
        d.text((10,10), WATERMARK, font=fnt, fill=(255,255,255,WM_OPACITY))

        img = Image.alpha_composite(img, txt)

        del d

    # write to stdout
    open('./jzbomb/'+fname, 'w+')
    img.save('./jzbomb/'+fname, "PNG")
    break

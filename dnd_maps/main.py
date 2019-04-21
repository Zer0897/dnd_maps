import tkinter as tk
import numpy as np

from pathlib import Path
from PIL import Image, ImageTk
from enum import Enum
from more_itertools import chunked
from itertools import chain

image_dir = Path(__file__).parent.with_name('res') / 'images'

class ImageDim(Enum):
    castle = 128, 128
    caves = 41, 41
    sample_128 = 128, 128


def getall_images():
    return list(image_dir.rglob('*.png'))


def view(img: Path):
    viewer = ImageViewer(img)
    viewer.mainloop()


def get_square(xfrom, xto, yfrom, yto, data):
    out = []
    for row in data[yfrom:yto]:
        out.append(row[xfrom:xto])
    return out


def main():
    images = {fp.stem: fp for fp in getall_images()}
    fp = images.get('sample_1')
    dim = ImageDim['sample_128']

    #TODO: Border Offset (this area is ignored)
    borders = [0,0,0,0]

    img = Image.open(fp)
    imgdata = chunked(img.getdata(), 128)
    columns = (img.width - borders[0] - borders[1]) / 128
    rows = (img.width - borders[2] - borders[3]) / 128

    data = [col for col in chunked(imgdata, int(columns))]
    square = get_square(0, 128, 0, 128, data)
    square = list(chain(*square))
    # new = Image.fromarray()
    print(bytearray('foo', 'utf-8'))
    # new.show()



    # print(columns, rows)
    # img.show()

    # chunks = chunked(img.getdata(), 128)

'''
o o o o o o
o x x x x x
o x x x x x
o x x x x x
o x x x x x
o x x x x x

'''

'''
Get a square (128x128 segment) at index x
Calculate segment centerpoint
    (technically can be done manually, but dynamic better)
Place overlay.png in center location
Tint overlay graphic (manuall or auto detection)
    grab first row, get RGB value
    tint overlay to match sampled RGB value.
        IMPORTANT!!!! Do not modify alpha value.
repeat for index x+1
'''
#getchannel (setchannel)
#paste
#transform
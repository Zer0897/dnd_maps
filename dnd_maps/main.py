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


def load_image(infilename):
    img = Image.open(infilename)



class Display:

    __slots__ = ('data',)

    def show(self, prcnt=1):
        height = round(self.image.height * prcnt)
        width = round(self.image.width * prcnt)

        image = self.image.resize((width, height), resample=Image.NEAREST)

        image.show()


class Square(Display):
    pass


class Map(Display):

    def __init__(self, fp: Path, dim: ImageDim):
        self.fp = fp
        self.dimensions = dim.value
        self.image = Image.open(self.fp)
        self.data = self.__parse_data()

    def __parse_data(self):
        data = np.asarray(img, dtype="int32", order='F')
        return np.transpose(data, (1,0,2))
        # return np.array(
        #     self.image.getdata()).reshape(self.image.height, self.image.width, 3
        # )

    @property
    def name(self):
        return self.fp.stem



def main():
    maps = {fp.stem: fp for fp in getall_images()}
    fp = maps['sample_1']

    samplemap = Map(fp, ImageDim.sample_128)
    samplemap.show()
    # print(samplemap.show())


    # Image.fromarray(data[0]).show()

    #TODO: Border Offset (this area is ignored)
    # borders = [0,0,0,0]

    # data = load_image(fp)



    # imgdata = chunked(img.getdata(), 128)
    # columns = (img.width - borders[0] - borders[1]) / 128
    # rows = (img.width - borders[2] - borders[3]) / 128

    # data = [col for col in chunked(imgdata, int(columns))]
    # square = get_square(0, 128, 0, 128, data)
    # new = Image.fromarray(, 'RGB')

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
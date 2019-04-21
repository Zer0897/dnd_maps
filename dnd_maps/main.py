import tkinter as tk

from pathlib import Path
from PIL import Image, ImageTk
from enum import Enum
from more_itertools import chunked

image_dir = Path(__file__).parent.with_name('res') / 'images'

class ImageDim(Enum):
    castle = 128, 128
    caves = 41, 41
    sample_128 = 128, 128


class ImageViewer(tk.Tk):

    def __init__(self, img: Image, *args, **kwds):
        super().__init__(*args, **kwds)


        self.img = ImageTk.PhotoImage()
        self.canvas = tk.Canvas(
            self, width=self.img.width(), height=self.img.height()
        )
        self.canvas.pack(fill='both')
        self.after_idle(self.view)

    def view(self):
        self.canvas.create_image(0, 0, anchor='nw', image=self.img)
        self.update()

def getall_images():
    return list(image_dir.rglob('*.png'))


def view(img: Path):
    viewer = ImageViewer(img)
    viewer.mainloop()

def main():
    images = {fp.stem: fp for fp in getall_images()}
    fp = images.get('sample_1')
    dim = ImageDim['sample_128']

    img = Image.open(fp)

    chunks = chunked(img.getdata(), 128)
    chunk = next(chunks)
    ImageViewer(chunk).mainloop()


'''
Get a square (128x128 segment) at index x
Calculate segment centerpoint
    (technically can be done manually, but dynamic better)
Place overlay.png in center location
repeat for index x+1
'''

#
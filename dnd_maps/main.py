import tkinter as tk

from pathlib import Path
from PIL import Image, ImageTk

# Grid Squares are 128x128x

image_dir = Path(__file__).parent.with_name('res') / 'images'


class ImageViewer(tk.Tk):

    def __init__(self, fp: Path, *args, **kwds):
        super().__init__(*args, **kwds)

        self.img = ImageTk.PhotoImage(file=str(fp))
        self.canvas = tk.Canvas(
            self, width=self.img.width(), height=self.img.height()
        )
        self.canvas.pack(fill='both')
        self.after_idle(self.view)

    def view(self):
        self.canvas.create_image(0, 0, anchor='nw', image=self.img)
        self.update()



def getall_images():
    return list(image_dir.iterdir())


def view(img: Path):
    viewer = ImageViewer(img)
    viewer.mainloop()


def main():
    view(getall_images()[0])





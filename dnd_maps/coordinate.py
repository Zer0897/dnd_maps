import numpy as np


class Coordinates:
    def __init__(self, szsurface, sztexture):
        x = np.arange(0, szsurface[0], sztexture[0], dtype=int)
        y = np.arange(0, szsurface[1], sztexture[1], dtype=int)
        self.xv, self.yv = np.meshgrid(x, y, indexing='ij')
        self._coordlocations = CoordLocation(self.xv, self.yv)
        self.num_columns = int(szsurface[0] // sztexture[0])
        self.num_rows = int(szsurface[1] // sztexture[1])

    def __iter__(self):
        return self.filter_output(np.nditer((self.xv, self.yv)))

    def get_positions(self, xfrom, yfrom, xto=None, yto=None):
        return self.filter_output(self._coordlocations.pop(xfrom, yfrom, xto, yto))

    def filter_output(self, coords: iter) -> iter:

        def valid(coord):
            return coord > (-1, -1)

        def clean(coord):
            return int(coord[0]), int(coord[1])

        return map(clean, filter(valid, coords))


class CoordLocation:
    """
    Coordinates are a list of lists
    each list coresponds to an layer of cooridinate axis
    This class defines methods to retrieve the correct
    layer and axis from a given position
    """
    def __init__(self, xcoords, ycoords):
        self.xcoords, self.ycoords = xcoords, ycoords

    def pop(self, xfrom, yfrom, xto=None, yto=None):
        """
        Returns an iterator of all the coordinates within the location specified
        locations are `used`, they can no longer be selected
        """
        xto = xto or xfrom + 1
        yto = yto or yfrom + 1

        xcoords, ycoords = self.xcoords[xfrom:xto], self.ycoords[xfrom:xto]
        # take values from array and replace with invalid values
        # dirty, but this way we don't have to reshape our arrays
        pxcoords = xcoords.take(range(yfrom, yto), axis=1)
        xcoords[:, yfrom:yto] = -1

        pycoords = ycoords.take(range(yfrom, yto), axis=1)
        ycoords[:, yfrom:yto] = -1

        self.xcoords[xfrom:xto], self.ycoords[xfrom:xto] = xcoords, ycoords

        return np.nditer((pxcoords, pycoords))

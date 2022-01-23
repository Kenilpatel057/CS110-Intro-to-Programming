import stddraw
import stdio
import sys


class Point:
    """
    Represents a point in 2-dimensional space.
    """

    def __init__(self, x, y):
        """
        Constructs a new point given its x and y coordinates.
        """

        self._x = x
        self._y = y

    def distanceTo(self, other):
        """
        Returns the Euclidean distance between self and other.
        """

        return ((self._x - other._x) ** 2 + (self._y - other._y) ** 2) ** 0.5

    def draw(self):
        """
        Draws self to standard draw.
        """

        stddraw.point(self._x, self._y)

    def drawTo(self, other):
        """
        Draws line segment between self and other.
        """

        stddraw.line(self._x, self._y, other._x, other._y)

    def __str__(self):
        """
        Returns a string representation of self.
        """

        return '(' + str(self._x) + ', ' + str(self._y) + ')'


# Test client. Creates and uses two Point objects.
def main():
    w = stdio.readInt()
    h = stdio.readInt()
    stddraw.setCanvasSize(w, h)
    stddraw.setXscale(0, w)
    stddraw.setYscale(0, h)
    stddraw.setPenRadius(.005)
    while not stdio.isEmpty():
        x = stdio.readFloat()
        y = stdio.readFloat()
        p = Point(x, y)
        p.draw()
    stddraw.show()

if __name__ == '__main__':
    main()

import stddraw
import stdio
import sys
from point import Point
from tour import Tour


# Reads in points from standard input, runs the nearest neighbor heuristic,
# prints to standard output the distance of the resulting tour along with the
# number of points, and displays the tour on standard draw.
def main():
    w = stdio.readInt()
    h = stdio.readInt()
    stddraw.setCanvasSize(w, h)
    stddraw.setXscale(0, w)
    stddraw.setYscale(0, h)
    stddraw.setPenRadius(.005)
    tour = Tour()
    while not stdio.isEmpty():
        x = stdio.readFloat()
        y = stdio.readFloat()
        p = Point(x, y)
        tour.insertNearest(p)
    stdio.writef('Tour distance = %f\n', tour.distance())
    stdio.writef('Number of points = %d\n', tour.size())
    tour.draw()
    stddraw.show()

if __name__ == '__main__':
    main()

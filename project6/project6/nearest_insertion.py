import stdio
import sys
from point import Point
from tour import Tour


# Reads in points from standard input, runs the nearest neighbor heuristic,
# and prints to standard output the resulting tour along with its distance
# and the number of points.
def main():
    w = stdio.readInt()
    h = stdio.readInt()
    tour = Tour()
    while not stdio.isEmpty():
        x = stdio.readFloat()
        y = stdio.readFloat()
        p = Point(x, y)
        tour.insertNearest(p)
    tour.show()
    stdio.writef('Tour distance = %f\n', tour.distance())
    stdio.writef('Number of points = %d\n', tour.size())

if __name__ == '__main__':
    main()

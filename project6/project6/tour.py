import stdio
from point import Point


class Tour:
    """
    Represents a tour in the traveling salesperson problem.
    """

    def __init__(self):
        """
        Creates an empty tour.
        """

        self._tour = ...

    def show(self):
        """
        Prints the tour to standard output.
        """

        ...

    def draw(self):
        """
        Draws the tour to standard draw.
        """

        ...

    def size(self):
        """
        Returns the number of points on the tour.
        """

        ...

    def distance(self):
        """
        Returns the total distance of the tour.
        """

        ...

    def insertNearest(self, p):
        """
        Inserts the point p using the nearest neighbor heuristic.
        """

        ...

    def insertSmallest(self, p):
        """
        Inserts the point p using the smallest increment heuristic.
        """

        ...

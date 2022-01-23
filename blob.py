class Blob:
    """
    Represents a blob.
    """

    def __init__(self):
        """
        Constructs an empty blob.
        """

        self._P = ...  # number of pixels
        self._x = ...  # x-coordinate of center of mass
        self._y = ...  # y-coordinate of center of mass

    def add(self, i, j):
        """
        Adds pixel (i, j) to this blob.
        """

        ...
        
    def mass(self):
        """
        Returns the number of pixels added to this blob, ie, its mass.
        """

        ...

    def distanceTo(self, other):
        """
        Returns the Euclidean distance between the center of mass of this blob
        and the center of mass of other blob.
        """

        ...

    def __str__(self):
        """
        Returns a string representation of this blob.
        """

        return '%d (%.4f, %.4f)' % (self._P, self._x, self._y)

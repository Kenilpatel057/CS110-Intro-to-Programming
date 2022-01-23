import stdarray
import stdio


# Return a new 2D list representing the transpose of the matrix
# represented by the given 2D list a. Note that the a need not
# have the same number of rows and columns.
def transpose(a):
    # Get the dimensions of matrix a.
    m = ...  # number of rows in a
    n = ...  # number of columns in a

    # Create an n-by-m matrix c with all elements initialized
    # to 0.0.
    ...

    # Fill in the elements of c such that c[i][j] = a[j][i],
    # where 0 <= i < n and 0 <= j < m.
    ...
            
    # Return c.
    ...


# Test client [DO NOT EDIT].
def _main():
    a = stdarray.readFloat2D()
    c = transpose(a)
    for row in c:
        for v in row[:-1]:
            stdio.write(str(v) + ' ')
        stdio.writeln(row[-1])


if __name__ == '__main__':
    _main()

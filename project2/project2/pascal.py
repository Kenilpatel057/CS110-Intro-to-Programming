import stdarray
import stdio
import sys

# Get n from command line, as an int.
n = ...

# Construct a 2D ragged list a of integers. The list must
# have n + 1 rows, with the ith (0 <= i <= n) row a[i] having
# i + 1 elements, each initialized to 1. For example, if n = 3,
# a should be initialized to [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1]].
a = []
for i in range(...):
    a += ...

# Fill the ragged list a using the formula for Pascal's triangle
#     a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
# where 0 <= i <= n and 1 <= j < i.
for i in range(..., ...):
    for j in range(..., ...):
        ...

# Write out the elements of the ragged list a.
for i in range(..., ...):
    for j in range(..., ...):
        # If j is not the last column, write the element with a
        # space after.
        if ...:
            ...
        # Otherwise, write the element with a newline after.
        else:
            ...

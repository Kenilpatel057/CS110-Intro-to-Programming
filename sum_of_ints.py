import stdio
import sys


# Returns the sum S(n) = 1 + 2 + ... + n, computed iteratively.
def sum_iter(n):
    ...

# Returns the sum S(n) = 1 + 2 + ... + n, computed recursively.
def sum_rec(n):
    ...
    

# Test client [DO NOT EDIT]. Reads an integer n from command line and
# writes the sum S(n) = 1 + 2 + ... + n, computed both iteratively and
# recursively.
def _main():
    n = int(sys.argv[1])
    stdio.writeln(sum_iter(n))
    stdio.writeln(sum_rec(n))


if __name__ == '__main__':
    _main()

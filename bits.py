import stdio
import sys


# Return the number of zeros in s, computed recursively.
def zeros(s):
    ...

# Return the number of ones in s, computed recursively.
def ones(s):
    ...
    

# Test client [DO NOT EDIT]. Reads a string s from command line and writes the
# the number of zeros and ones in s, both computed recursively.
def _main():
    s = sys.argv[1]
    stdio.writef('zeros = %d, ones = %d, total = %d\n',
                 zeros(s), ones(s), len(s))


if __name__ == '__main__':
    _main()

import stdio
import sys


# A recursive function that returns True if s is a palindrome, and False
# otherwise.
def is_palindrome(s):
    ...
    

# Test client [DO NOT EDIT]. Read a string s from command line and writes
# whether or not s is a palindrome.
def _main():
    s = sys.argv[1]
    stdio.writeln(is_palindrome(s))


if __name__ == '__main__':
    _main()

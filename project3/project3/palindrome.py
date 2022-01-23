import stdio
import sys


# Return True if s is a palindrome and False otherwise. You may
# assume that s is all lower case and doesn't any whitespace
# characters.
def is_palindrome(s):
    # Iterate over half of the string s.
    for i in range(...):
        # Compare character at i with the character at
        # len(s) - i - 1. If they are different, s is not a
        # palindrome, so return False.
        ...

    # s is a palindrome, so return True.
    ...


# Test client [DO NOT EDIT].
def _main():
    s = sys.argv[1]
    stdio.writeln(is_palindrome(s))


if __name__ == '__main__':
    _main()

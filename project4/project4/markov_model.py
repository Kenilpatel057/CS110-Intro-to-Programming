import stdio
import stdrandom
import sys


class MarkovModel(object):
    """
    Represents a Markov model of order k from a given text string.
    """

    def __init__(self, text, k):
        """
        Create a Markov model of order k from given text (assumed
        to have length at least k).
        """

        ...
        
    def order(self):
        """
        Return order of Markov model.
        """

        ...

    def kgram_freq(self, kgram):
        """
        Return number of occurrences of kgram in text.
        """

        ...
        
    def char_freq(self, kgram, c):
        """
        Return number of times character c follows kgram.
        """

        ...
        
    def rand(self, kgram):
        """
        Return a random character following kgram.
        """

        ...
        
    def gen(self, kgram, T):
        """
        Generate and return a string of length T by simulating a trajectory
        through the correspondng Markov chain. The first k (<= T) characters
        of the generated string is the argument kgram.
        """

        ...
        
    def replace_unknown(self, corrupted):
        """
        Replace unknown characters (~) in corrupted with most probablenb
        characters, and return that string.
        """

        # Return the index of the maximum element in the given list a.
        def argmax(a):
            return a.index(max(a))

        original = ''
        for i in range(len(corrupted)):
            if corrupted[i] == '~':
                ...
            else:
                original += corrupted[i]
        return original


def _main():
    """
    Test client [DO NOT EDIT].
    """

    text, k = sys.argv[1], int(sys.argv[2])
    model = MarkovModel(text, k)
    a = []
    while not stdio.isEmpty():
        kgram = stdio.readString()
        char = stdio.readString()
        a.append((kgram.replace("-", " "), char.replace("-", " ")))
    for kgram, char in a:
        if char == ' ':
            stdio.writef('freq(%s) = %s\n', kgram, model.kgram_freq(kgram))
        else:
            stdio.writef('freq(%s, %s) = %s\n', kgram, char,
                         model.char_freq(kgram, char))


if __name__ == '__main__':
    _main()

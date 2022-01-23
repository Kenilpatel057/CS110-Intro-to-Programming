"""
guitar_string.py

Models a guitar string.
"""

import math
import random
import ring_buffer
import stdarray
import stdio
import sys

# Sampling rate.
SPS = 44100


def create(frequency):
    """
    Create and return a guitar string of the given frequency, using a sampling
    rate given by SPS. A guitar string is represented as a ring buffer of
    of capacity N (SPS divided by frequency, rounded up to the nearest
    integer), with all values initialized to 0.0.
    """

    ...

def create_from_samples(init):
    """
    Create and return a guitar string whose size and initial values are given
    by the list init.
    """

    ...

def pluck(string):
    """
    Pluck the given guitar string by replacing the buffer with white noise.
    """

    ...

def tic(string):
    """
    Advance the simulation one time step on the given guitar string by applying
    the Karplus-Strong update.
    """

    ...

def sample(string):
    """
    Return the current sample from the given guitar string.
    """

    ...


def _main():
    """
    Test client [DO NOT EDIT].
    """

    N = int(sys.argv[1])
    samples = [.2, .4, .5, .3, -.2, .4, .3, .0, -.1, -.3]
    test_string = create_from_samples(samples)
    for t in range(N):
        stdio.writef('%6d %8.4f\n', t, sample(test_string))
        tic(test_string)


if __name__ == '__main__':
    _main()

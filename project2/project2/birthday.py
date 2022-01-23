import random
import stdarray
import stdio
import sys

DAYS_PER_YEAR = 365

# Get trials from command line, as an int.
trials = ...

# Define a variable count denoting the total number of
# individuals sampled across the trials number of experiments,
# and initialize it to 0.
count = ...

# Peform trials number of experiments, where each experiment
# involves sampling individuals until a pair of them share
# a birthday.
for t in range(...):
    # Setup a 1D list birthdays_seen of DAYS_PER_YEAR booleans,
    # all set to False by default. This list will keep track
    # of the birthdays encountered in this experiment.
    birthdays_seen = ...

    # Sample individuals until match.
    while True:
        # Increment count by 1.
        ...

        # Define a variable birthday with a random integer
        # from the interval [0, DAYS_PER_YEAR).
        birthday = ...

        # If birthday has been encountered, abort this experiment.
        if ...:
            ...

        # Record the fact that we are seeing this birthday for
        # the first time.
        else:
            ...

# Write the average number of people that must be sampled before
# a match, as an int.
stdio.writeln(...)

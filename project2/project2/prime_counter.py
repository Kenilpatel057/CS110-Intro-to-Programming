import stdio
import sys

# Get N from command line, as an int.
N = ...

# Define primes to store the result (number of primes <= N).
primes = ...

# Iterate over integers 2 to N (inclusive).
for i in range(..., ...):
    # Define a variable j to store the potential divisors of i,
    # and initialize it to 2.
    ...

    # Repeat as long as j is less than or equal to i / j.
    while ...:
        # If i is divisible by j, it is not a prime so exit
        # (break) this inner loop.
        if ...:
            ...

        # Increment j by 1.
        ...

    # If j is greater than i / j, then i is a prime. So
    # increment primes by one.
    if ...:
        ...

# Write primes.
...

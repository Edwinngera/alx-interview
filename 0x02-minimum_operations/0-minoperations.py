#!/usr/bin/python3
"""
Defines a method that calculates the fewest number of operations needed
to result in exactly n copies of a character in a text file, whose
only operations are Copy All and Paste
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed
    to result in exactly n copies of a character in a text file,
    whose only operations are Copy All and Paste

    parameters:
        n [int]: number of copies of the character desired

    returns:
        the minimum number of operations needed to result in n characters
        or 0 if n is impossible to achieve
    """
    # minOperations will be the sum of all prime factors of n
    # Check if given a valid positive int greater than 1
    if type(n) is not int or n <= 1:
        return 0
    # Start summation list to store divisors
    summation = []
    # start divisors at 2, first prime number
    divisor = 2
    # divide until no longer divisible or dividing by itself
    while (n % divisor) is 0 and (n // divisor) is not 1:
        # each time dividing, add divisor to list to sum later
        summation.append(divisor)
        # update the number to show the division
        n = n // divisor
    # update divisor to 3, next prime number
    divisor = 3
    # keep going until number is less than divisor
    while n > divisor:
        # keep completing divisions with new odd numbers
        while (n % divisor) is 0 and (n // divisor) is not 1:
            summation.append(divisor)
            n = n // divisor
        # move divisor to next odd number
        # not-strictly prime, but later odd numbers are comprised of previous
        divisor += 2
    # add the number itself, last prime number
    summation.append(n)
    # return the sum of all prime factors
    return sum(summation)

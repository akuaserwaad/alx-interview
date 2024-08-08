#!/usr/bin/python3

""" Minimum Operations """

def minOperations(n):
    """
    Given a text file with one 'H', and only "Copy All" and "Paste"
    operations available, write a method to calculate the minimum number
    of operations needed to get exactly `n` 'H' characters.

    Returns the minimum operations as an integer, or 0 if it's impossible.
    """
    if not isinstance(n, int):
        return 0

    op = 0
    i = 2
    while i <= n:
        if n % i == 0:
            n //= i
            op += i
            i = 1
        i += 1
    return op


#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n):
    """
    Given a text file containing a single character 'H', your text editor supports only two operations: "Copy All" and "Paste." 
    Given an integer `n`, write a method to determine the minimum number of operations required to produce exactly `n` 'H' characters in the file.
    - Returns an integer representing the minimum number of operations.
    - If it's not possible to achieve exactly `n` 'H' characters, return 0.
    
    """
    if not isinstance(n, int):
        return 0

    op = 0
    i = 2
    while (i <= n):
        if not (n % i):
            n = int(n / i)
            op += i
            i = 1
        i += 1
    return op

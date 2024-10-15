#!/usr/bin/python3


def minOperations(n):
    """
    Compute the minimum number of operations to reduce a number
    to 1 using only division operations.

    :param n: The number to reduce
    :type n: int
    :return: The minimum number of division operations
    :rtype: int
    """
    if n < 2:
        return 0
    list_factor = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                list_factor.append(i)
    return sum(list_factor)

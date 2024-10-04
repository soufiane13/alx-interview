#!/usr/bin/python3

def pascal_triangle(n):
    """
    This function will generate a Pascal Triangle up to the given number of
    rows. The output will be a list of lists.

    :param n: The number of rows to generate
    :type n: int
    :return: A list of lists representing the Pascal Triangle
    :rtype: list
    """
    k = list()

    if n <= 0:
        return k

    if n > 0:
        # The first row is always [1]
        k.append([1])

    if n > 1:
        # The second row is always [1, 1]
        k.append([1, 1])

    for x in range(3, n+1):
        # For each row, we need to create a list of the correct size
        k.append([0] * x)

        # The first and last elements of each row are always 1
        k[x-1][0] = 1
        k[x-1][x-1] = 1

        # For each element in the row (except the first and last)
        for y in range(1, x-1):
            # The value is the sum of the two elements directly above it
            k[x-1][y] = k[x-2][y-1] + k[x-2][y]
            k[x-1][y] = \
                k[x-2][y-1] + k[x-2][y]

    return k


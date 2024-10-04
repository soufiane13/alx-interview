#!/usr/bin/python3
"""
Defines function returns a list of lists of integers
representing the Pascal's triangle of n
"""
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n
    :param n: the number of rows of Pascal's triangle
    :type n: int
    :return: a list of lists of integers representing Pascal's triangle of n
    :rtype: list
    """
    if type(n) is not int:
        raise TypeError("the number of rows must be an integer")
    triangle = []
    if n <= 0:
        return triangle
    previous = [1]
    # iterate over the rows of the triangle
    for row_index in range(n):
        rlist = []
        if row_index == 0:
            rlist = [1]
        else:
            for i in range(row_index + 1):
                # iterate over the elements of the current row
                # and calculate the element based on the previous row
                if i == 0:
                    rlist.append(0 + previous[i])
                elif i == (row_index):
                    rlist.append(previous[i - 1] + 0)
                else:
                    rlist.append(previous[i - 1] + previous[i])
        previous = rlist
        triangle.append(rlist)
    return triangle

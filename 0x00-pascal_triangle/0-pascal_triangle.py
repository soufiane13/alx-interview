#!/usr/bin/python3
def pascal_triangle(n):
    """
    This function takes an integer n as input and returns the
    first n lines of Pascal's triangle as a list of lists.
    """
#!/usr/bin/python3
def pascal_triangle(n):
    """
    This function takes an integer n as input and returns the
    first n lines of Pascal's triangle as a list of lists.
    """

    triangle_pascal = []
    if type(n) is not int or n <= 0:
        return triangle_pascal
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle_pascal[i - 1][j - 1] + triangle_pascal[i - 1][j])
        triangle_pascal.append(line)
    return triangle_pascal

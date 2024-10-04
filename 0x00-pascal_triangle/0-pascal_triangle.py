def pascal_triangle(n):
    """
    This function returns a Pascal's triangle of n size.

    Args:
        n (int): The size of the triangle.

    Returns:
        list: A Pascal's triangle of n size.
    """
    # Initialize an empty list
    l = []
    if n <= 0:
        # Return an empty list for n <= 0
        return l
    # Initialize the first row of the triangle
    l = [[1]]
    # Iterate over the rows of the triangle
    for i in range(1, n):
        # Initialize the current row
        temp = [1]
        # Iterate over the elements of the current row
        for j in range(len(l[i - 1]) - 1):
            # Calculate the value of the current element
            curr = l[i - 1]
            temp.append(l[i - 1][j] + l[i - 1][j + 1])
        # Add the last element of the row
        temp.append(1)
        # Add the current row to the triangle
        l.append(temp)
    # Return the triangle
    return k

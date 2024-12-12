#!/usr/bin/python3

"""
This module contains code for solving the "Who is the winner?" problem from
CodeWars. The problem is to write a function that takes two arguments: a number
x and a list of numbers. The function is to determine who wins in a game
between Ben and Maria. Ben wins if the sum of the first x numbers is even.
Maria wins if the sum is odd. The function returns a string indicating who
wins.
"""

def isWinner(x, nums):
    """
    This function takes two arguments, x and nums, and returns a string
    indicating who wins the game between Ben and Maria.

    Parameters:
    x (int): The number of numbers to take from the list.
    nums (list): The list of numbers to take the numbers from.

    Returns:
    str: A string indicating who wins. The string is either "Ben" or "Maria".
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]

    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    This function takes two arguments, ls and x, and removes all multiples of
    x from the list ls.

    Parameters:
    ls (list): The list to remove the numbers from.
    x (int): The number to remove the multiples of.

    Returns:
    None
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break

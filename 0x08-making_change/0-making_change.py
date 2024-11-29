#!/usr/bin/python3

"""
Function to make change for a given total
using the given coins as denominations
"""


def makeChange(coins, total):
    """
    Calculates the minimum number of coins
    needed to make change for a total amount
    given a list of coins as denominations

    Args:
        coins (list): List of denominations
        total (int): Total amount

    Returns:
        int: Minimum number of coins needed
    """
    if total <= 0:
        return 0
    check = 0
    temp = 0
    # Sort the coins in descending order
    coins.sort(reverse=True)
    for i in coins:
        # Add the current coin to the total until
        # we reach the total or exceed it
        while check < total:
            check += i
            temp += 1
        if check == total:
            # If we reach the total, return the current
            # count of coins
            return temp
        # If we exceed the total, subtract the current
        # coin and decrement the count
        check -= i
        temp -= 1
    # If we can't make change for the total, return -1
    return -1

#!/usr/bin/python3

"""
This program determines who wins a game between two players
when the game is played with different numbers of rounds.

The game is played in rounds. In each round, the current player
is given a set of numbers from 1 to the number of rounds.
The player must then cross out the smallest prime number in the set.
The other numbers in the set are then updated to not be divisible
by the smallest prime number.

The player who wins the most rounds is declared the winner of the game.
If both players win the same number of rounds, the game is a draw.
"""


def isWinner(x, nums):
    """
    Determines who wins the game with the given numbers of rounds.

    Parameters
    ----------
    x : int
        The number of rounds in the game.
    nums : list
        A list of integers representing the number of rounds to play.

    Returns
    -------
    str
        The winner of the game as a string.
    """
    mariaWinsCount = 0
    benWinsCount = 0

    for num in nums:
        roundsSet = list(range(1, num + 1))
        primesSet = primes_in_range(1, num)

        if not primesSet:
            benWinsCount += 1
            continue

        isMariaTurns = True

        while(True):
            if not primesSet:
                if isMariaTurns:
                    benWinsCount += 1
                else:
                    mariaWinsCount += 1
                break

            smallestPrime = primesSet.pop(0)
            roundsSet.remove(smallestPrime)

            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]

            isMariaTurns = not isMariaTurns

    if mariaWinsCount > benWinsCount:
        return "Winner: soufiane"

    if mariaWinsCount < benWinsCount:
        return "Winner: hamza"

    return None


def is_prime(n):
    """
    Checks if a number is prime.

    Parameters
    ----------
    n : int
        The number to check.

    Returns
    -------
    bool
        True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """
    Returns a list of prime numbers in the given range.

    Parameters
    ----------
    start : int
        The start of the range.
    end : int
        The end of the range.

    Returns
    -------
    list
        A list of prime numbers in the given range.
    """
    primes = [n for n in range(start, end+1) if is_prime(n)]
    return primes

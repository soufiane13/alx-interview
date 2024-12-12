#!/usr/bin/python3

def isWinner(x, nums):
    """
    Decide who wins the Prime Game.

    The Prime Game is played by two players, Maria and Ben, who take turns
    choosing a number from a list of numbers. The game ends when all numbers
    have been chosen. The player who chose more prime numbers in their list
    wins the game.

    :param x: The number of rounds to play.
    :type x: int
    :param nums: A list of numbers to choose from.
    :type nums: list
    :return: The winner of the game, or None if the game is a draw.
    :rtype: str or None
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    # Find prime numbers up to n using the Sieve of Eratosthenes.
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # Count the number of prime numbers in each list.
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    # Decide the winner.
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'

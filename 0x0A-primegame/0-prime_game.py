#!/usr/bin/python3


def isWinner(x, nums):
    """
    This function takes the number of rounds and a list of numbers as parameters and returns the winner of the game.
    The game is played such that the players take turns to remove numbers from the list if they are prime numbers.
    The player with the most number of primes in the end wins.
    If there is a tie, the function returns None.
    """
    Ben = 0
    Maria = 0

    for round in range(x):
        playing_numbers = [num for num in range(2, nums[round] + 1)]
        # Use the Sieve of Eratosthenes to find the prime numbers
        index = 0
        while (index < len(playing_numbers)):
            current_prime = playing_numbers[index]
            sieve_index = index + current_prime
            while(sieve_index < len(playing_numbers)):
                playing_numbers.pop(sieve_index)
                sieve_index += current_prime - 1
            index += 1

        prime_count = (len(playing_numbers))
        if prime_count and prime_count % 2:
            Maria += 1
        else:
            Ben += 1

    if Ben == Maria:
        return None
    return 'Ben' if Ben > Maria else 'Maria'

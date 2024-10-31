#!/usr/bin/python3
"""UTF-8 validation module.

This module contains a single function `validUTF8` for validating a given
sequence of bytes as a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Validates a given sequence of bytes as a valid UTF-8 encoding.

    The function takes a list of integers as input, where each integer
    represents a byte in the input sequence. The function returns `True` if the
    input sequence is a valid UTF-8 encoding and `False` otherwise.
    :param data: A list of integers representing the input sequence of bytes.
    :type data: list[int]
    :return: `True` if the input sequence is a valid UTF-8 encoding and `False`
             otherwise.
    :rtype: bool
    """

    skip = 0
    n = len(data)
    for i in range(n):
        if skip > 0:
            skip -= 1
            continue

        # Check if the current byte is valid
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return False

        # Check if the current byte is a single-byte character
        if data[i] <= 0x7f:
            skip = 0
        # Check if the current byte is a 2-byte character
        elif data[i] & 0b11111000 == 0b11110000:
            span = 4
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        # Check if the current byte is a 3-byte character
        elif data[i] & 0b11110000 == 0b11100000:
            span = 3
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        # Check if the current byte is a 4-byte character
        elif data[i] & 0b11100000 == 0b11000000:
            span = 2
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        else:
            return False

    return True

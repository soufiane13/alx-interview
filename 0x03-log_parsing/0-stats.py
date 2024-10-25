#!/usr/bin/python3
"""
Task 0. Log parsing
"""

import sys


def printStats(file_size, status):
    """
    Print statistics about the log.

    Args:
        file_size (int): The total size of all files.
        status (dict): A dictionary with the status codes as keys and the number
            of times they appear as values.
    """
    print("File size: {}".format(file_size))
    for key, value in sorted(status.items()):
        if value != 0:
            print("{}: {}".format(key, value))


total_f_size = 0
count = 0
status_possible = {200: 0, 301: 0, 400: 0, 401: 0,
                   403: 0, 404: 0, 405: 0, 500: 0}
try:
    # Iterate over each line in the log file
    for line in sys.stdin:
        args = line.split()

        # Get the status code and file size from the line
        status_code = int(args[-2])
        file_size = int(args[-1])

        # Increment the count for the status code and add the file size to the total
        if status_code in status_possible:
            status_possible[status_code] += 1

        total_f_size += file_size
        count += 1

        # Print the statistics every 10 lines
        if count == 10:
            printStats(total_f_size, status_possible)
            count = 0
    # Print the final statistics
    printStats(total_f_size, status_possible)
except KeyboardInterrupt:
    raise
finally:
    # Print the final statistics if the program is interrupted
    printStats(total_f_size, status_possible)
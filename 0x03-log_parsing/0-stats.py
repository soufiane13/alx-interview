#!/usr/bin/python3
"""
Log parsing script that reads log data from standard input and outputs file size and frequency of status codes.
"""

import sys
import re

def output(log: dict) -> None:
    """
    Prints the current file size and frequency of HTTP status codes.
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code-frequency"]):
        if log["code-frequency"][code]:
            print("{}: {}".format(code, log["code-frequency"][code]))

if __name__ == "__main__":
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)'
    )

    line_count = 0
    log = {}
    log["file_size"] = 0
    log["code-frequency"] = {
        str(code): 0 for code in [
            200, 301, 400, 401, 403, 404, 405, 500
        ]
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if match:
                line_count += 1
                code = match.group(1)
                file_size = int(match.group(2))

                # Update total file size
                log["file_size"] += file_size

                # Increment frequency of status code if it's numeric
                if code.isdecimal():
                    log["code-frequency"][code] += 1

                # Output log information every 10 lines
                if line_count % 10 == 0:
                    output(log)
    finally:
        # Output log information at the end of input
        output(log)


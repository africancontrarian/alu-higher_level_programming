#!/usr/bin/python3
"""Defines a script that reads stdin line by line and computes
metrics from an HTTP access log."""
import sys


def print_stats(total_size, status_codes):
    """Print the total file size and the number of lines seen for
    each status code, in ascending order of status code.

    Args:
        total_size (int): The cumulative sum of all file sizes read
            so far.
        status_codes (dict): Maps each status code seen so far to
            the number of times it has appeared.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    valid_codes = ("200", "301", "400", "401", "403", "404", "405", "500")
    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            line_count += 1

            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            if len(parts) >= 2 and parts[-2] in valid_codes:
                status_codes[parts[-2]] = status_codes.get(
                    parts[-2], 0) + 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

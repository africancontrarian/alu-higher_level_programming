#!/usr/bin/python3
"""Displays the X-Request-Id header value of a URL's response."""
import sys
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))

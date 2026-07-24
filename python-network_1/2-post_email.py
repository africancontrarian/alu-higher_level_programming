#!/usr/bin/python3
"""Sends a POST request with an email parameter and prints the body."""
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen


if __name__ == "__main__":
    data = urlencode({"email": sys.argv[2]}).encode("utf-8")
    with urlopen(Request(sys.argv[1], data=data)) as response:
        print(response.read().decode("utf-8"))

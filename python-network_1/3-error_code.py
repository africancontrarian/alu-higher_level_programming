#!/usr/bin/python3
"""Fetches a URL and prints the status code for an HTTPError."""
import sys
from urllib.error import HTTPError
from urllib.request import urlopen


if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.code))

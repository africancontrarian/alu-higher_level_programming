#!/usr/bin/python3
"""Sends a POST request with an email parameter and prints the body."""
import sys
import requests


if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(response.text)

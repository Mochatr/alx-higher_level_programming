#!/usr/bin/python3
"""
This script takes in a URL,
sends a request to the URL
and displays the value of
the variable X-Request-Id in the response header
"""

import requests
import sys


def search_x_request_id(url):
    """
    Sends a GET request to the specified URL
    and prints the value of the 'X-Requested-Id'
    header variable from the response
    """

    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        search_x_request_id(sys.argv[1])
    else:
        print("Usage: ./5-hbtn_header.py <https://alx-intranet.hbtn.io>")

#!/usr/bin/python3

""" Module """
import urllib.request
import sys


def fetch_x_request_id(url):
    """
    Sends a request to a URL and displays the value
    of the X-Request-Id variable found in the header of the response.
    """
    url = "https://alx-intranet.hbtn.io"

    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader("X-Request-Id")
        print(x_request_id)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        fetch_x_request_id(sys.argv[1])
    else:
        print("Usage: ./script.py <https://alx-intranet.hbtn.io>")

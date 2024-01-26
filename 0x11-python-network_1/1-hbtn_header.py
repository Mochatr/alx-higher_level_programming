#!/usr/bin/python3

""" Module """
import urllib.request


def fetch_x_request_id():
    """
    Sends a request to a URL and displays the value
    of the X-Request-Id variable found in the header of the response.
    """
    url = "https://alx-intranet.hbtn.io"

    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader("X-Request-Id")
        print(x_request_id)


if __name__ == "__main__":
    fetch_x_request_id()

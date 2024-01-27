#!/usr/bin/python3
"""
This script takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""

import requests
import sys


def sendpost_request(url, email):
    """ Sends a POST request """
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        sendpost_request(sys.argv[1], sys.argv[2])
    else:
        print("Usage: ./6-post_email.py <http://0.0.0.0:5000/post_email> <hr@holbertonschool.com>")

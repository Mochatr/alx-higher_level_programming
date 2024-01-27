#!/usr/bin/python3
"""
This script takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))

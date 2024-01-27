#!/usr/bin/python3
"""
This script takes in a URL
sends a request to the URL
and displays the body of the response.
"""

import requests
import sys
from requests.exceptions import HTTPError


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except HTTPError as err:
        print(f"Error code: {response.status_code}")

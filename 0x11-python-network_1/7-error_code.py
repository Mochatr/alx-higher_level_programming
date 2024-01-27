#!/usr/bin/python3
"""
This script takes in a URL 
sends a request to the URL 
and displays the body of the response.
"""

import requests
import sys


def search_url_json(url):
    """
    Searches content from the specified URL
    and attempts to parse and print it as JSON
    """
    response = requests.get(url)
    try:
        json_data = response.json()
        print(json_data)
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        search_url_json(sys.argv[1])
    else:
        print("Usage: ./7-error_code.py <http://0.0.0.0:5000>")

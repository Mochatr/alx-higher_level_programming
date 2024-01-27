#!/usr/bin/python3
"""
This script takes in a URL
sends a request to the URL
and displays the body of the response.
"""

import requests
import sys


def search_user(letter):
    """
    Sends a POST request
    """
    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": letter}
    response = requests.post(url, data=payload)

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'), json_response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)

#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    post_dictionary = {"q": sys.argv[1] if len(sys.argv) > 1 else ""}

    response = requests.post(url, data=post_dictionary)

    try:
        json_response = response.json()
        if json_response = {}:
            print("No result")
        else:
            print("[{}] {}".format(json_response["id"], json_response["name"]))
    except ValueError:
        print("Not a valid JSON")

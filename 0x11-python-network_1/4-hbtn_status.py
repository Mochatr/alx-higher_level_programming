#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
"""

import search_status():
    """ searches the status """

    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
    print("\t- utf8 content:", response.text.encode('utf-8'))


if __name__ == "__main__":
    search_status()

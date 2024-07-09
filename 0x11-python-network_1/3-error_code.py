#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)\
        - We will need to manage urllib.error HTTPError
"""
import sys
import urllib.request as request
from urllib.error import HTTPError

if __name__ == "__main__":
    """
    We will initialize the url values to a variable using the
    sys.argv to pass as a command line arguments
    """
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            r = response.read()
            print(r.decode('utf-8'))
    except HTTPError as e:
        print("Error code: ".format(e.code))

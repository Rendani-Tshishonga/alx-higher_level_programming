#!/usr/bin/python3
"""
Write a python script that takes in a URL, sends a request
to the URL and display the value of the X-Request-Id variable
found in the header of the response
"""
import sys
import urllib.request as request

if __name__ == "__main__":
    url = sys.argv[1]

    with request.urlopen(url) as response:
        r = response.headers.get('X-Request-Id')
        print(r)

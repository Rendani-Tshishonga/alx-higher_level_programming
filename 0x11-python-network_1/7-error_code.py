#!/usr/bin/python3
"""
A python script that trakes in a URL
sends a request to the URL and displays the body of the
response
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv
    r = requests.get(url)
    if r.status_codes >= 400:
        print("Error code: {}".format(r.status_code)
    else:
        print(r.text)

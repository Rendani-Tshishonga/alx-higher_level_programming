#!/usr/bin/python3
"""
Write a python script that takes in a URL and an email
sends a POST request to the passed URL with an email as parameter
and finally displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    r = requests.post(url, data=value)
    print(r.text)


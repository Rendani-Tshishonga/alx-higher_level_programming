#!/usr/bin/python3
"""
A python script that takes your github credentials and uses the GITHUB API to
return the id.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    """
    Many web services require authentication we will use Basic authentication
    to achieve this.
    """
    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get('https://api.github.com/user', auth=basic)
    print(r.json().get('id'))

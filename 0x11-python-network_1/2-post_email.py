#!/usr/bin/python3
"""
A script that takes a URL and an email, sends a POST request to the passed
URL with the eamil as a parameter
"""
import sys
import urllib.request as request
import urllib.parse as parse

if __name__ == "__main__":
    """
    We will initialize the URL value and email values to
    respective variables and encode the data using the ascii code
    to transmit the request to the Server. The encoding is done
    through the urllib.parse library.
    """
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = parse.urlencode(value)
    data = data.encode('ascii')
    """
    We will use the Request object which mimicks the actions
    executed by HTTP servers of sending request and issueing responses from the
    server. We will open the request using the urlopen function to return the bytes response
    of the server.
    """
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        r = response.read()
        print(r.decode('utf-8'))

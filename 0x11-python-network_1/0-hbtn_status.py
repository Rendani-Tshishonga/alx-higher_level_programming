#!/usr/bin/python3
"""
We will develop a script that fetches
a url using the urllib.request packages
"""
import urllib.request as request

if __name__ == "__main__":

    """
    We will use the with statement to return the response of the 
    HTTP server.
    """
    url = 'https://alx-intranet.hbtn.io/status'

    with request.urlopen(url) as response:
        r = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(r)))
        print("\t- content: {}".format(r))
        print("\t- utf8 content: {}".format(r.decode('utf-8')))
        
    

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
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        the_page = response.read()
        print(the_page)
    

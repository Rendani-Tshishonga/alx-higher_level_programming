#!/usr/bin/python3
"""
A python script that takes in a letter and sends a POST request to a url
"""
import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1]
    payload = {"q": letter}

    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(request.get('id'), requests.get('name')))
    except ValueError:
        print("Not a valid JSON")

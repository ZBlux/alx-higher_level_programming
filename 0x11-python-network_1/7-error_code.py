#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and manage errors
"""
import requests
import sys

if __name__ == '__main__':

    a = requests.get(sys.argv[1])

    if a.status_code >= 400:
        print("Error code: {}".format(a.status_code))
    else:
        print(a.text)

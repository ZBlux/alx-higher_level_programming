#!/usr/bin/python3
"""
-Python script that takes in a URL, sends a request to the URL
and manage HTTP Errors
"""
import urllib.request
import sys


if __name__ == "__main__":

    req = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(req) as res:
            request = res.read().decode('utf8')
        print(request)

    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))

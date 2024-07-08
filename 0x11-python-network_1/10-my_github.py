#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == '__main__':

    a = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    json = a.json()
    try:
        print(json['id'])
    except:
        print("None")

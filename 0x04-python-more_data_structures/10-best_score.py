#!/usr/bin/python3

def best_score(a_dictionary):
    x = 0
    greatest_numb = None
    if type(a_dictionary) is dict:
        for (key, value) in a_dictionary.items():
            if value > x:
                x = value
                greatest_numb = key
    return greatest_numb

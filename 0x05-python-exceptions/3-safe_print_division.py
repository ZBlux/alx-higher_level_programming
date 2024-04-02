#!/usr/bin/python3

def safe_print_division(a, b):
    c = None
    try:
        div = a / b
        c = div
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(c))
    return c

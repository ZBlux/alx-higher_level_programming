#!/usr/bin/python3

def no_c(my_string):
    c_string = ""
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        c_string += my_string[i]
    return (c_string)

#!/usr/bin/python3
def magic_string(H=[]):
    H.append("BestSchool")
    return (", ".join(H) if len(H) > 1 else "BestSchool")

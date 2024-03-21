#!/usr/bin/python3
"""A function that adds two integers."""

def add_integer(a, b=98):
    """This function adds two integers"""
    if a is not isinstance(int, float):
        raise TypeError("a must be an integer")
    if b is not isinstance(int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

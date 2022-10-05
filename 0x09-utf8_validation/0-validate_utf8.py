#!/usr/bin/python3
"""
0-validate_utf8 function
"""


def validUTF8(data):
    """
    method that determines if a given data
    set represents a valid UTF-8 encoding
    """
    for element in data:
        if element > 255 or element < 1:
            return False
    return True

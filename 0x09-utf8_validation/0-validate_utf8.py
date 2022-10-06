#!/usr/bin/python3
"""
0-validate_utf8 function
"""


def validUTF8(data: list) -> bool:
    """
    method that determines if a given data
    set represents a valid UTF-8 encoding
    """
    count = 0

    for x in data:

        if 191 >= x >= 128:

            if not count:
                return False

            count -= 1
        else:
            if count:
                return False

            if x < 128:
                continue
            elif x < 224:
                count = 1
            elif x < 240:
                count = 2
            elif x < 248:
                count = 3
            else:
                return False

    return count == 0

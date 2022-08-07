#!/usr/bin/python3
"""Lockboxes Solutions"""


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened
    """
    newlist = []
    n = len(boxes)
    for i in boxes:
        if len(i) == 0 and i is not boxes[n-1]:
            return False
        for j in i:
            newlist.append(j)
    for index, keys in enumerate(boxes):
        if index in newlist or index < n-1:
            return True
        else:
            return False

#!/usr/bin/python3
"""0-lockboces"""
def canUnlockAll(boxes):
    """canUnlockAll"""

    opened = set([0])
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key not in opened and key < len(boxes):
                opened.add(key)
                keys.append(key)
    return len(opened) == len(boxes)

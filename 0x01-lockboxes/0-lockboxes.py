#!/usr/bin/python3
"""
Solution to lockboxes problem

Parameters:
    boxes (list): A list of lists, where each inner list represents the keys inside a lockbox.

Returns:
    bool: True if all of the lockboxes can be opened, False otherwise.
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.

    Algorithm:
        1. Check if the input is valid.
        2. Iterate over all of the keys.
        3. For each key, check if the key is inside any of the lockboxes.
        4. If the key is inside a lockbox, open the lockbox.
        5. If the key is not inside any of the lockboxes, return False.
        6. If the code reaches the end of the loop without returning False, return True.
    """

    # Check if the input is valid.
    if not isinstance(boxes, list):
        return False
    if len(boxes) == 0:
        return False

    # Iterate over all of the keys.
    for k in range(1, len(boxes) - 1):
        # Check if the key is inside any of the lockboxes.
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        # If the key is not inside any of the lockboxes, return False.
        if not boxes_checked:
            return False

    # If the code reaches the end of the loop without returning False, return True.
    return True

#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
    Determines if all the boxes in the given list can be unlocked.

    Args:
        boxes (list): A list of lists representing the lockboxes.
        Each inner list contains the keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    visited = set()
    visited.add(0)
    stack = [0]
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < len(boxes) and key not in visited:
                stack.append(key)
                visited.add(key)
    return len(visited) == len(boxes)

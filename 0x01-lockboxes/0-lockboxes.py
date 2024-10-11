#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    This function will check if all boxes can be open.

    Parameters
    ----------
    boxes : list
        A list of lists where each sublist contains the keys of the boxes that
        can be opened with the key in the current box.

    Returns
    -------
    bool
        True if all boxes can be opened and False otherwise.
    """
    if not isinstance(boxes, list):
        return False
    elif len(boxes) == 0:
        return False

    # Check if all boxes can be open
    for k in range(1, len(boxes) - 1):
        checked_boxes = False
        for idx in range(len(boxes)):
            # Check if the key in the current box is in one of the other boxes
            if k in boxes[idx] and k != idx:
                checked_boxes = True
                break
        # If not, return False
        if not checked_boxes:
            return False

    return True

#!/usr/bin/python3
"""
Module to calculate how much rainwater is retained after it rains.
"""


def rain(walls):
    """
    Calculate how many square units of water will be retained after it rains.

    Arguments:
    walls -- list of non-negative integers representing wall heights

    Returns:
    Integer indicating total amount of rainwater retained.
    """
    if not walls:
        return 0

        left, right = 0, len(walls) - 1
         left_max, right_max = 0, 0
        water = 0

    # Iterate through the walls list until the two pointers meet
    while left < right:
        # If the wall at the left pointer is shorter or equal to the wall at the right pointer
        if walls[left] <= walls[right]:
            # Update the maximum height of walls seen so far from the left
            left_max = max(left_max, walls[left])
            # Add the difference between the maximum height seen so far from the left and the current wall height to the total amount of water trapped
            water += left_max - walls[left]
            # Move the left pointer one step to the right
            left += 1
        else:
            # Update the maximum height of walls seen so far from the right
            right_max = max(right_max, walls[right])
            # Add the difference between the maximum height seen so far from the right and the current wall height to the total amount of water trapped
            water += right_max - walls[right]
            # Move the right pointer one step to the left
            right -= 1

    # Return the total amount of water trapped
    return water
    
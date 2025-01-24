import numpy as np
import random

def is_valid_placement(area, x, y, width, height, seperation=1):
    """Checks if a rectangle can be placed at the given position with separation."""
    x_start, x_end = max(0, x - seperation), min(len(area[0]), x + width + seperation)
    y_start, y_end = max(0, y - seperation), min(len(area), y + height + seperation)

    # Check if the area is free
    for i in range(y_start, y_end):
        for j in range(x_start, x_end):
            if area[i][j]:  # If any part of the area is already used
                return False
    return True
    
    
def optimize_placement(rectangles, bin_width, bin_height):
    """Optimizes rectangle placements in the bin."""
    placements = []
    used_area = np.zeros((bin_height, bin_width), dtype=bool)

    for rect in rectangles:
        placed = False
        while not placed:
            x = random.randint(0, bin_width - rect["width"])
            y = random.randint(0, bin_height - rect["height"])

            if is_valid_placement(used_area, x, y, rect["width"], rect["height"]):
                placements.append({"id": rect["id"], "x": x, "y": y})
                used_area[y : y + rect["height"], x : x + rect["width"]] = True
                placed = True

    return placements


# """Checks if a rectangle can be placed at the given position."""
    # for i in range(y, y + height):
    #     for j in range(x, x + width):
    #         if area[i][j]:
    #             return False
    # return True


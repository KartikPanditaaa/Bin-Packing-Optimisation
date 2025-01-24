def print_rectangle_info(rectangles):
    """Prints information about the rectangles."""
    for rect in rectangles:
        print(f"Rectangle {rect['id']}: {rect['width']}x{rect['height']}")

from optimization import optimize_placement
from visualization import plot_placements
import json
import os


def main():
    # Define bin dimensions
    bin_width, bin_height = 80, 40

    # Define rectangles with constraints
    # rectangles = [
    #     {"id": 1, "width": 10, "height": 5},
    #     {"id": 2, "width": 12, "height": 7},
    #     {"id": 3, "width": 8, "height": 6},
    #     {"id": 4, "width": 9, "height": 6},
    #     {"id": 5, "width": 7, "height": 7},
    #     {"id": 6, "width": 6, "height": 4},
    #     {"id": 7, "width": 5, "height": 5},
    #     {"id": 8, "width": 4, "height": 3},
    #     {"id": 9, "width": 3, "height": 2},
    # ]
    
    with open("input_data.json") as f:
        print("Current working directory:", os.getcwd())
        data = json.load(f)
        rectangles = data["rectangles"]
        constraints = data["constraints"]

    # Optimize placement
    placements = optimize_placement(rectangles, bin_width, bin_height)

    # Visualize the results
    plot_placements(rectangles, placements, bin_width, bin_height)

if __name__ == "__main__":
    main()

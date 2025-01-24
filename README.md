# Rectangle Placement Optimization

## Overview

The Rectangle Placement Optimization project aims to solve the problem of efficiently placing a set of rectangles within a defined bin area. This is a common problem in various fields such as logistics, manufacturing, and computer graphics, where the goal is to maximize space utilization while adhering to specific constraints.

## Problem Statement

Given a set of rectangles, each with defined dimensions, and a bin of fixed width and height, the challenge is to determine the optimal arrangement of these rectangles within the bin. The solution should ensure that:

- Rectangles do not overlap.
- All rectangles fit within the bin dimensions.
- Any additional constraints specified in the input data are respected.

## Solution Approach

The project utilizes an optimization algorithm to determine the best placement of rectangles within the bin. The key components of the solution include:

1. **Input Data**: The rectangles and their constraints are read from a JSON file (`input_data.json`). This file should contain the dimensions of each rectangle and any specific constraints that need to be considered during placement.

2. **Optimization Function**: The `optimize_placement` function is responsible for calculating the optimal arrangement of rectangles. It takes into account the dimensions of the bin and the rectangles, applying the necessary constraints to find a feasible solution.

3. **Visualization**: The results of the optimization are visualized using the `plot_placements` function, which provides a graphical representation of the rectangle placements within the bin.

## Requirements

To run this project, you will need the following Python packages:

- `json`
- `os`
- Any additional libraries required for optimization and visualization (e.g., `matplotlib` for plotting).

You can install the necessary packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. **Prepare Input Data**: Create a JSON file named `input_data.json` in the project directory. The file should have the following structure:

```json
{
    "rectangles": [
        {"id": 1, "width": 10, "height": 5},
        {"id": 2, "width": 12, "height": 7},
        ...
    ],
    "constraints": {
        // Define any constraints here
    }
}
```

2. **Run the Program**: Execute the main script to perform the optimization and visualize the results:

```bash
python src/main.py
```

3. **View Results**: The program will output the current working directory and display the visual representation of the rectangle placements.

## Acknowledgments

- [Optimization Algorithms](https://en.wikipedia.org/wiki/Optimization) - For foundational concepts in optimization.
- [Visualization Libraries](https://matplotlib.org/) - For tools used in visualizing the placements.

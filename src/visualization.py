import matplotlib.pyplot as plt

def plot_placements(rectangles, placements, bin_width, bin_height):
    """Visualizes the placements of rectangles within the bin."""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, bin_width)
    ax.set_ylim(0, bin_height)
    ax.set_title("Rectangle Placements")
    ax.set_xlabel("Width")
    ax.set_ylabel("Height")

    for placement in placements:
        rect = next(r for r in rectangles if r["id"] == placement["id"])
        ax.add_patch(
            plt.Rectangle(
                (placement["x"], placement["y"]),
                rect["width"],
                rect["height"],
                edgecolor="blue",
                facecolor="lightblue",
            )
        )
        ax.text(
            placement["x"] + rect["width"] / 2,
            placement["y"] + rect["height"] / 2,
            str(rect["id"]),
            ha="center",
            va="center",
            fontsize=8,
        )

    plt.gca().invert_yaxis()
    plt.show()

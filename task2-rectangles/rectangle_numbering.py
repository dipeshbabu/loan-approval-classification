import matplotlib.pyplot as plt
import numpy as np


def line_length(line):
    # Calculate the length of a line given its endpoints
    return (
        (line["endpoints"][0][0] - line["endpoints"][1][0]) ** 2
        + (line["endpoints"][0][1] - line["endpoints"][1][1]) ** 2
    ) ** 0.5


def draw_rectangle_with_lines(rectangle_line, title):
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Draw the rectangle
    rectangle_coords = [(0, 0), (0, 5), (10, 5), (10, 0), (0, 0)]
    ax.plot(*zip(*rectangle_coords), marker="o")

    # Draw the line inside the rectangle
    ax.plot(*zip(*rectangle_line["endpoints"]), marker="o")

    # Assign number to the rectangle based on the length of the line inside it
    size = line_length(rectangle_line)
    ax.text(
        rectangle_line["endpoints"][0][0],
        rectangle_line["endpoints"][0][1] - 0.5,
        str(int(size)),
        fontsize=12,
    )

    # Set axis limits and aspect ratio to make the rectangle image straight
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    plt.gca().set_aspect("equal", adjustable="box")

    # Set title
    plt.title(title)

    # Display the plot
    plt.show()


if __name__ == "__main__":
    # Four rectangles with lines of different lengths represented by endpoints (x1, y1) and (x2, y2)
    rectangle1 = {"endpoints": ((2, 1), (5, 1))}
    rectangle2 = {"endpoints": ((2, 1), (7, 1))}
    rectangle3 = {"endpoints": ((2, 1), (9, 1))}
    rectangle4 = {"endpoints": ((0.5, 0.5), (9.5, 0.5))}

    # Draw the rectangles with lines and assign numbers
    draw_rectangle_with_lines(rectangle1, "1")
    draw_rectangle_with_lines(rectangle2, "2")
    draw_rectangle_with_lines(rectangle3, "3")
    draw_rectangle_with_lines(rectangle4, "4")

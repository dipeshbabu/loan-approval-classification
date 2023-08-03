import matplotlib.pyplot as plt
import numpy as np
import matplotlib.transforms as transforms


def line_length(line):
    # Calculate the length of a line given its endpoints
    return (
        (line["endpoints"][0][0] - line["endpoints"][1][0]) ** 2
        + (line["endpoints"][0][1] - line["endpoints"][1][1]) ** 2
    ) ** 0.5


def align_rectangles(rectangle_lines):
    # Calculate the rotation angles for each rectangle
    angles = [
        np.arctan2(
            rectangle_line["endpoints"][1][1] - rectangle_line["endpoints"][0][1],
            rectangle_line["endpoints"][1][0] - rectangle_line["endpoints"][0][0],
        )
        for rectangle_line in rectangle_lines
    ]

    # Get the average angle
    avg_angle = np.mean(angles)

    # Create a transformation to apply the average angle rotation
    rotation_transform = transforms.Affine2D().rotate(avg_angle)  # type: ignore

    # Align and draw the rectangles
    fig, ax = plt.subplots()
    for rectangle_line in rectangle_lines:
        # Rotate the rectangle
        rotated_rectangle = rotation_transform.transform(
            [
                [rectangle_line["endpoints"][0][0], rectangle_line["endpoints"][0][1]],
                [rectangle_line["endpoints"][1][0], rectangle_line["endpoints"][1][1]],
            ]
        )

        # Draw the rectangle
        rectangle_coords = [
            (rotated_rectangle[0][0], rotated_rectangle[0][1]),
            (rotated_rectangle[1][0], rotated_rectangle[1][1]),
            (rotated_rectangle[1][0], 5),
            (rotated_rectangle[0][0], 5),
            (rotated_rectangle[0][0], rotated_rectangle[0][1]),
        ]
        ax.plot(*zip(*rectangle_coords), marker="o")

        # Assign numbers to the rectangles based on the length of lines inside them
        size = line_length(rectangle_line)
        ax.text(
            rotated_rectangle[0][0],
            rotated_rectangle[0][1] - 0.5,
            str(int(size)),
            fontsize=12,
        )

    # Set axis limits and aspect ratio to make the rectangle image straight
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    plt.gca().set_aspect("equal", adjustable="box")

    # Set title
    plt.title("Aligned Rectangles")

    # Display the plot
    plt.show()


if __name__ == "__main__":
    # Four rectangles with lines of different lengths represented by endpoints (x1, y1) and (x2, y2)
    rectangle1 = {"endpoints": ((2, 1), (5, 1))}
    rectangle2 = {"endpoints": ((2, 1), (7, 1))}
    rectangle3 = {"endpoints": ((2, 1), (9, 1))}
    rectangle4 = {"endpoints": ((0.5, 0.5), (9.5, 0.5))}

    # Align the rectangles and draw them
    align_rectangles([rectangle1, rectangle2, rectangle3, rectangle4])

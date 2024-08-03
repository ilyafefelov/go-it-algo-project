import matplotlib.pyplot as plt
import numpy as np

def draw_pythagoras_tree(ax, x, y, length, angle, depth, max_depth):
    """
    Draw a Pythagoras tree fractal on the given axes.
    Parameters:
    - ax (matplotlib.axes.Axes): The axes on which to draw the fractal.
    - x (float): The x-coordinate of the starting point of the tree.
    - y (float): The y-coordinate of the starting point of the tree.
    - length (float): The length of the initial line segment.
    - angle (float): The angle at which the branches diverge from the initial line segment.
    - depth (int): The current depth of recursion.
    - max_depth (int): The maximum depth of recursion.
    Returns:
    None
    """
    if depth > max_depth:
        return
    
    # Calculate new (x, y) coordinates
    x_new = x + length * np.cos(angle)
    y_new = y + length * np.sin(angle)

    # Calculate color based on depth
    color = (depth / max_depth, 0, 1 - depth / max_depth)

    # Draw the line with the calculated color
    ax.plot([x, x_new], [y, y_new], color=color)

    # Recursive calls for left and right branches
    new_length = length * np.sqrt(2) / 2
    draw_pythagoras_tree(ax, x_new, y_new, new_length, angle - np.pi / 4, depth + 1, max_depth)
    draw_pythagoras_tree(ax, x_new, y_new, new_length, angle + np.pi / 4, depth + 1, max_depth)

def plot_pythagoras_tree(levels):
    """
    Plot a Pythagoras tree fractal.
    Parameters:
    levels (int): The number of levels in the fractal.
    Returns:
    None
    """
    fig, ax = plt.subplots()
    ax.axis('off')

    # Initial values for the first call
    draw_pythagoras_tree(ax, 0, 0, 1, np.pi / 2, 0, levels)

    plt.show()

# Example usage:
plot_pythagoras_tree(4)

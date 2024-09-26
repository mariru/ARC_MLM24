import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.colors import Normalize
from param import String

colors = ['#000000', '#4285F4', '#EA4335', '#34A853', '#FBBC04', '#9AA0A6', '#FF4081', '#FF6D00',
               '#A0D7E7', '#A42E51']
cmap = ListedColormap(colors)
norm = Normalize(vmin=0, vmax=9)


def show_colors():
    plt.figure(figsize=(4, 1), dpi=200)
    plt.imshow([list(range(10))], cmap=cmap)
    plt.xticks(list(range(10)))
    plt.yticks([])
    plt.show()


def vis_one_grid(input_grid):
    """
    Visualizes a single grid with color blocks separated by white gridlines.

    Parameters:
    input_grid (list of lists or numpy array): A 2D matrix where values from 0 to 9 represent colors.
    """

    # Convert the matrix to a numpy array if it's not already
    input_grid = np.array(input_grid)

    # Create the plot
    fig, ax = plt.subplots()
    ax.matshow(input_grid, cmap=cmap, norm=norm)

    # Customize grid appearance: white gridlines, with gridlines width and spacing
    ax.set_xticks(np.arange(-0.5, input_grid.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-0.5, input_grid.shape[0], 1), minor=True)
    ax.grid(which="minor", color="white", linestyle='-', linewidth=2)

    # Remove ticks and labels
    ax.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False, right=False, top=False)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Display the color grid
    plt.show()


def vis_two_grid(input_grid, output_grid):
    """
    Visualizes two grids side by side, with labels 'Input' and 'Output' respectively.

    Parameters:
    input_grid (list of lists or numpy array): A 2D matrix for the 'Input' on the left.
    output_grid (list of lists or numpy array): A 2D matrix for the 'Output' on the right.
    """

    # Convert the matrices to numpy arrays if they're not already
    input_grid = np.array(input_grid)
    output_grid = np.array(output_grid)

    # Create the plot with two subplots
    fig, axes = plt.subplots(1, 2)

    # Plot the input matrix
    axes[0].matshow(input_grid, cmap=cmap, norm=norm)
    axes[0].set_title('Input', pad=20)

    # Customize grid appearance: white gridlines, with gridlines width and spacing
    axes[0].set_xticks(np.arange(-0.5, input_grid.shape[1], 1), minor=True)
    axes[0].set_yticks(np.arange(-0.5, input_grid.shape[0], 1), minor=True)
    axes[0].grid(which="minor", color="white", linestyle='-', linewidth=2)

    # Remove ticks and labels for input matrix
    axes[0].tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False, right=False, top=False)
    axes[0].set_xticklabels([])
    axes[0].set_yticklabels([])

    # Plot the output matrix
    axes[1].matshow(output_grid, cmap=cmap, norm=norm)
    axes[1].set_title('Output', pad=20)

    # Customize grid appearance: white gridlines, with gridlines width and spacing
    axes[1].set_xticks(np.arange(-0.5, output_grid.shape[1], 1), minor=True)
    axes[1].set_yticks(np.arange(-0.5, output_grid.shape[0], 1), minor=True)
    axes[1].grid(which="minor", color="white", linestyle='-', linewidth=2)

    # Remove ticks and labels for output matrix
    axes[1].tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False, right=False, top=False)
    axes[1].set_xticklabels([])
    axes[1].set_yticklabels([])

    # Show the side-by-side plot
    plt.tight_layout()
    plt.show()


def vis_com_grid(input_grid, output_grid, true_grid):
    """
    Visualizes three grids: input_grid (upper left), true_grid (upper right),
    and output_grid (bottom center).

    Parameters:
    input_grid (numpy array): A 2D matrix representing the input.
    output_grid (numpy array): A 2D matrix representing the output.
    true_grid (numpy array): A 2D matrix representing the true values.
    """

    # Convert the matrices to numpy arrays if they're not already
    input_grid = np.array(input_grid)
    output_grid = np.array(output_grid)
    true_grid = np.array(true_grid)

    # Create the plot with three subplots arranged in a grid
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    fig.delaxes(axes[1, 1])  # Remove the bottom-right subplot

    # Plot the input matrix (upper left)
    ax_input = axes[0, 0]
    ax_input.matshow(input_grid, cmap=cmap, norm=norm)
    ax_input.set_title('Input', pad=20)

    # Remove ticks and labels for input matrix
    ax_input.set_xticks(np.arange(-0.5, input_grid.shape[1], 1), minor=True)
    ax_input.set_yticks(np.arange(-0.5, input_grid.shape[0], 1), minor=True)
    ax_input.grid(which="minor", color="white", linestyle='-', linewidth=2)
    ax_input.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False, right=False, top=False)
    ax_input.set_xticklabels([])
    ax_input.set_yticklabels([])

    # Plot the true matrix (upper right)
    ax_true = axes[0, 1]
    ax_true.matshow(true_grid, cmap=cmap, norm=norm)
    ax_true.set_title('True', pad=20)

    # Remove ticks and labels for true matrix
    ax_true.set_xticks(np.arange(-0.5, true_grid.shape[1], 1), minor=True)
    ax_true.set_yticks(np.arange(-0.5, true_grid.shape[0], 1), minor=True)
    ax_true.grid(which="minor", color="white", linestyle='-', linewidth=2)
    ax_true.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False, right=False, top=False)
    ax_true.set_xticklabels([])
    ax_true.set_yticklabels([])

    # Plot the output matrix (bottom center)
    ax_output = axes[1, 0]
    ax_output.matshow(output_grid, cmap=cmap, norm=norm)
    ax_output.set_title('Output', pad=20)

    # Remove ticks and labels for output matrix
    ax_output.set_xticks(np.arange(-0.5, output_grid.shape[1], 1), minor=True)
    ax_output.set_yticks(np.arange(-0.5, output_grid.shape[0], 1), minor=True)
    ax_output.grid(which="minor", color="white", linestyle='-', linewidth=2)
    ax_output.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False, right=False, top=False)
    ax_output.set_xticklabels([])
    ax_output.set_yticklabels([])

    # Adjust layout to fit titles and matrices
    plt.tight_layout()
    plt.show()

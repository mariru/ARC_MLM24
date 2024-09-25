import numpy as np


def mat_to_pc(input_matrix):
    """
    Transforms a matrix to a point cloud in the format (i, j, c),
    where i and j are the coordinates of non-black points and c is the color value.

    Parameters:
    input_matrix (numpy array or list of lists): The input matrix where values represent colors.

    Returns:
    point_cloud (list of tuples): A list of points in the format (i, j, c).
    size (int list): The size of the matrix. size[0] is rows and size[1] is columns.
    """
    point_cloud = []
    size = [len(input_matrix), len(input_matrix[0])]

    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[i])):
            if input_matrix[i][j] != 0:
                point_cloud.append((i, j, input_matrix[i][j]))

    # Return the point cloud and its size
    return point_cloud, size


def point_cloud_to_matrix(point_cloud, rows, cols):
    """
    Converts a point cloud back into a matrix.

    Parameters:
    point_cloud (list of tuples): A list of points in the format (i, j, c), where i and j are
                                  the coordinates and c is the color.
    rows (int): The number of rows for the matrix.
    cols (int): The number of columns for the matrix.

    Returns:
    matrix (numpy array): The reconstructed matrix.
    """
    # Initialize a matrix of size (rows, cols) with all values set to 0 (black)
    matrix = np.zeros((rows, cols), dtype=int)

    # Loop through the point cloud and set the corresponding matrix values
    for point in point_cloud:
        i, j, c = point
        matrix[i, j] = c

    return matrix

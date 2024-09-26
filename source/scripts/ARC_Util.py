from source.scripts.DataTransfer import *
from source.scripts.DataVisualization import *
from source.tests.test_data_format import *


class arc_grid:

    def __init__(self, grid:np.array):
        validate_grid(grid)
        self.grid = grid
        self.rows, self.cols = grid.shape
        self.point_cloud = grid_to_point_cloud(grid)

    def get_point_cloud(self):
        return self.point_cloud

    def get_grid(self):
        return self.grid

    def get_size(self):
        return self.rows, self.cols

    def set_grid(self, grid:np.array):
        validate_grid(grid)
        self.grid = grid
        self.rows, self.cols = grid.shape
        self.point_cloud = grid_to_point_cloud(grid)

    def set_point_cloud(self, point_cloud:np.array):
        validate_point_cloud(point_cloud)
        self.point_cloud = point_cloud
        self.grid = point_cloud_to_grid(self.point_cloud)
        self.rows, self.cols = self.grid.shape

    def vis(self):
        vis_one_grid(self.grid)


class arc_grid_set:

    def __init__(self, input_grid:arc_grid, output_grid:arc_grid, true_grid:arc_grid = np.array([[]])):
        self.input_grid = input_grid
        self.output_grid = output_grid
        self.true_grid = true_grid

    def get_input_grid(self):
        return self.input_grid

    def get_output_grid(self):
        return self.output_grid

    def get_true_grid(self):
        return self.true_grid

    def set_input_grid(self, input_grid:arc_grid):
        self.input_grid = input_grid

    def set_output_grid(self, output_grid:arc_grid):
        self.output_grid = output_grid

    def set_true_grid(self, true_grid:arc_grid):
        self.true_grid = true_grid

    def vis_pair(self):
        vis_two_grid(self.input_grid, self.output_grid)

    def vis_sets(self):
        vis_com_grid(self.input_grid, self.output_grid, self.true_grid)



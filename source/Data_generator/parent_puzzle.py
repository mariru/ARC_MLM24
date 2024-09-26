import numpy as np
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(project_root)
from scripts.DataTransfer import *
from scripts.DataVisualization import *


class puzzle():
    '''
    A general class for all the ARC puzzles, modify the input_init and solve function to generate different puzzle grids based on their rules.
    '''
    def __init__(self, input_size = [8,8], puzzle_id = 0) -> None:
        self.puzzle_id = puzzle_id
        self.rule = "Input a sparse matrix, change the pixel colors based on a colormap."
        self.examples = []

    def input_init(self, size):
        x = (np.random.rand(*size) < 0.1)* np.random.randint(1,10,size)
        return x

    def sample(self, matrix_sizes):
        for mat_size in matrix_sizes:
            input = self.input_init(mat_size)
            output = self.solve(input)
            self.examples.append((input, output))
        return self.examples
            
    def solve(self, input):
        return input
    def visualize(self, idx):
        try:
            vis_two_grid(*self.examples[idx])
        except:
            print("out of range")
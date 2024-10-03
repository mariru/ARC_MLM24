import numpy as np
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(project_root)
from source.scripts.DataTransfer import *
from source.scripts.DataVisualization import *


class puzzle():
    '''
    A general class for all the ARC puzzles, modify the input_init and solve function to generate different puzzle grids based on their rules.
    '''
    def __init__(self, input_size = [8,8], puzzle_id = 0) -> None:
        self.puzzle_id = puzzle_id
        self.rule = "Input a sparse matrix, change the pixel colors based on a colormap."
        self.examples = []

    def construct_inputs(self):
        size = np.random.randint(3,10,[2])
        x = (np.random.rand(*size) < 0.1)* np.random.randint(1,10,size)
        return x

    def sample(self, sample_times, is_list = False):
        train_data = []
        for i in range(sample_times):
            input = self.construct_inputs()
            output = self.construct_solutions(input)
            train_data.append({ "input": input if not is_list else input.tolist(), 
                                "output": output if not is_list else output.tolist()})
            self.example=(input, output)
        test_input = self.construct_inputs()
        test_data = [{"input": test_input if not is_list else test_input.tolist()}]
        data_pack = {"test": test_data, "train": train_data}
        return data_pack

            
    def construct_solutions(self, input):
        return input
    def visualize(self):
        vis_two_grid(*self.example)
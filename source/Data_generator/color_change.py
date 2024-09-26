import numpy as np
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(project_root)
from scripts.DataTransfer import *
from scripts.DataVisualization import *
from parent_puzzle import puzzle



class color_change_puzzle(puzzle):
    def __init__(self, input_size=[8, 8], puzzle_id=0) -> None:
        super().__init__(input_size, puzzle_id)
        np.random.seed(self.puzzle_id)
        self.color_map = dict(zip(range(1,10), np.random.randint(1,10,[9])))
        np.random.seed(None)
        print(self.color_map)

    def construct_input(self, size):
        x = (np.random.rand(*size) < 0.1)* np.random.randint(1,10,size)
        return x
    
    def construct_solutions(self, input):
        mapping_color = np.vectorize(lambda x: self.color_map[x] if x!=0 else 0)
        output = mapping_color(input)
        return output


if __name__ == '__main__':
    c1_pz = color_change_puzzle(puzzle_id=23)
    grid_examples = c1_pz.sample([[3,4], [5,6], [7,8]])
    for i in range(3):
        c1_pz.visualize(i)

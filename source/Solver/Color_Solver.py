import numpy as np
import sys
import os
project_root_ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(project_root_)

# print("sys path of Solver.py: ",sys.path)

from Solver.Parent_Solver import parent_solver
from scripts.DataTransfer import *
from scripts.DataVisualization import *
from Data_generator.color_change import *
from Data_generator.parent_puzzle import *


class color_change_solver(parent_solver):
    def __init__(self, puzzle_data):
        self.train_data = puzzle_data['train']
        self.test_input = puzzle_data['test'][0]['input']
        # print(self.test_input)
        self.color_map = None
        self.test_solution = None


    def Extract_Cmap(self):
        """
        infer color map
        """
        color_map = {}
        for train_example in self.train_data:
            input_grid = np.array(train_example['input'])
            output_grid = np.array(train_example['output'])
            # print("input grid:", input_grid)
            
            input_colors = input_grid[input_grid != 0]
            output_colors = output_grid[input_grid != 0]
            # print(input_colors)
            # calculate map
            for in_color, out_color in zip(input_colors, output_colors):
                if in_color not in color_map:
                    color_map[in_color] = out_color

        self.color_map = color_map
        print("Inferred Color Map:", self.color_map)
    

    def Apply_Cmap(self, test_input=None):
        """
        Apply color map on test data to generate solution
        """
        if test_input==None:
            test_input = self.test_input
        test_grid = np.array(test_input)
        mapping_color = np.vectorize(lambda x: self.color_map.get(x, 0))  # default = 0
        output_grid = mapping_color(test_grid)
        return output_grid.tolist()
    

    def Solve(self):
        """
        infer map + apply map
        """
        self.Extract_Cmap()
        self.test_solution = self.Apply_Cmap()



if __name__ == '__main__':
    # sample input
    puzzle_data = {'test': [{'input': [[0, 0, 0], [0, 4, 0], [0, 0, 0], [0, 0, 7], [3, 0, 0], [0, 0, 0], [0, 0, 0]]}], 'train': [{'input': [[0, 0, 0, 0, 0, 0, 0, 0, 0], [9, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 4, 0, 0, 0, 0, 0], [0, 3, 0, 0, 0, 0, 0, 0, 0], [0, 0, 7, 0, 0, 0, 0, 0, 0], [0, 5, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 3, 0, 0, 0, 0, 0]], 'output': [[0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 7, 0, 0, 0, 0, 0], [0, 9, 0, 0, 0, 0, 0, 0, 0], [0, 0, 4, 0, 0, 0, 0, 0, 0], [0, 9, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 9, 0, 0, 0, 0, 0]]}, {'input': [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 4, 0, 0, 9, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]], 'output': [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 7, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]}, {'input': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 8], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 'output': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 7], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]}, {'input': [[0, 9, 0, 0], [2, 8, 0, 0], [0, 0, 0, 0], [5, 0, 5, 0]], 'output': [[0, 2, 0, 0], [7, 7, 0, 0], [0, 0, 0, 0], [9, 0, 9, 0]]}, {'input': [[0, 0, 0, 0, 0, 3, 0, 0, 0], [0, 0, 0, 0, 0, 0, 9, 0, 0], [0, 0, 0, 0, 6, 0, 0, 0, 0]], 'output': [[0, 0, 0, 0, 0, 9, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 8, 0, 0, 0, 0]]}, {'input': [[0, 0, 0, 4], [6, 0, 0, 0], [0, 0, 0, 0], [3, 0, 0, 0], [0, 0, 0, 0], [6, 0, 0, 0], [1, 0, 0, 0], [9, 0, 0, 0]], 'output': [[0, 0, 0, 7], [8, 0, 0, 0], [0, 0, 0, 0], [9, 0, 0, 0], [0, 0, 0, 0], [8, 0, 0, 0], [4, 0, 0, 0], [2, 0, 0, 0]]}, {'input': [[0, 0, 0, 0, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 'output': [[0, 0, 0, 0, 7], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]}]}

    solver_1 = color_change_solver(puzzle_data)
    solver_1.Solve()

    print("Test Solutions:", solver_1.Get_Solution())

    # print("Test Solutions:", solver_1.Get_Solution_in_dictionary())
    # print("Test Solutions:", solver_1.Get_Solution_in_numpy())

    solver_1.test_visualize()

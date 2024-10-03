import numpy as np
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(project_root)
from scripts.DataTransfer import *
from scripts.DataVisualization import *


class parent_solver():
    def __init__(self, puzzle_data):
        self.train_data = puzzle_data['train']
        self.test_input = puzzle_data['test'][0]['input']
        self.rule = None
        self.test_solution = None

    def Rule_Extract(self):
        return self.rule

    def Apply_Rule(self):
        return self.test_solution

    def Solve(self):
        self.Rule_Extract()
        self.Apply_Rule()


    def Get_Solution(self):
        return self.test_solution
    
    def Get_Solution_in_dictionary(self):
        return {'test': [{'output': self.test_solution}]}
    
    def Get_Solution_in_numpy(self):
        return np.array(self.test_solution)
    

    def test_visualize(self):
        vis_two_grid(self.test_input, self.test_solution)

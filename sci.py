from source.Solver.Color_Solver import *


if __name__ == '__main__':
    c1_pz = color_change_puzzle(puzzle_id=23)
    grid_examples = c1_pz.sample(7,True)
    print(grid_examples)
    c1_pz.visualize()
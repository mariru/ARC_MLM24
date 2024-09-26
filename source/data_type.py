import numpy as np

class arc_grid():
    def __init__(self, init_array = np.zeros([3,3]) ) -> None:
        self.array = init_array
        self.h, self.w = self.array.shape
from DATASET.pre_process import *

data, diff = process_data()

def make_grid(length):
    grid = []
    for i in range(length):
        for j in range(length):
            grid.append(["."])

print(make_grid(3))
        

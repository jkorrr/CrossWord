# from BACKEND.pre_process import *
import random
# data, diff = process_data()

def make_grid(length):
    grid = []
    for i in range(length):
        row = []
        for j in range(length):
            row.append(["w"])
        grid.append(row)
    return grid

def rotate_180(grid):
    n = len(grid)
    rotated_grid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_grid[i][j] = grid[n - i - 1][n - j - 1]
    return rotated_grid

def generate_pattern(grid):
    n = len(grid) // 2
    for _ in range(3):
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)
        for i in range(x):
            for j in range(y):
                grid[i][j] = "BLANK"  
    
    temp_grid = rotate_180(grid)
    
    for _ in range(3):
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)
        for i in range(x):
            for j in range(y):
                temp_grid[i][j] = "BLANK" 
    grid = rotate_180(grid)

    return grid

grid = make_grid(10)
print(generate_pattern(grid))






        

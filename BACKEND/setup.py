import random
from CLASSES.Reflections import Reflection
import numpy as np

def make_grid(length):
    grid = []
    for _ in range(length):
        row = []
        for _ in range(length):
            row.append("")
        grid.append(row)
    return grid

def generate_pattern(grid):
    n = len(grid) // 2
    p = random.randint(0, 4)
    for _ in range(p):
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)
        for i in range(x):
            for j in range(y):
                grid[i][j] = "BLANK"
    
    temp_grid = Reflection.rotate_180(grid)
    
    for _ in range(p):
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)
        for i in range(x):
            for j in range(y):
                temp_grid[i][j] = "BLANK"
    grid = Reflection.rotate_180(temp_grid)
    return grid

def find_longest_empty_length(grid):
    grid_t = np.transpose(grid)

    def find_empty_row(grid):
        curr_len = 0
        all_empty_indices = []
        max_row_lens = []
        i = 0
        j = 0
        for row in grid:
            x = []
            for cell in row:
                if cell == "":
                    curr_len += 1
                    x.append([i, j])
                else:
                    curr_len = 0
                j += 1
            max_row_lens.append(curr_len)
            all_empty_indices.append(x)
            curr_len = 0
            i += 1
            j = 0
        
        max_row_len = max(max_row_lens)
        row_idx = max_row_lens.index(max_row_len)
        indices = all_empty_indices[row_idx]

        return max_row_len, row_idx, indices
    
    def find_empty_col(grid_t):
        max_col_len, col_idx, indices = find_empty_row(grid_t)
        for idx in indices:
            idx = np.flip(idx)

        return max_col_len, col_idx, indices    

    max_row_len, row_idx, indices = find_empty_row(grid)
    max_col_len, col_idx, indices = find_empty_col(grid_t)
    
    max_empty = max(max_row_len, max_col_len)
    if max_empty == max_row_len:
        return find_empty_row(grid)
    else:
        return find_empty_col(grid_t)

def find_all_empty_indices(grid):
    indices = []
    i = 0
    j = 0
    for row in grid:
        for cell in row:
            if cell == "":
                indices.append([i, j])
                j += 1
        i += 1
        j = 0
    return indices

# grid = make_grid(10)
# print(generate_pattern(grid))
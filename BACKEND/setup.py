import random
from CLASSES.Reflections import Reflection

def make_grid(length):
    grid = []
    for i in range(length):
        row = []
        for j in range(length):
            row.append(["w"])
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
    grid = Reflection.rotate_180(grid)

    return grid

grid = make_grid(10)
print(generate_pattern(grid))






        

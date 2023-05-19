class Reflection:
    def __init__(self, grid):
        self.grid = grid
    
    def rotate_180(grid):
        n = len(grid)
        rotated_grid = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated_grid[i][j] = grid[n - i - 1][n - j - 1]
        return rotated_grid

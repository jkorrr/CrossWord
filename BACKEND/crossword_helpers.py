import numpy as np
import pandas as pd
from crossword import ALPHABET


def out_of_bounds(grid, row, col):
    g = len(grid) - 1
    if row < 0 or row > g - 1 or col < 0 or col > g - 1:
        return False
    return True

def place_word(grid, word, row, col, direction):
    if direction == 'horizontal':
        for i in range(len(word)):
            if out_of_bounds(grid, row, col) or grid[row][col + i] == 'BLANK':
                raise Exception("Can't place word in this spot")
            grid[row][col + i] = word[i]
    if direction == 'vertical':
        for i in range(len(word)):
            if out_of_bounds(grid, row, col) or grid[row + i][col] == 'BLANK':
                raise Exception("Can't place word in this spot")
            grid[row + i][col] = word[i]

def remove_word(grid, word, row, col, direction):
    if direction == 'horizontal':
        for i in range(len(word)):
            grid[row][col + i] = ""
    if direction == 'vertical':
        for i in range(len(word)):
            grid[row + i][col] = ""

def valid_crossword(grid, dictionary):
    grid_t = np.transpose(grid)
    def find_words(grid):
        words = []
        for row in grid:
            word = ""
            for cell in row:
                if cell in ALPHABET:
                    word += cell
                elif cell == "BLANK":
                    word = ""
            if len(word) > 0:
                words.append(word)
        return words
    
    total_words = find_words(grid) + find_words(grid_t)

    for word in total_words:
        if word not in dictionary:
            return False
    return True 
         
def can_place_word(grid, word, row, col, direction, dictionary):
    if direction == 'horizontal':
        for i in range(len(word)):
            if out_of_bounds(grid, row, col + i) or (grid[row][col + i] != "" and grid[row][col + i] != word[i]) or grid[row][col + i] == "BLANK":
                return False
    if direction == 'vertical':
        for i in range(len(word)):
            if out_of_bounds(grid, row + i, col) or (grid[row + i][col] != "" and grid[row + i][col] != word[i]) or grid[row + i][col] == "BLANK":
                return False
            
    test_grid = place_word(grid, word, row, col, direction)
    if not valid_crossword(test_grid, dictionary):
        return False
    return True
    



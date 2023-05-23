from pre_process import process_data
import random
from setup import *
from CLASSES.Graph import Graph
from CLASSES.Trie import Trie
import numpy as np
import random

ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

n = random.randint(5, 10)

data, diff = process_data()
grid = make_grid(n)
grid = generate_pattern(grid)

# print(np.shape(grid))

root = Trie()
words = list(data.keys())


for word in words:
    if type(word) is str:
        root.insert(word.lower())

def generate_random_letters(length):
    word = []
    while length >= 0:
        i = random.randint(0, 75)
        if i > 25:
            word.append("*")
        else:
            word.append(ALPHABET[i])
        length -= 1
    return word



def make_crossword(grid):
    g = Graph(n)
    # grid_copy = np.copy(grid)

    word_len, idx, indices = find_longest_empty_length(grid)

    random_word = generate_random_letters(word_len)

    potential_words = root.find_words(random_word, word_len)

    if len(potential_words) == 0:
        while len(potential_words) == 0:
            random_word = generate_random_letters(word_len)
            potential_words = root.find_words(random_word, word_len)

    word = random.choice(potential_words)
    i = 0
    print(indices)
    while len(word) != 0:
        x, y = indices[i]
        grid[x][y] = word[0]
        word = word[1:]
        i += 1
    return grid

x = make_crossword(grid)
print(x)
'''
word_len, idx, indices = find_longest_empty_length(grid)
print(word_len)
print(idx)
print(indices)
'''
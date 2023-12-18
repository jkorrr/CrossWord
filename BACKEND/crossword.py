from pre_process import process_data
import random
from setup import *
from CLASSES.Graph import Graph
from CLASSES.Trie import Trie
import numpy as np
import random

ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

VOWELS = ['a', 'e', 'i', 'o', 'u']

n = random.randint(5, 10)

data, diff = process_data()
grid = make_grid(n)
grid = generate_pattern(grid)

root = Trie()
dictionary = list(data.keys())

for word in dictionary:
    if type(word) is str:
        root.insert(word.lower())

def generate_random_letters(length):
    word = []
    while length > 0:
        i = random.randint(0, 75)
        if i > 25:
            word.append("*")
        else:
            word.append(ALPHABET[i])
        length -= 1
    return word

def add_first_word(grid):
    # g = Graph(n)
    word_len, idx, indices = find_longest_empty_length(grid)
    random_word = ['*' for _ in range(word_len)]

    potential_words = root.find_words(random_word, word_len)
    word = random.choice(potential_words)

    for i, (x, y) in enumerate(indices):
        grid[x][y] = word[i]
    return word, grid

def check_valid_word(grid, indices):
    word = ""
    for x, y in indices:
        word += grid[x][y]
    if word in dictionary:
        return True
    return False




    



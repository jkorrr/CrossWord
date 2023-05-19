from pre_process import process_data
import random
from setup import make_grid, generate_pattern
from CLASSES.Graph import Graph
from CLASSES.Trie import Trie

n = random.randint(5, 10)

data, diff = process_data()
grid = make_grid(n)
grid = generate_pattern(grid)

root = Trie()
words = list(data.keys())


for word in words:
    if type(word) is str:
        root.insert(word)

print(root.print_trie())
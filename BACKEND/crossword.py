from BACKEND.pre_process import process_data
import random
from BACKEND.setup import make_grid, generate_pattern
from CLASSES.Graph import Graph
from CLASSES.Trie import Trie

n = random.randint(0, 10)

data, diff = process_data()
grid = make_grid(n)
grid = generate_pattern(grid)

root = Trie()
for word in data.values():
    root.insert(word)

print(root)
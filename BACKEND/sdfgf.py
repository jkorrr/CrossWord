import random

class CrosswordGenerator:
    def __init__(self, size):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.words = []

    def generate(self):
        self.words = self.get_words_from_dictionary()
        self.words.sort(key=lambda word: -len(word))
        self.place_word(self.words[0], (0, 0), (1, 0))
        self.fill_grid()

    def get_words_from_dictionary(self):
        # Replace this with your own method to retrieve words from a dictionary
        # or use a pre-defined word list
        return ['example', 'crossword', 'grid', 'puzzle', 'words']

    def place_word(self, word, start, direction):
        x, y = start
        dx, dy = direction

        for letter in word:
            self.grid[x][y] = letter
            x += dx
            y += dy

    def fill_grid(self):
        for word in self.words[1:]:
            intersections = self.find_intersections(word)
            random.shuffle(intersections)

            for intersection in intersections:
                if self.try_place_word(word, intersection):
                    break

    def try_place_word(self, word, intersection):
        x, y, dx, dy = intersection
        x -= dx
        y -= dy

        if self.can_place_word(word, (x, y), (dx, dy)):
            self.place_word(word, (x, y), (dx, dy))
            return True

        return False

    def can_place_word(self, word, start, direction):
        x, y = start
        dx, dy = direction

        for letter in word:
            if not (0 <= x < self.size and 0 <= y < self.size) or self.grid[x][y] != ' ':
                return False

            x += dx
            y += dy

        return True

    def find_intersections(self, word):
        intersections = []

        for x in range(self.size):
            for y in range(self.size):
                if self.grid[x][y] == ' ':
                    if self.can_place_word(word, (x, y), (1, 0)):
                        intersections.append((x, y, 1, 0))
                    if self.can_place_word(word, (x, y), (0, 1)):
                        intersections.append((x, y, 0, 1))

        return intersections

    def print_grid(self):
        for row in self.grid:
            print(' '.join(row))

    def print_clues(self):
        across_clues = {}
        down_clues = {}
        current_word_id = 1

        for x in range(self.size):
            for y in range(self.size):
                if self.grid[x][y] != ' ':
                    if (x == 0 or self.grid[x-1][y] == ' ') and (x < self.size-1 and self.grid[x+1][y] != ' '):
                        down_clue = self.get_word_down((x, y))
                        down_clues[current_word_id] = down_clue
                        current_word_id += 1

                    if (y == 0 or self.grid[x][y-1] == ' ') and (y < self.size-1 and self.grid[x][y+1] != ' '):
                        across_clue = self.get_word_across((x, y))
                        across_clues[current_word_id] = across_clue
                        current_word_id += 1

        print("Across Clues:")
        for num, clue in across_clues.items():
            print(f"{num}. {clue}")

        print("\nDown Clues:")
        for num, clue in down_clues.items():
            print(f"{num}. {clue}")

    def get_word_across(self, start):
        x, y = start
        word = ""
        while x < self.size and self.grid[x][y] != ' ':
            word += self.grid[x][y]
            x += 1
        return word

    def get_word_down(self, start):
        x, y = start
        word = ""
        while y < self.size and self.grid[x][y] != ' ':
            word += self.grid[x][y]
            y += 1
        return word

# Generate a 15x15 blank crossword grid with symmetric black cells
grid_size = 15
crossword_generator = CrosswordGenerator(grid_size)
crossword_generator.generate()
crossword_generator.print_grid()

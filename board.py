DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0),
              (1, 1), (1, -1), (-1, 1), (-1, -1)]


class Board(object):
    def __init__(self):
        self.set_layout([])

    def set_layout(self, layout):
        # Convert all cells to uppercase to ensure case insensitivity
        self.layout = [[cell.upper() for cell in line] for line in layout]

    def _line_search(self, word, x, y, direction):
        '''Determine if a word is found in a grid starting at location in a
         given direction'''
        for char in word:
            if (x < 0 or y < 0 or x == len(self.layout)
               or y == len(self.layout)):
                return False
            if char != self.layout[y][x]:
                return False
            x += direction[0]
            y += direction[1]
        return True

    def _search(self, word):
        # Return True if a word is in board, False if not.
        found = False
        word = word.upper()

        for y, line in enumerate(self.layout):
            for x, char in enumerate(line):
                if word[0] == char:
                    if any([self._line_search(word, x, y, direction)
                           for direction in DIRECTIONS]):
                        found = True
        return found

    def find_words(self, words):
        return [word for word in words if self._search(word)]

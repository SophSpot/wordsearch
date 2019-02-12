import unittest
from board import Board


class TestBoard(unittest.TestCase):

    def setUp(self):
        test_board = [['a', 'b', 'c'],
                      ['d', 'e', 'f'],
                      ['g', 'h', 'i']]
        self.board = Board()
        self.board.set_layout(test_board)

    def test_horizontal(self):
        self.assertEqual(self.board.find_words(['abc', 'fed', 'hi',
                                                'i', 'abf']),
                         ['abc', 'fed', 'hi', 'i'])

    def test_vertical(self):
        self.assertEqual(self.board.find_words(['adg', 'heb', 'if',
                                               'f', 'ifb']),
                         ['adg', 'heb', 'if', 'f'])

    def test_diagonal(self):
        self.assertEqual(self.board.find_words(['aei', 'fb', 'dhi']),
                         ['aei', 'fb'])


if __name__ == '__main__':
    unittest.main()

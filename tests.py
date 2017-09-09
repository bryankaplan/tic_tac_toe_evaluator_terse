#!/usr/bin/env python3

import unittest
from solution import e as examine

X = 'X'
O = 'O'
_ = ' '

# Each test asserts against a tuple of (boolean X won, boolean O won).
NO_WIN = (False, False)
X_WINS = (True, False)
O_WINS = (False, True)
BOTH_WIN = (True, True)

class TestCase(unittest.TestCase):

    def test_no_wins_2x2(self):

        boards = ((_,_,
                   _,_),

                  (O,X,
                   _,_))

        for board in boards:
            self.assertEqual(examine(board), NO_WIN)

    def test_no_wins_3x3(self):

        boards = ((O,X,O,
                   X,_,X,
                   O,X,O),

                  (X,X,_,
                   X,_,O,
                   _,O,O))

        for board in boards:
            self.assertEqual(examine(board), NO_WIN)

    def test_no_wins_4x4(self):

        boards = ((X,X,_,X,
                   X,_,O,O,
                   O,X,O,_,
                   X,_,O,O),

                  (X,X,_,X,
                   X,_,O,O,
                   O,X,O,_,
                   X,_,O,O))

        for board in boards:
            self.assertEqual(examine(board), NO_WIN)

    def test_no_wins_5x5(self):

        boards = ((X,X,_,_,X,
                   X,X,_,_,_,
                   X,X,O,O,O,
                   X,X,O,O,O,
                   _,_,O,O,O),

                  (X,O,O,_,_,
                   X,X,O,O,_,
                   _,X,X,O,O,
                   _,_,X,X,O,
                   _,_,_,X,O))

        for board in boards:
            self.assertEqual(examine(board), NO_WIN)

    def test_horizontal_x_wins_2x2(self):

        boards = ((X,X,
                   O,_),

                  (O,_,
                   X,X))

        for board in boards:
            self.assertEqual(examine(board), X_WINS)

    def test_horizontal_o_wins_2x2(self):

        boards = ((O,O,
                   X,_),

                  (_,X,
                   O,O))

        for board in boards:
            self.assertEqual(examine(board), O_WINS)

    def test_horizontal_both_win_2x2(self):

        boards = ((X,X,
                   O,O),

                  (O,O,
                   X,X))

        for board in boards:
            self.assertEqual(examine(board), BOTH_WIN)

    def test_horizontal_x_wins_3x3(self):

        boards = ((X,X,X,
                   _,O,_,
                   _,O,O),

                  (O,_,O,
                   X,X,X,
                   O,_,_),

                  (_,O,O,
                   _,_,O,
                   X,X,X))

        for board in boards:
            self.assertEqual(examine(board), X_WINS)

    def test_horizontal_o_wins_3x3(self):

        boards = ((O,O,O,
                   X,_,X,
                   _,X,_),

                  (_,X,_,
                   O,O,O,
                   X,X,_),

                  (_,X,_,
                   _,X,X,
                   O,O,O))

        for board in boards:
            self.assertEqual(examine(board), O_WINS)

    def test_horizontal_both_win_3x3(self):

        boards = ((O,O,O,
                   X,X,X,
                   _,_,_),

                  (X,X,X,
                   O,O,O,
                   _,_,_),

                  (X,X,X,
                   O,O,O,
                   X,X,X))

        for board in boards:
            self.assertEqual(examine(board), BOTH_WIN)

    def test_horizontal_x_wins_4x4(self):

        boards = ((X,X,X,X,
                   _,O,O,_,
                   _,O,O,_,
                   _,_,_,_),

                  (O,_,_,O,
                   X,X,X,X,
                   _,O,O,_,
                   _,_,_,_),

                  (_,_,_,_,
                   _,O,O,_,
                   X,X,X,X,
                   _,O,O,_),

                  (_,_,_,_,
                   _,O,O,_,
                   _,O,O,_,
                   X,X,X,X))

        for board in boards:
            self.assertEqual(examine(board), X_WINS)

    def test_horizontal_o_wins_4x4(self):

        boards = ((O,O,O,O,
                   _,_,_,_,
                   X,_,_,X,
                   _,X,X,_),

                  (X,_,_,X,
                   O,O,O,O,
                   X,O,O,X,
                   _,X,X,_),

                  (X,_,_,X,
                   O,_,_,O,
                   O,O,O,O,
                   _,X,X,_),

                  (X,_,_,X,
                   _,_,_,_,
                   X,_,_,X,
                   O,O,O,O))

        for board in boards:
            self.assertEqual(examine(board), O_WINS)

    def test_horizontal_both_win_4x4(self):

        boards = ((X,X,X,X,
                   O,O,O,O,
                   X,_,X,_,
                   O,_,O,_),

                  (O,O,O,O,
                   X,X,X,X,
                   _,_,O,O,
                   _,_,X,X),

                  (_,_,_,_,
                   O,O,O,O,
                   X,X,X,X,
                   _,_,_,_),

                  (_,_,_,_,
                   O,O,O,O,
                   O,O,O,O,
                   X,X,X,X))

        for board in boards:
            self.assertEqual(examine(board), BOTH_WIN)

    def test_horizontal_x_wins_5x5(self):

        boards = ((X,X,X,X,X,
                   O,_,O,_,O,
                   _,_,_,_,_,
                   _,O,_,O,_,
                   _,_,_,_,_),

                  (_,_,_,_,_,
                   X,X,X,X,X,
                   _,_,_,_,_,
                   _,O,_,O,_,
                   _,O,O,O,_),

                  (_,_,O,_,_,
                   _,_,O,_,_,
                   X,X,X,X,X,
                   _,_,O,_,_,
                   _,_,O,O,_),

                  (O,_,O,_,_,
                   _,_,_,O,_,
                   _,O,_,_,O,
                   X,X,X,X,X,
                   _,_,_,_,_),

                  (_,_,O,_,_,
                   _,O,O,O,_,
                   _,_,O,_,_,
                   _,_,_,_,_,
                   X,X,X,X,X))

        for board in boards:
            self.assertEqual(examine(board), X_WINS)

    def test_horizontal_o_wins_5x5(self):

        boards = ((O,O,O,O,O,
                   _,_,_,_,_,
                   _,_,_,_,_,
                   X,X,_,X,X,
                   _,_,_,_,X),

                  (_,X,X,X,_,
                   O,O,O,O,O,
                   _,_,_,_,_,
                   _,_,X,_,_,
                   _,_,X,_,_),

                  (_,_,X,_,_,
                   _,_,X,_,_,
                   O,O,O,O,O,
                   _,_,_,_,_,
                   _,X,X,X,_),

                  (_,_,_,_,_,
                   _,_,X,_,_,
                   X,X,_,X,X,
                   O,O,O,O,O,
                   _,_,_,_,_),

                  (_,_,_,_,_,
                   _,X,_,X,_,
                   _,X,X,X,_,
                   _,_,_,_,_,
                   O,O,O,O,O))

        for board in boards:
            self.assertEqual(examine(board), O_WINS)

    def test_horizontal_both_win_5x5(self):

        boards = ((X,X,X,X,X,
                   O,O,O,O,O,
                   _,_,_,_,_,
                   _,_,_,_,_,
                   _,_,_,_,_),

                  (O,O,O,O,O,
                   X,X,X,X,X,
                   _,_,_,_,_,
                   _,_,_,_,_,
                   _,_,_,_,_),

                  (_,_,_,_,_,
                   _,_,_,_,_,
                   X,X,X,X,X,
                   _,_,_,_,_,
                   O,O,O,O,O),

                  (_,_,_,_,_,
                   O,O,O,O,O,
                   _,_,_,_,_,
                   X,X,X,X,X,
                   _,_,_,_,_),

                  (_,_,_,_,_,
                   _,_,_,_,_,
                   O,O,O,O,O,
                   O,O,O,O,O,
                   X,X,X,X,X))

        for board in boards:
            self.assertEqual(examine(board), BOTH_WIN)

    def test_vertical_x_wins_2x2(self):

        boards = ((X,_,
                   X,O),

                  (O,X,
                   _,X))

        for board in boards:
            self.assertEqual(examine(board), X_WINS)

    def test_vertical_o_wins_2x2(self):

        boards = ((O,_,
                   O,X),

                  (_,O,
                   X,O))

        for board in boards:
            self.assertEqual(examine(board), O_WINS)

    def test_vertical_both_win_2x2(self):

        boards = ((O,X,
                   O,X),

                  (X,O,
                   X,O))

        for board in boards:
            self.assertEqual(examine(board), BOTH_WIN)

    def test_vertical_x_wins_3x3(self):

        boards = ((X,_,O,
                   X,O,_,
                   X,_,O),

                  (_,X,_,
                   O,X,_,
                   O,X,O),

                  (_,_,X,
                   _,O,X,
                   O,O,X))

        for board in boards:
            self.assertEqual(examine(board), X_WINS)

    def test_vertical_o_wins_3x3(self):

        boards = ((O,_,X,
                   O,_,X,
                   O,X,_),

                  (_,O,_,
                   X,O,X,
                   X,O,X),

                  (X,X,O,
                   O,X,O,
                   X,_,O))

        for board in boards:
            self.assertEqual(examine(board), O_WINS)

    def test_vertical_both_win_3x3(self):

        boards = ((X,_,O,
                   X,_,O,
                   X,_,O),

                  (O,X,O,
                   O,X,_,
                   O,X,X))

        for board in boards:
            self.assertEqual(examine(board), BOTH_WIN)

    def test_vertical_x_wins_4x4(self):

        boards = ((X,_,O,_,
                   X,_,_,O,
                   X,_,O,_,
                   X,_,_,O),

                  (_,X,_,O,
                   _,X,_,O,
                   _,X,O,_,
                   _,X,_,O),

                  (_,_,X,_,
                   _,_,X,_,
                   O,O,X,_,
                   O,O,X,_),

                  (_,O,_,X,
                   _,_,O,X,
                   _,O,_,X,
                   O,_,_,X))

        for board in boards:
            self.assertEqual(examine(board), X_WINS)

    def test_vertical_o_wins_4x4(self):

        boards = ((O,X,_,_,
                   O,_,X,_,
                   O,_,_,X,
                   O,_,_,X),

                  (X,O,X,X,
                   _,O,_,_,
                   _,O,_,_,
                   X,O,_,_),

                  (_,_,O,_,
                   _,_,O,_,
                   X,X,O,_,
                   X,X,O,_),

                  (X,_,_,O,
                   X,X,_,O,
                   _,X,_,O,
                   O,X,_,O))

        for board in boards:
            self.assertEqual(examine(board), O_WINS)

    def test_vertical_both_win_4x4(self):

        boards = ((X,O,X,O,
                   X,O,X,O,
                   X,O,X,O,
                   X,O,X,O),

                  (_,X,O,_,
                   _,X,O,_,
                   _,X,O,_,
                   _,X,O,_),

                  (O,_,_,X,
                   O,_,_,X,
                   O,_,_,X,
                   O,_,_,X))

        for board in boards:
            self.assertEqual(examine(board), BOTH_WIN)

    def test_vertical_x_wins_5x5(self):

        boards = ((X,_,_,_,O,
                   X,_,_,O,_,
                   X,_,O,_,_,
                   X,_,_,O,_,
                   X,_,_,_,O),

                  (_,X,_,O,_,
                   _,X,_,O,_,
                   _,X,_,_,O,
                   _,X,_,O,_,
                   _,X,_,O,_),

                  (_,_,X,_,_,
                   O,_,X,_,O,
                   _,O,X,O,_,
                   _,_,X,_,O,
                   _,_,X,_,_),

                  (_,_,_,X,O,
                   _,_,_,X,O,
                   _,O,_,X,_,
                   _,O,_,X,_,
                   _,O,_,X,_),

                  (_,_,_,_,X,
                   _,_,_,_,X,
                   O,_,_,_,X,
                   O,O,_,_,X,
                   O,O,_,_,X))

        for board in boards:
            self.assertEqual(examine(board), X_WINS)

    def test_vertical_o_wins_5x5(self):

        boards = ((O,_,_,_,X,
                   O,_,_,X,_,
                   O,_,X,_,_,
                   O,_,_,X,_,
                   O,_,_,_,X),

                  (_,O,_,_,_,
                   _,O,_,_,X,
                   _,O,X,X,X,
                   _,O,_,_,X,
                   _,O,_,_,_),

                  (_,_,O,_,X,
                   X,_,O,_,_,
                   _,_,O,_,X,
                   X,_,O,_,_,
                   _,_,O,_,X),

                  (X,_,_,O,_,
                   X,_,_,O,_,
                   _,X,_,O,_,
                   _,_,X,O,_,
                   _,_,X,O,_),

                  (_,_,_,_,O,
                   _,_,_,_,O,
                   _,_,X,_,O,
                   _,_,X,_,O,
                   X,X,X,_,O))

        for board in boards:
            self.assertEqual(examine(board), O_WINS)

    def test_vertical_both_win_5x5(self):

        boards = ((X,_,_,_,O,
                   X,_,_,_,O,
                   X,_,_,_,O,
                   X,_,_,_,O,
                   X,_,_,_,O),

                  (X,X,O,O,O,
                   X,X,O,O,O,
                   X,X,X,O,O,
                   X,X,X,O,O,
                   X,X,X,O,O),

                  (O,_,X,_,_,
                   O,_,X,_,_,
                   O,_,X,_,_,
                   O,_,X,_,_,
                   O,_,X,_,_),

                  (_,_,_,X,O,
                   _,_,_,X,O,
                   _,_,_,X,O,
                   _,_,_,X,O,
                   _,_,_,X,O),

                  (_,O,_,_,X,
                   _,O,_,_,X,
                   _,O,_,_,X,
                   _,O,_,_,X,
                   _,O,_,_,X))

        for board in boards:
            self.assertEqual(examine(board), BOTH_WIN)

    def test_diagonal_x_wins_2x2(self):

        boards = ((X,O,
                   _,X),

                  (O,X,
                   X,_))

        for board in boards:
            self.assertEqual(examine(board), X_WINS)

    def test_diagonal_o_wins_2x2(self):

        boards = ((O,X,
                   _,O),

                  (_,O,
                   O,X))

        for board in boards:
            self.assertEqual(examine(board), O_WINS)

    def test_diagonal_both_win_2x2(self):

        boards = ((X,O,
                   O,X),

                  (O,X,
                   X,O))

        for board in boards:
            self.assertEqual(examine(board), BOTH_WIN)

    def test_diagonal_x_wins_3x3(self):

        boards = ((X,O,_,
                   O,X,O,
                   _,_,X),

                  (O,_,X,
                   O,X,_,
                   X,_,X))

        for board in boards:
            self.assertEqual(examine(board), X_WINS)

    def test_diagonal_o_wins_3x3(self):

        boards = ((O,_,_,
                   _,O,X,
                   X,X,O),

                  (X,X,O,
                   _,O,_,
                   O,X,_))

        for board in boards:
            self.assertEqual(examine(board), O_WINS)

    def test_diagonal_both_win_3x3(self):

        boards = ()

        for board in boards:
            self.assertEqual(examine(board), BOTH_WIN)

    def test_diagonal_x_wins_4x4(self):

        boards = ((X,O,O,O,
                   O,X,_,_,
                   _,_,X,_,
                   _,_,_,X),

                  (_,_,O,X,
                   _,_,X,O,
                   _,X,O,X,
                   X,O,O,O))

        for board in boards:
            self.assertEqual(examine(board), X_WINS)

    def test_diagonal_o_wins_4x4(self):

        boards = ((O,_,X,X,
                   _,O,X,X,
                   _,_,O,_,
                   _,_,_,O),

                  (X,_,_,O,
                   X,_,O,_,
                   _,O,_,_,
                   O,_,X,X))

        for board in boards:
            self.assertEqual(examine(board), O_WINS)

    def test_diagonal_both_win_4x4(self):

        boards = ((O,_,_,X,
                   _,O,X,_,
                   _,X,O,_,
                   X,_,_,O),

                  (X,_,_,O,
                   _,X,O,_,
                   _,O,X,_,
                   O,_,_,X))

        for board in boards:
            self.assertEqual(examine(board), BOTH_WIN)

    def test_diagonal_x_wins_5x5(self):

        boards = ((X,_,_,O,_,
                   _,X,_,_,O,
                   _,_,X,_,_,
                   O,_,_,X,_,
                   O,O,_,_,X),

                  (O,O,O,_,X,
                   _,_,_,X,_,
                   _,_,X,_,_,
                   _,X,_,_,_,
                   X,_,O,_,O))

        for board in boards:
            self.assertEqual(examine(board), X_WINS)

    def test_diagonal_o_wins_5x5(self):

        boards = ((O,_,X,_,_,
                   _,O,_,_,_,
                   X,_,O,_,X,
                   _,_,_,O,_,
                   X,_,X,_,O),

                  (_,_,_,_,O,
                   X,X,_,O,_,
                   X,_,O,_,_,
                   _,O,_,_,_,
                   O,_,_,X,X))

        for board in boards:
            self.assertEqual(examine(board), O_WINS)


if __name__ == '__main__':
    unittest.main(verbosity=2)

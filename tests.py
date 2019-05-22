import unittest

import numpy as np

from exceptions import AlreadyBusyException
from main import TicTacToe


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.tic_tac_toe = TicTacToe()

    def test_board_result(self):
        self.assertEqual(self.tic_tac_toe.check_board(), None)
        self.tic_tac_toe.board = np.array([['X', 'X', 'X'], ['_', '_', '_'], ['_', '_', '_']])
        self.assertEqual(self.tic_tac_toe.check_board(), "X")
        self.tic_tac_toe.board = np.array([['O', 'O', 'O'], ['_', '_', '_'], ['_', '_', '_']])
        self.assertEqual(self.tic_tac_toe.check_board(), "O")
        self.tic_tac_toe.board = np.array([['X', '_', '_'], ['_', 'X', '_'], ['_', '_', 'X']])
        self.assertEqual(self.tic_tac_toe.check_board(), "X")
        self.tic_tac_toe.board = np.array([['_', '_', 'O'], ['_', 'O', '_'], ['O', '_', 'X']])
        self.assertEqual(self.tic_tac_toe.check_board(), "O")
        self.tic_tac_toe.board = np.array([['X', 'O', 'X'], ['O', 'O', 'X'], ['O', 'X', 'O']])
        self.tic_tac_toe.free_spots = []
        self.assertEqual(self.tic_tac_toe.check_board(), "DEUCE")

    def test_move_to_busy_place(self):
        self.tic_tac_toe.board = np.array([['X', 'X', 'X'], ['_', '_', '_'], ['_', '_', '_']])
        with self.assertRaises(AlreadyBusyException):
            self.tic_tac_toe.place_piece('O', (0, 0))
            self.tic_tac_toe.place_piece('X', (0, 0))
            return

    def test_choose_wrong_bounds(self):
        self.tic_tac_toe.board = np.array([['X', 'X', 'X'], ['_', '_', '_'], ['_', '_', '_']])
        with self.assertRaises(IndexError):
            self.tic_tac_toe.place_piece('O', (3, 0))
            return

    def tearDown(self):
        del self.tic_tac_toe

import random
from itertools import cycle
from time import sleep

import numpy as np

from exceptions import AlreadyBusyException


class TicTacToe(object):

    def __init__(self):
        self.pieces = ["X", "O"]
        self.starting_piece = ''
        self.player_piece_choice = ''
        self.busy_spots = []
        self.board = np.array([['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']])
        self.free_spots = [(x, y) for x in range(len(self.board)) for y in range(len(self.board))]

    def get_random_empty_place(self):
        """
        :return: a tuple containing an random empty position on the board
        """
        return random.choice(self.free_spots)

    def place_piece(self, piece, position):
        """
        Places a Piece in the board
        :param piece: the piece to put
        :param position: a tuple containing the coordinates of the piece
        :return: nothing
        """
        if position not in self.busy_spots:
            self.board[position[0], position[1]] = piece
            self.busy_spots.append(position)
            self.free_spots.remove(position)
        else:
            raise AlreadyBusyException("That place already got's a piece.")

    @property
    def are_free_spots(self):
        """
        property yo check if there are still free spots on the board
        :return:
        """
        return len(self.free_spots) != 0

    def who_goes_first(self):
        """
        Decides randomly who's the first turn
        :return: 1 for the first player or 2 for the second player
        """
        print("Selecting staring piece...")
        sleep(1)
        self.starting_piece = random.choice("XO")
        print("Staring piece will be {}".format(self.starting_piece))
        self.pieces.insert(0, self.pieces.pop(self.pieces.index(self.starting_piece)))

    def player_move(self):
        """
        This function simulates the piece placement for the player. Asks for coordinates and tries to put
        the piece
        :return: nothing
        """
        while True:
            print("Your turn:")
            try:
                row_coordinate = int(input("Enter a row coordinate to row x of the board: "))
                col_coordinate = int(input("Enter a column coordinate to column x of the board: "))
                self.place_piece(self.player_piece_choice, (row_coordinate, col_coordinate))
                break
            except ValueError:
                print("The value you inserted is not valid. Try again")
            except AlreadyBusyException as e:
                print(e)
            except IndexError:
                print("Incorrect Coordinates. Values must be between 0 and 2")

    def computer_move(self, piece):
        """
        Function to simulate the piece placement of the computer
        :param piece: the piece
        :return: Nothing
        """
        print("Computer turn: ")
        sleep(1)
        empty_place = self.get_random_empty_place()
        self.place_piece(piece, empty_place)

    def print_board(self):
        """
        Just Prints the board
        :return: Nothing
        """
        print(self.board)

    def is_player_turn(self, piece):
        """
        Checks if it is the player turn
        :param piece: the piece turn
        :return: True if it is the player's turn
        """
        return self.player_piece_choice == piece

    def play(self):
        """
        function to play. it will create a cycle that will only finish when there is a winner
        or if there are no more moves and no one won(a deuce)
        :return: Nothing
        """
        while True:
            piece_choice = str(input("Choose your pieces: X or O:"))
            if piece_choice not in ("X", "O"):
                print("wrong choice, try again")
            else:
                break
        self.player_piece_choice = piece_choice
        self.who_goes_first()
        result = None
        try:
            for piece in cycle(self.pieces):
                if self.is_player_turn(piece):
                    self.player_move()
                else:
                    self.computer_move(piece)
                self.print_board()
                result = self.check_board()
                if result:
                    raise StopIteration
        except StopIteration:
            print("END OF THE GAME Result: {} {}".format(result, "Wins !" if result is not "DEUCE" else ""))

    def check_board(self):
        """
        Checks the result of the board
        :return: X if the player X has won, O if the player O has won, DEUCE if no one won and there is no
        more empty places, or None, in case the game should continue.
        """
        cols = [''.join(row) for row in self.board.transpose().tolist()]
        rows = [''.join(row) for row in self.board.tolist()]
        diagonal = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(self.board.tolist())]))
        lines = rows + list(cols) + list(diagonal)
        return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'DEUCE' if not self.are_free_spots else None


def main():
    tic_tac_toe = TicTacToe()
    tic_tac_toe.play()


if __name__ == "__main__":
    main()

from consts import *

# TODO: Add notes to class
class GameField:
    def __init__(self):
        self.board = []
        self.build_empty_board()

    def build_empty_board(self):
        """Building an empty matrix"""
        self.board = [[EMPTY for col in range(COLS_COUNT)] for row in range(ROWS_COUNT)]

    def get_board(self):
        """Returns the board"""
        return self.board

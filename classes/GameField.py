import random

from consts import *


# TODO: Add notes to class
class GameField:
    def __init__(self):
        self.board = []
        self.mines = []
        self.build_empty_board()
        self.insert_flag_position()

    def build_empty_board(self):
        """Building an empty matrix"""
        self.board = [[EMPTY for col in range(COLS_COUNT)] for row in range(ROWS_COUNT)]

    def get_board(self):
        """Returns the board"""
        return self.board

    def insert_mines(self):
        """Inserting mines to the grid"""
        for mine in range(MINE_COUNT):

            valid_mine = False
            while not(valid_mine):
                mine_col_x = random.randint(MIN_X, MAX_X-MINE_WIDTH)
                mine_row_y = random.randint(MIN_Y, MAX_Y - MINE_WIDTH)
                if (SAFE_ZONE_X_START < mine_col_x < SAFE_ZONE_X_END) and (SAFE_ZONE_Y_START < mine_row_y < SAFE_ZONE_Y_END):
                    # The mine is not valid
                    pass
                else:
                    valid_mine = True
                    # TODO: Add mine to screen



    def insert_flag_position(self):
        """Insert the flag position to matrix"""
        # Get the flag position
        flag_start_col_square = FLAG_X // SQUARE_SIZE
        flag_start_row_square = FLAG_Y // SQUARE_SIZE
        flag_end_row_square = flag_start_row_square + FLAG_HEIGHT_SQUARES
        flag_end_col_square = flag_start_col_square + FLAG_WIDTH_SQUARES

        # Update soldier position in matrix
        for row in range(flag_start_row_square, flag_end_row_square):
            for col in range(flag_start_col_square, flag_end_col_square):
                self.board[row][col] = FLAG

    def update_soldier_location(self, soldier):
        """Updates the soldier location in the grid"""
        # Reset the board where soldier
        self.board = [[EMPTY if val == SOLDIER else val for val in subl] for subl in self.board]

        # Get the soldier position
        soldier_start_col_square = soldier.get_x() // SQUARE_SIZE
        soldier_start_row_square = soldier.get_y() // SQUARE_SIZE
        soldier_end_row_square = soldier_start_row_square + SOLDIER_HEIGHT_SQUARES
        soldier_end_col_square = soldier_start_col_square + SOLDIER_WIDTH_SQUARES

        # Update soldier position in matrix
        for row in range(soldier_start_row_square, soldier_end_row_square):
            for col in range(soldier_start_col_square, soldier_end_col_square):
                self.board[row][col] = SOLDIER

        # print('\n'.join(map(''.join, self.board)))
        # print()

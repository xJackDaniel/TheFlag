import random

from consts import *


# TODO: Add notes to class
class GameField:
    def __init__(self):
        self.board = []
        self.mines = []
        self.build_empty_board()
        self.insert_flag_position()
        self.insert_mines()

    def build_empty_board(self):
        """Building an empty matrix"""
        self.board = [[EMPTY for col in range(COLS_COUNT)] for row in range(ROWS_COUNT)]

    def get_board(self):
        """Returns the board"""
        return self.board

    def get_mines(self):
        """Returns the mines"""
        return self.mines

    def insert_mines(self):
        """Inserting mines to the grid"""
        def check_x_safe_zone(x):
            """Returns True/False if x is in the safe zone"""
            return SAFE_ZONE_X_START < x < SAFE_ZONE_X_END

        def check_y_safe_zone(y):
            """Returns True/False if y is in the safe zone"""
            return SAFE_ZONE_Y_START < y < SAFE_ZONE_Y_END

        for mine in range(MINE_COUNT):
            valid_mine = False
            while not valid_mine:
                mine_col_x = random.randrange(MIN_X, MAX_X-MINE_WIDTH, SQUARE_SIZE)
                mine_row_y = random.randrange(MIN_Y, MAX_Y - MINE_HEIGHT, SQUARE_SIZE)
                while check_x_safe_zone(mine_col_x) or check_y_safe_zone(mine_row_y):
                    # The mine is not valid - Check if x or y is not valid
                    if check_x_safe_zone(mine_col_x):
                        mine_col_x = random.randrange(MIN_X, MAX_X - MINE_WIDTH, SQUARE_SIZE)
                    else:
                        mine_row_y = random.randrange(MIN_Y, MAX_Y - MINE_HEIGHT, SQUARE_SIZE)
                else:
                    valid_mine = True
                    # Add mine to screen and to list
                    self.mines.append((mine_col_x, mine_row_y))
                    self.insert_mine_position(mine_col_x, mine_row_y)

    def insert_object(self, start_x, end_x, start_y, end_y, value):
        """Inserts an object to the matrix"""
        for row in range(start_y, end_y):
            for col in range(start_x, end_x):
                self.board[row][col] = value

    def insert_mine_position(self, x, y):
        """Insert the mine position to matrix"""
        # Get the flag position
        mine_start_col_square = x // SQUARE_SIZE
        mine_start_row_square = y // SQUARE_SIZE
        mine_end_row_square = mine_start_row_square + MINE_HEIGHT_SQUARES
        mine_end_col_square = mine_start_col_square + MINE_WIDTH_SQUARES

        # Update mine position in matrix
        self.insert_object(mine_start_col_square, mine_end_col_square, mine_start_row_square, mine_end_row_square, MINE)

    def insert_flag_position(self):
        """Insert the flag position to matrix"""
        # Get the flag position
        flag_start_col_square = FLAG_X // SQUARE_SIZE
        flag_start_row_square = FLAG_Y // SQUARE_SIZE
        flag_end_row_square = flag_start_row_square + FLAG_HEIGHT_SQUARES
        flag_end_col_square = flag_start_col_square + FLAG_WIDTH_SQUARES

        # Update flag position in matrix
        self.insert_object(flag_start_col_square, flag_end_col_square, flag_start_row_square, flag_end_row_square, FLAG)

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
        self.insert_object(soldier_start_col_square, soldier_end_col_square, soldier_start_row_square, soldier_end_row_square, SOLDIER)

        # print('\n'.join(map(','.join, self.board)))
        # print()

    def check_lose(self, soldier):
        """Checks if one of the soldier legs touched a mine"""
        legs_indexes = soldier.get_legs_index()
        # Check if one of the legs is mine
        for leg_index in legs_indexes:
            leg_col = leg_index[X_INDEX]
            leg_row = leg_index[Y_INDEX]
            if self.board[leg_row][leg_col] == MINE:
                return True
        return False


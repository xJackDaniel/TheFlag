import random
import ast
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
            return SAFE_ZONE_X_START <= x < SAFE_ZONE_X_END

        def check_y_safe_zone(y):
            """Returns True/False if y is in the safe zone"""
            return SAFE_ZONE_Y_START <= y < SAFE_ZONE_Y_END

        def check_x_flag_zone(x):
            """Returns True/False if x is in the flag safe zone"""
            return SAFE_ZONE_X_FLAG_START <= x < SAFE_ZONE_X_FLAG_END

        def check_y_flag_zone(y):
            """Returns True/False if y is in the flag safe zone"""
            return SAFE_ZONE_Y_FLAG_START <= y < SAFE_ZONE_Y_FLAG_END

        for mine in range(MINE_COUNT):
            valid_mine = False
            while not valid_mine:
                mine_col_x = random.randrange(MIN_X, MAX_X - MINE_WIDTH, SQUARE_SIZE)
                mine_row_y = random.randrange(MIN_MINE_Y, MAX_Y - MINE_HEIGHT, SQUARE_SIZE)
                while (check_x_safe_zone(mine_col_x) and check_y_safe_zone(mine_row_y)) or (
                        check_x_flag_zone(mine_col_x) and check_y_flag_zone(mine_row_y)):
                    # The mine is not valid
                    mine_col_x = random.randrange(MIN_X, MAX_X - MINE_WIDTH, SQUARE_SIZE)
                    mine_row_y = random.randrange(MIN_MINE_Y, MAX_Y - MINE_HEIGHT, SQUARE_SIZE)
                else:
                    valid_mine = True
                    # Add mine to screen and to list
                    self.mines.append((mine_col_x, mine_row_y))
                    self.insert_mine_position(mine_col_x, mine_row_y)

    def insert_object(self, start_x, end_x, start_y, end_y, value):
        """Inserts an object to the matrix"""
        for row in range(start_y, end_y):
            for col in range(start_x, end_x):
                # check that the soldier will not overwrite the mines or the flag
                if value == SOLDIER:
                    current_square = self.board[row][col]
                    if current_square == EMPTY:
                        self.board[row][col] = SOLDIER
                else:
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
        self.insert_object(soldier_start_col_square, soldier_end_col_square, soldier_start_row_square,
                           soldier_end_row_square, SOLDIER)

        # print('\n'.join(map(','.join, self.board)))
        # print()

    def load_save(self, data, screen, soldier):
        """Loads a save to current game"""

        def remove_nan(lst):
            """Removes all nan values from list"""
            return list(filter(lambda a: str(a) != DATA_EMPTY_COL, lst))

        df_len = len(data)
        # Get the board
        new_board = data.values[:ROWS_COUNT].tolist()
        # Get soldier location
        new_soldier_location = remove_nan(data.iloc[df_len - DATA_SOLDIER_ROW - 1].values.tolist())
        # Get bushes and convert them back to dict
        new_bushes_lst = remove_nan(data.iloc[df_len - DATA_BUSHES_ROW - 1].values.tolist())
        for bush_index, new_bush in enumerate(new_bushes_lst):
            new_bushes_lst[bush_index] = ast.literal_eval(new_bush)
        # Get Mines and convert them back to tuple
        new_mines_lst = remove_nan(data.iloc[df_len - DATA_MINES_ROW - 1].values.tolist())
        for mine_index, new_mine in enumerate(new_mines_lst):
            new_mines_lst[mine_index] = ast.literal_eval(new_mine)
        # Update the data
        self.board = new_board
        self.mines = new_mines_lst
        screen.update_bushes(new_bushes_lst)
        soldier.update_position(new_soldier_location)


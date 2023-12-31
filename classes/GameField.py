import random
import ast
from consts import *


class GameField:
    """Class that represents the Game matrix"""
    def __init__(self):
        self.board = []
        self.mines = []
        self.teleports = []
        self.build_empty_board()
        self.insert_flag_position()
        self.insert_mines()
        self.insert_teleports()

    def build_empty_board(self):
        """Building an empty matrix"""
        self.board = [[EMPTY for col in range(COLS_COUNT)] for row in range(ROWS_COUNT)]

    def get_board(self):
        """
            Returns the board
            :rtype: list[[list]]
        """
        return self.board

    def get_mines(self):
        """
            Returns the mines
            :rtype: list
        """
        return self.mines

    def get_teleports(self):
        """
            Returns the teleports
            :rtype: list
        """
        return self.teleports

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

        def check_mine(x, y):
            """Check if there is a space between the mine to other teleports and objects"""
            # Get the mine position
            mine_start_col_square = x // SQUARE_SIZE - MINE_SPACE_SQUARES
            mine_start_row_square = y // SQUARE_SIZE - MINE_SPACE_SQUARES
            mine_end_row_square = mine_start_row_square + MINE_HEIGHT_SQUARES + MINE_SPACE_SQUARES + 1
            mine_end_col_square = mine_start_col_square + MINE_WIDTH_SQUARES + MINE_SPACE_SQUARES + 1

            # First check - no mine or other object in the wanted position
            # Second check - no mine or other object in radius of 2 squares from the wanted position
            for row_index in range(mine_start_row_square, mine_end_row_square):
                for col_index in range(mine_start_col_square, mine_end_col_square):
                    if col_index >= COLS_COUNT:
                        continue
                    current_square = self.board[row_index][col_index]
                    if current_square != EMPTY:
                        return False
            return True

        for mine in range(MINE_COUNT):
            valid_mine = False
            while not valid_mine:
                mine_col_x = random.randrange(MIN_X, MAX_MINE_X, SQUARE_SIZE)
                mine_row_y = random.randrange(MIN_MINE_Y, MAX_MINE_Y, SQUARE_SIZE)
                while ((check_x_safe_zone(mine_col_x) and check_y_safe_zone(mine_row_y)) or (
                        check_x_flag_zone(mine_col_x) and check_y_flag_zone(mine_row_y)) or
                       not check_mine(mine_col_x, mine_row_y)):
                    # The mine is not valid
                    mine_col_x = random.randrange(MIN_X, MAX_MINE_X, SQUARE_SIZE)
                    mine_row_y = random.randrange(MIN_MINE_Y, MAX_MINE_Y, SQUARE_SIZE)
                else:
                    valid_mine = True
                    # Add mine to screen and to list
                    self.mines.append((mine_col_x, mine_row_y))
                    self.insert_mine_position(mine_col_x, mine_row_y)

    def insert_object(self, start_x, end_x, start_y, end_y, value):
        """
            Inserts an object to the matrix
            :param start_x: int
            :param end_x: int
            :param start_y: int
            :param end_y: int
            :param value: str
        """
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
        """
            Insert the mine position to matrix
            :param x: int
            :param y: int
        """
        # Get the flag position
        mine_start_col_square = x // SQUARE_SIZE
        mine_start_row_square = y // SQUARE_SIZE
        mine_end_row_square = mine_start_row_square + MINE_HEIGHT_SQUARES
        mine_end_col_square = mine_start_col_square + MINE_WIDTH_SQUARES

        # Update mine position in matrix
        self.insert_object(mine_start_col_square, mine_end_col_square, mine_start_row_square, mine_end_row_square, MINE)

    def insert_teleport_position(self, x, y):
        """
            Insert the teleport position to matrix
            :param x: int
            :param y: int
        """
        # Get the flag position
        teleport_start_col_square = x // SQUARE_SIZE
        teleport_start_row_square = y // SQUARE_SIZE
        teleport_end_row_square = teleport_start_row_square + TELEPORT_HEIGHT_SQUARES
        teleport_end_col_square = teleport_start_col_square + TELEPORT_WIDTH_SQUARES

        # Update mine position in matrix
        self.insert_object(teleport_start_col_square, teleport_end_col_square, teleport_start_row_square, teleport_end_row_square, TELEPORT)

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
        """
            Updates the soldier location in the grid
            :param soldier: Soldier Object
        """
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


    def load_save(self, data, screenObj, soldier, guard):
        """
            Loads a save to current game
            :param data: pandas DataFrame
            :param screenObj: Screen Object
            :param soldier: Soldier Object
            :param guard: Guard Object
        """

        def remove_nan(lst):
            """
                Removes all nan values from list
                :param lst: list
                :rtype: list
            """
            return list(filter(lambda a: str(a) != DATA_EMPTY_COL, lst))

        def get_valid_lst(lst):
            """
                Gets a str list and returns a valid python list
                :param lst: list
                :rtype: list
            """
            for index, value in enumerate(lst):
                lst[index] = ast.literal_eval(value)
            return lst
        df_len = len(data)
        # Get the board
        new_board = data.values[:ROWS_COUNT].tolist()
        # Get Guard location
        new_guard = remove_nan(data.iloc[df_len - DATA_GUARD_ROW - 1].values.tolist())
        new_guard_location = (new_guard[X_INDEX], new_guard[Y_INDEX])
        new_guard_direction = new_guard[DIRECTION_INDEX]
        # Get Teleports and convert them back to tuple
        new_teleports_lst = get_valid_lst(remove_nan(data.iloc[df_len - DATA_TELEPORTS_ROW - 1].values.tolist()))
        # Get soldier location
        new_soldier_location = remove_nan(data.iloc[df_len - DATA_SOLDIER_ROW - 1].values.tolist())
        # Get bushes and convert them back to dict
        new_bushes_lst = get_valid_lst(remove_nan(data.iloc[df_len - DATA_BUSHES_ROW - 1].values.tolist()))
        # Get Mines and convert them back to tuple
        new_mines_lst = get_valid_lst(remove_nan(data.iloc[df_len - DATA_MINES_ROW - 1].values.tolist()))
        # Update the data
        self.board = new_board
        self.teleports = new_teleports_lst
        self.mines = new_mines_lst
        screenObj.update_bushes(new_bushes_lst)
        soldier.update_position(new_soldier_location)
        guard.update_position(new_guard_location)
        guard.set_direction(new_guard_direction)
        # Set guard image
        if new_guard_direction == RIGHT_DIRECTION:
            guard.change_image(GUARD_RIGHT_IMG_PATH)
        else:
            guard.change_image(GUARD_LEFT_IMG_PATH)


    def insert_teleports(self):
        """Inserting teleports to the grid"""

        def check_teleport(x, y):
            """
                Check if there is a space between the teleport to other mines and objects
                :param x: int
                :param y: int
                :rtype: bool
            """
            # Get the flag position
            teleport_start_col_square = x // SQUARE_SIZE - TELEPORT_SPACE_SQUARES
            teleport_start_row_square = y // SQUARE_SIZE - TELEPORT_SPACE_SQUARES
            teleport_end_row_square = teleport_start_row_square + TELEPORT_HEIGHT_SQUARES + TELEPORT_SPACE_SQUARES + 1
            teleport_end_col_square = teleport_start_col_square + TELEPORT_WIDTH_SQUARES + TELEPORT_SPACE_SQUARES + 1

            # First check - no mine in the wanted position
            # Second check - no mine in radius of 2 squares from the wanted position
            for row_index in range(teleport_start_row_square, teleport_end_row_square):
                for col_index in range(teleport_start_col_square, teleport_end_col_square):
                    current_square = self.board[row_index][col_index]
                    if current_square != EMPTY:
                        return False
            return True

        for teleport in range(TELEPORT_COUNT):
            valid_teleport = False
            while not valid_teleport:
                teleport_col_x = random.randrange(MIN_TELEPORT_X, MAX_TELEPORT_X, SQUARE_SIZE)
                teleport_row_y = random.randrange(MIN_TELEPORT_Y, MAX_TELEPORT_Y, SQUARE_SIZE)
                while not check_teleport(teleport_col_x, teleport_row_y):
                    # The teleport is not valid
                    teleport_col_x = random.randrange(MIN_X, MAX_X - TELEPORT_WIDTH, SQUARE_SIZE)
                    teleport_row_y = random.randrange(MIN_TELEPORT_Y, MAX_Y - TELEPORT_HEIGHT, SQUARE_SIZE)
                else:
                    valid_teleport = True
                    # Add mine to screen and to list
                    self.teleports.append((teleport_col_x, teleport_row_y))
                    self.insert_teleport_position(teleport_col_x, teleport_row_y)

    def get_teleport_location(self, col_x, row_y):
        """
            Returns the teleport location as a tuple like (x,y)
            :param col_x: int
            :param row_y: int
            :rtype: tuple (col, row)
        """
        # Try to move left to find the start of the teleport
        found = False
        while not found:
            check_col = col_x - 1
            left_position = self.board[row_y][check_col]
            if left_position != TELEPORT:
                return col_x, row_y
            col_x -= 1


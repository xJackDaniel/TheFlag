import random

from consts import *


class Soldier:
    """Class that represents the soldier in the game"""
    def __init__(self, game_field):
        self.in_bush = False
        self.img_path = SOLDIER_IMG_PATH
        self.x = START_SOLDIER_X
        self.y = START_SOLDIER_Y
        self.width = SOLDIER_WIDTH
        self.height = SOLDIER_HEIGHT
        self.status = NOT_RUNNING_STATUS
        # Insert the soldier to board
        game_field.update_soldier_location(self)

    def get_x(self):
        """
            Returns the x of the soldier
            :rtype: int
        """
        return self.x

    def get_y(self):
        """
            Returns the y of the soldier
            :rtype: int
        """
        return self.y

    def is_in_bush(self):
        """
            Returns if the soldier is in a bush
            :rtype: bool
        """
        return self.in_bush

    def set_status(self, status):
        """
            Sets a status to the soldier object
            :param status: str
        """
        self.status = status

    def change_image(self, img):
        """
            Change the soldier image
            :param img: str (img path)
        """
        self.img_path = img

    def draw_soldier(self, screenObj, transparent=False):
        """
            Draws the soldier to the screen
            :param screenObj: Screen Object
            :param transparent: bool (optional)
        """
        location = (self.x, self.y)
        size = (self.width, self.height)
        if self.in_bush:
            transparent = True
        screenObj.draw_object(self.img_path, location, size, transparent)

    def check_lose(self, game_field):
        """
            Checks if one of the soldier legs touched a mine
            :param game_field: GameField Object
            :rtype: bool
        """
        legs_indexes = self.get_legs_index()
        # Check if one of the legs is mine
        for leg_index in legs_indexes:
            leg_col = leg_index[X_INDEX]
            leg_row = leg_index[Y_INDEX]
            board = game_field.get_board()
            if board[leg_row][leg_col] == MINE:
                self.status = LOSE_STATUS
                return True
        return False

    def check_win(self, game_field):
        """
            Check if the soldier body touch the Flag
            :param game_field: GameField Object
            :rtype: bool
        """
        body_indexes = self.get_body_index()
        for body_index in body_indexes:
            x_body = body_index[X_INDEX]
            y_body = body_index[Y_INDEX]
            board = game_field.get_board()
            if board[y_body][x_body] == FLAG:
                self.status = WIN_STATUS
                return True
        return False

    def check_bush(self, screenObj):
        """
            Returns if the soldier is in a bush
            :param screenObj: Screen Object
        """
        bushes = screenObj.get_bushes()
        in_bush = False
        for bush in bushes:
            bush_x, bush_y = bush.get(BUSH_LOCATION_KEY)
            bush_width, bush_height = bush.get(BUSH_SIZE_KEY)
            if (bush_x <= self.x <= bush_x + bush_width) and \
                    (self.y <= bush_y <= self.y + SOLDIER_HEIGHT or
                     self.y <= bush_y + bush_height <= self.y + SOLDIER_HEIGHT):
                        in_bush = True
                        break
        self.in_bush = in_bush

    def check_teleport(self, game_field):
        """
            Checks if one of the soldier legs touched a teleport
            :param game_field: GameField Object
        """
        if self.status != WIN_STATUS or self.status != LOSE_STATUS:
            legs_indexes = self.get_legs_index()
            # Check if one of the legs is TELEPORT
            for leg_index in legs_indexes:
                leg_col = leg_index[X_INDEX]
                leg_row = leg_index[Y_INDEX]
                board = game_field.get_board()
                if board[leg_row][leg_col] == TELEPORT:
                    # Get the teleport x,y
                    current_teleport = game_field.get_teleport_location(leg_col, leg_row)
                    self.teleport(game_field, current_teleport)

    def teleport(self, game_field, current_teleport):
        """
            Teleports to another teleport
            :param game_field: GameField Object
            :param current_teleport: tuple (x, y)
        """
        teleport_location = (current_teleport[X_INDEX] * SQUARE_SIZE, current_teleport[Y_INDEX] * SQUARE_SIZE)
        # Choose another teleport
        all_teleports = game_field.get_teleports().copy()
        # Remove the current teleport - to choose another teleport randomly
        all_teleports.remove(teleport_location)
        # Choose random teleport
        rnd_teleport = random.choice(all_teleports)
        # move the soldier
        self.x = rnd_teleport[X_INDEX]
        self.y = rnd_teleport[Y_INDEX] - SQUARE_SIZE * SOLDIER_HEIGHT_SQUARES
        # Change Status
        self.status = TELEPORT_STATUS

    def move_x(self, right: bool, game_field, screenObj):
        """
            updating soldier position - only right and left
            :param right: bool
            :param game_field: GameField Object
            :param screenObj: Screen Object
        """
        moved = False
        if right:
            # Make sure that the soldier is not crossing the screen size
            if not (self.x + STEP_SIZE > WINDOW_WIDTH - SOLDIER_WIDTH):
                self.x += STEP_SIZE
                moved = True
        else:
            if not self.x == MIN_X:
                self.x -= STEP_SIZE
                moved = True
        if moved:
            # Check bush
            self.check_bush(screenObj)
            # Check teleport
            self.check_teleport(game_field)
            game_field.update_soldier_location(self)
            # Check lose/win
            lose = self.check_lose(game_field)
            if not lose:
                self.check_win(game_field)

    def move_y(self, up: bool, game_field, screenObj):
        """
            updating soldier position - only up and down
            :param up: bool
            :param game_field: GameField Object
            :param screenObj: Screen Object
        """
        moved = False
        if up:
            if not self.y == MIN_Y:
                self.y -= STEP_SIZE
                moved = True
        else:
            # Make sure that the soldier is not crossing the screen size
            if not (self.y + STEP_SIZE > WINDOW_HEIGHT - SOLDIER_HEIGHT):
                self.y += STEP_SIZE
                moved = True
        if moved:
            # Check bush
            self.check_bush(screenObj)
            # Check teleport
            self.check_teleport(game_field)
            game_field.update_soldier_location(self)
            # Check lose/win
            lose = self.check_lose(game_field)
            if not lose:
                self.check_win(game_field)

    def get_legs_index(self):
        """
            Returns the index of the soldier legs
            :rtype: list
        """
        indexes = []
        for col in range(SOLDIER_WIDTH_SQUARES):
            y_square = self.y // SQUARE_SIZE
            x_square = self.x // SQUARE_SIZE
            indexes.append([x_square + col, y_square + SOLDIER_HEIGHT_SQUARES - 1])
        return indexes

    def get_body_index(self):
        """
            Returns the index of the soldier body
            :rtype: list
        """
        indexes = []
        for row in range(SOLDIER_HEIGHT_SQUARES):
            for col in range(SOLDIER_WIDTH_SQUARES):
                y_square = self.y // SQUARE_SIZE
                x_square = self.x // SQUARE_SIZE
                indexes.append([x_square + col, y_square + row])
        # Remove the legs indexes
        leg_indexes = self.get_legs_index()
        for leg_index in leg_indexes:
            indexes.remove(leg_index)
        return indexes

    def get_status(self):
        """
            Returns the soldier status
            :rtype: str
        """
        return self.status

    def update_position(self, location):
        """
            Updates the soldier location - Used to load saves
            :param location: tuple (x, y)
        """
        self.x = location[X_INDEX]
        self.y = location[Y_INDEX]

    def blink(self, screens, screenObj, guard):
        """
            Blink the soldier image
            :param screens: screens module
            :param screenObj: Screen Object
            :param guard: Guard Object
        """
        def is_even(num):
            """
                Returns if a num is even
                :param num: int
                :rtype: bool
            """
            return num % 2 == 0
        # Blink the soldier
        for blink in range(TELEPORT_BLINK_TIMES+1):
            if is_even(blink):
                transparent = True
            else:
                transparent = False
            screens.display_regular_screen(screenObj, self, SOLDIER_IMG_PATH, guard, transparent)
            # Update the display
            pygame.display.update()
            # Delay between the blinks
            pygame.time.wait(BLINK_DELAY)
        self.set_status(RUNNING_STATUS)

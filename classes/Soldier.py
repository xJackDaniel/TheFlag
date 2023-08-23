from consts import *

# TODO: Add notes to class
class Soldier:
    def __init__(self, game_field):
        self.img_path = SOLDIER_IMG_PATH
        self.x = START_SOLDIER_X
        self.y = START_SOLDIER_Y
        self.width = SOLDIER_WIDTH
        self.height = SOLDIER_HEIGHT
        self.status = RUNNING_STATUS
        # Insert the soldier to board
        game_field.update_soldier_location(self)


    def get_x(self):
        """Returns the x of the soldier"""
        return self.x

    def get_y(self):
        """Returns the y of the soldier"""
        return self.y

    def change_soldier_image(self, img):
        """Change the soldier image"""
        self.img_path = img

    def draw_soldier(self, screenObj):
        """Draws the soldier to the screen"""
        location = (self.x, self.y)
        size = (self.width, self.height)
        screenObj.draw_object(self.img_path, location, size)

    def check_lose(self, game_field):
        """Checks if one of the soldier legs touched a mine"""
        legs_indexes = self.get_legs_index()
        # Check if one of the legs is mine
        for leg_index in legs_indexes:
            leg_col = leg_index[X_INDEX]
            leg_row = leg_index[Y_INDEX]
            board = game_field.get_board()
            if board[leg_row][leg_col] == MINE:
                return True
        return False

    def move_x(self, right: bool, game_field):
        """updating soldier position - only right and left """
        moved = False
        if right:
            # Make sure that the soldier is not crossing the screen size
            if not (self.x+STEP_SIZE > WINDOW_WIDTH-SOLDIER_WIDTH):
                self.x += STEP_SIZE
                moved = True
        else:
            if not self.x == MIN_X:
                self.x -= STEP_SIZE
                moved = True
        if moved:
            # Check lose
            if self.check_lose(game_field):
                self.status = LOSE_STATUS
            game_field.update_soldier_location(self)

    def move_y(self, up: bool, game_field):
        """updating soldier position - only up and down """
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
            # Check lose
            if self.check_lose(game_field):
                self.status = LOSE_STATUS
            game_field.update_soldier_location(self)

    def get_legs_index(self):
        """Returns the index of the soldier legs"""
        indexes = []
        for col in range(SOLDIER_WIDTH_SQUARES):
            y_square = self.y // SQUARE_SIZE
            x_square = self.x // SQUARE_SIZE
            indexes.append([x_square+col, y_square + SOLDIER_HEIGHT_SQUARES - 1])
        return indexes

    def get_body_index(self):
        """Returns the index of the soldier body"""
        indexes = []
        for row in range(SOLDIER_HEIGHT_SQUARES):
            for col in range(SOLDIER_WIDTH_SQUARES):
                y_square = self.y // SQUARE_SIZE
                x_square = self.x // SQUARE_SIZE
                indexes.append([x_square+col, y_square+row])
        # Remove the legs indexes
        leg_indexes = self.get_legs_index()
        for leg_index in leg_indexes:
            indexes.remove(leg_index)
        return indexes

    def get_status(self):
        """Returns the soldier status"""
        return self.status


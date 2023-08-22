from consts import *

# TODO: Add notes to class
class Soldier:
    def __init__(self, screen, game_field):
        self.img_path = SOLDIER_IMG_PATH
        self.x = START_SOLDIER_X
        self.y = START_SOLDIER_Y
        self.width = SOLDIER_WIDTH
        self.height = SOLDIER_HEIGHT
        # Classes
        self.screenObj = screen
        self.game_field = game_field
        # Insert the soldier to board
        self.game_field.update_soldier_location(self)


    def get_x(self):
        """Returns the x of the soldier"""
        return self.x

    def get_y(self):
        """Returns the y of the soldier"""
        return self.y

    def change_soldier_image(self, img):
        """Change the soldier image"""
        self.img_path = img

    def draw_soldier(self):
        """Draws the soldier to the screen"""
        location = (self.x, self.y)
        size = (self.width, self.height)
        self.screenObj.draw_object(self.img_path, location, size)

    def move_x(self, right: bool):
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
            self.game_field.update_soldier_location(self)

    def move_y(self, up: bool):
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
            self.game_field.update_soldier_location(self)

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



from classes.Soldier import Soldier
from consts import *


class Guard(Soldier):
    def __init__(self, game_field):
        super().__init__(game_field=game_field)
        self.x = GUARD_START_X
        self.y = GUARD_START_Y
        self.direction = RIGHT_DIRECTION
        self.img_path = GUARD_RIGHT_IMG_PATH

    def get_direction(self):
        """Returns the direction"""
        return self.direction

    def set_direction(self, direction):
        """Set a moving direction to the guard"""
        self.direction = direction

    def move_guard(self, soldier):
        """Move the guard on the screen"""
        # Check if guard gets to end of screen
        if self.direction == RIGHT_DIRECTION and self.x + GUARD_WIDTH >= WINDOW_WIDTH:
            # We need to turn it to left
            self.direction = LEFT_DIRECTION
            self.img_path = GUARD_LEFT_IMG_PATH
        elif self.direction == LEFT_DIRECTION and self.x <= 0:
            # We need to turn it to right
            self.direction = RIGHT_DIRECTION
            self.img_path = GUARD_RIGHT_IMG_PATH
        # Move the guard
        if self.direction == RIGHT_DIRECTION:
            self.x += GUARD_STEP_SIZE
        else:
            self.x -= GUARD_STEP_SIZE
        # Check lose
        self.check_lose(soldier)

    def check_lose(self, soldier):
        """Checks if one of the soldier touched the guard"""
        if not soldier.is_in_bush():
            # If the soldier is in a bush, The guard can't kill him
            soldier_start_y = soldier.get_y()
            soldier_end_y = soldier_start_y + SOLDIER_HEIGHT
            if (self.x <= soldier.get_x() <= self.x + GUARD_WIDTH) and \
                    (self.y <= soldier_start_y <= self.y + GUARD_HEIGHT or
                     self.y <= soldier_end_y < self.y + GUARD_HEIGHT):
                self.status = LOSE_STATUS
                return True
            return False

    def draw_guard(self, screenObj):
        """Draws the guard to the screen"""
        location = (self.x, self.y)
        size = (self.width, self.height)
        screenObj.draw_object(self.img_path, location, size)

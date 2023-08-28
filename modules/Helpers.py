from consts import *

def mouse_in_object(mouse_pos, obj_x, obj_y, obj_width, obj_height):
    """
        Checks if mouse in object
        :param mouse_pos: tuple (x, y)
        :param obj_x: int
        :param obj_y: int
        :param obj_width: int
        :param obj_height: int
    """
    if obj_x + obj_width > mouse_pos[X_INDEX] > obj_x and \
            obj_y < mouse_pos[Y_INDEX] < obj_y + obj_height:
        return True
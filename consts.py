import pygame

ROWS_COUNT = 25
COLS_COUNT = 50

SQUARE_SIZE = 20

WINDOW_WIDTH = COLS_COUNT * SQUARE_SIZE
WINDOW_HEIGHT = ROWS_COUNT * SQUARE_SIZE

WINDOW_CAPTION = "The flag"

GREEN = (67, 161, 68)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

X_INDEX = 0
Y_INDEX = 1

FPS = 60

EMPTY = "EMPTY"
SOLDIER = "SOLDIER"
FLAG = "FLAG"
MINE = "MINE"
TELEPORT = "TELEPORT"

MIN_X = 0
MAX_X = WINDOW_WIDTH

MIN_Y = 0
MAX_Y = WINDOW_HEIGHT

BUSH_IMG_PATH = "img/grass.png"
BUSH_COUNT = 20
BUSH_SIZE = (SQUARE_SIZE * 2, SQUARE_SIZE * 2)
BUSH_LOCATION_KEY = "location"
BUSH_SIZE_KEY = "size"
BUSH_WIDTH_INDEX = 0
BUSH_HEIGHT_INDEX = 1

SOLDIER_IMG_PATH = "img/soldier.png"
SOLDIER_MINE_SCREEN_IMG_PATH = "img/soldier_nigth.png"
SOLDIER_EXPLODED_IMG_PATH = "img/explotion.png"

TRANSPARENT_ALPHA_NUM = 128

START_SOLDIER_X = 0
START_SOLDIER_Y = 0
SOLDIER_WIDTH_SQUARES = 2
SOLDIER_HEIGHT_SQUARES = 4
SOLDIER_WIDTH = SOLDIER_WIDTH_SQUARES * SQUARE_SIZE
SOLDIER_HEIGHT = SOLDIER_HEIGHT_SQUARES * SQUARE_SIZE

FLAG_IMG_PATH = "img/flag.png"
FLAG_WIDTH_SQUARES = 4
FLAG_HEIGHT_SQUARES = 3
FLAG_WIDTH = FLAG_WIDTH_SQUARES * SQUARE_SIZE
FLAG_HEIGHT = FLAG_HEIGHT_SQUARES * SQUARE_SIZE
FLAG_X = WINDOW_WIDTH - FLAG_WIDTH
FLAG_Y = WINDOW_HEIGHT - FLAG_HEIGHT

WELCOME_MESSAGE = """Welcome to The Flag game, Have Fun!"""
WELCOME_X = SQUARE_SIZE
WELCOME_Y = SQUARE_SIZE
WELCOME_FONT = "arial"
WELCOME_SIZE = 20

LOSE_MESSAGE = """You lose!"""
LOSE_X = WINDOW_WIDTH // 2 - 10 * SQUARE_SIZE
LOSE_Y = WINDOW_HEIGHT // 2 - 5 * SQUARE_SIZE
LOSE_FONT = "arial"
LOSE_SIZE = 100

WIN_MESSAGE = """You won!"""
WIN_X = WINDOW_WIDTH // 2 - 10 * SQUARE_SIZE
WIN_Y = WINDOW_HEIGHT // 2 - 5 * SQUARE_SIZE
WIN_FONT = "arial"
WIN_SIZE = 100

NOT_FOUND_MESSAGE = """Save number {number} not found!"""
NOT_FOUND_X = WINDOW_WIDTH // 2 - 12 * SQUARE_SIZE
NOT_FOUND_Y = WINDOW_HEIGHT // 2 - 5 * SQUARE_SIZE
NOT_FOUND_FONT = "arial"
NOT_FOUND_SIZE = 50

LOADING_SAVE_MESSAGE = """Loading save number {number}..."""
LOADING_SAVE_X = WINDOW_WIDTH // 2 - 12 * SQUARE_SIZE
LOADING_SAVE_Y = WINDOW_HEIGHT // 2 - 5 * SQUARE_SIZE
LOADING_SAVE_FONT = "arial"
LOADING_SAVE_SIZE = 50


SAVED_MESSAGE = """Game was successfully saved to save number {number}!"""
SAVED_X = WINDOW_WIDTH // 2 - 18 * SQUARE_SIZE
SAVED_Y = WINDOW_HEIGHT // 2 - 5 * SQUARE_SIZE
SAVED_FONT = "arial"
SAVED_SIZE = 40


STEP_SIZE = SQUARE_SIZE

SAFE_ZONE_X_START = 0
SAFE_ZONE_X_END = SOLDIER_WIDTH + 3 * SQUARE_SIZE
SAFE_ZONE_Y_START = 0
SAFE_ZONE_Y_END = SOLDIER_HEIGHT + 3 * SQUARE_SIZE

SAFE_ZONE_X_FLAG_START = WINDOW_WIDTH - FLAG_WIDTH - 3 * SQUARE_SIZE
SAFE_ZONE_X_FLAG_END = WINDOW_WIDTH
SAFE_ZONE_Y_FLAG_START = WINDOW_HEIGHT - FLAG_WIDTH - 3 * SQUARE_SIZE
SAFE_ZONE_Y_FLAG_END = WINDOW_HEIGHT

MINE_IMG_PATH = "img/mine.png"
MINE_COUNT = 20
MINE_WIDTH_SQUARES = 3
MINE_HEIGHT_SQUARES = 1
MINE_WIDTH = MINE_WIDTH_SQUARES * SQUARE_SIZE
MINE_HEIGHT = MINE_HEIGHT_SQUARES * SQUARE_SIZE

LINE_WIDTH = 1

MINE_SCREEN_DELAY = 1000
END_GAME_DELAY = 3000
MESSAGE_DELAY = 2000
BLINK_DELAY = 500

RUNNING_STATUS = "running"
WIN_STATUS = "win"
LOSE_STATUS = "lose"
TELEPORT_STATUS = "teleport"

DATABASE_FILE = "data/data.xlsx"
KEY_ERROR = "There is no saved game at this number!"
SUCCESS = "Success"
APPEND_MODE = "a"
WRITE_MODE = "w"

SAVE_KEYS = {pygame.K_1: "1", pygame.K_2: "2", pygame.K_3: "3", pygame.K_4: "4", pygame.K_5: "5", pygame.K_6: "6",
             pygame.K_7: "7", pygame.K_8: "8", pygame.K_9: "9"}

CHECK_DELAY = 1

DATA_MINES_ROW = 0
DATA_BUSHES_ROW = 1
DATA_SOLDIER_ROW = 2
COUNT_OF_SAVED_ADDITIONAL_OBJECTS = 3

DATA_EMPTY_COL = "nan"

TELEPORT_IMG_PATH = "img/teleport.png"
TELEPORT_COUNT = 5
TELEPORT_WIDTH_SQUARES = 3
TELEPORT_HEIGHT_SQUARES = 1
TELEPORT_WIDTH = MINE_WIDTH
TELEPORT_HEIGHT = MINE_HEIGHT

TELEPORT_SPACE_SQUARES = 2
TELEPORT_SPACE = TELEPORT_SPACE_SQUARES * SQUARE_SIZE
MINE_SPACE_SQUARES = 2
MINE_SPACE = MINE_SPACE_SQUARES * SQUARE_SIZE

MIN_MINE_X = MINE_SPACE
MIN_MINE_Y = SOLDIER_HEIGHT + MINE_SPACE

MAX_MINE_X = MAX_X - MINE_WIDTH - MINE_SPACE
MAX_MINE_Y = MAX_Y - MINE_HEIGHT - MINE_SPACE

MIN_TELEPORT_X = TELEPORT_SPACE
MIN_TELEPORT_Y = SOLDIER_HEIGHT + TELEPORT_SPACE

MAX_TELEPORT_X = MAX_X - TELEPORT_WIDTH - TELEPORT_SPACE
MAX_TELEPORT_Y = MAX_Y - TELEPORT_HEIGHT - TELEPORT_SPACE

TELEPORT_BLINK_TIMES = 2

GUARD_FRIST_PLACEMENT = 13


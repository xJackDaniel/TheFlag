ROWS_COUNT = 25
COLS_COUNT = 50

SQUARE_SIZE = 20

WINDOW_WIDTH = COLS_COUNT*SQUARE_SIZE
WINDOW_HEIGHT = ROWS_COUNT*SQUARE_SIZE

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

MIN_X = 0
MAX_X = WINDOW_WIDTH

MIN_Y = 0
MAX_Y = WINDOW_HEIGHT

BUSH_IMG_PATH = "img/grass.png"
BUSH_COUNT = 20
BUSH_SIZE = (SQUARE_SIZE * 2, SQUARE_SIZE * 2)
BUSH_LOCATION_KEY = "location"
BUSH_SIZE_KEY = "size"

SOLDIER_IMG_PATH = "img/soldier.png"
SOLDIER_MINE_SCREEN_IMG_PATH = "img/soldier_nigth.png"
START_SOLDIER_X = 0
START_SOLDIER_Y = 0
SOLDIER_WIDTH_SQUARES = 2
SOLDIER_HEIGHT_SQUARES = 4
SOLDIER_WIDTH = SOLDIER_WIDTH_SQUARES*SQUARE_SIZE
SOLDIER_HEIGHT = SOLDIER_HEIGHT_SQUARES*SQUARE_SIZE

FLAG_IMG_PATH = "img/flag.png"
FLAG_WIDTH_SQUARES = 4
FLAG_HEIGHT_SQUARES = 3
FLAG_WIDTH = FLAG_WIDTH_SQUARES*SQUARE_SIZE
FLAG_HEIGHT = FLAG_HEIGHT_SQUARES*SQUARE_SIZE
FLAG_X = WINDOW_WIDTH-FLAG_WIDTH
FLAG_Y = WINDOW_HEIGHT-FLAG_HEIGHT


WELCOME_MESSAGE = """Welcome to The Flag game, Have Fun!"""
WELCOME_X = SQUARE_SIZE
WELCOME_Y = SQUARE_SIZE
WELCOME_FONT = "arial"
WELCOME_SIZE = 20

STEP_SIZE = SQUARE_SIZE

SAFE_ZONE_X_START = 0
SAFE_ZONE_X_END = SQUARE_SIZE*SOLDIER_WIDTH + 3*SQUARE_SIZE
SAFE_ZONE_Y_START = 0
SAFE_ZONE_Y_END = SQUARE_SIZE*SOLDIER_HEIGHT + 3*SQUARE_SIZE

MINE_IMG_PATH = "img/mine.png"
MINE_COUNT = 20
MINE_WIDTH_SQUARES = 3
MINE_HEIGHT_SQUARES = 1
MINE_WIDTH = MINE_WIDTH_SQUARES * SQUARE_SIZE
MINE_HEIGHT = MINE_HEIGHT_SQUARES * SQUARE_SIZE

LINE_WIDTH = 1


import pandas as pd
from consts import *


def write_to_csv(save_number, board, bushes, mines, soldier):
    """Writes the board and bushes to csv file"""
    # Add bushes to end of sheet
    board_copy = board.copy()
    # Soldier
    board_copy.append([soldier.get_x(), soldier.get_y()])
    # Bushes
    board_copy.append(bushes)
    # Mines
    board_copy.append(mines)
    # Write the board to Excel file with specific sheet name
    df = pd.DataFrame(board_copy)

    with pd.ExcelWriter(DATABASE_FILE, engine='openpyxl', mode=APPEND_MODE) as writer:
        workBook = writer.book
        try:
            workBook.remove(workBook[str(save_number)])
        except:
            pass
            # Worksheet does not exist
        finally:
            df.to_excel(writer, sheet_name=str(save_number), index=False, header=True)
            writer._save()


def read_csv(save_number):
    """Loads a save number from db"""
    try:
        data = pd.read_excel(DATABASE_FILE, sheet_name=str(save_number), engine='openpyxl')
        return data, SUCCESS
    except Exception as e:
        # Check if there is no data with this save_number
        if isinstance(e, KeyError) or isinstance(e, ValueError):
            return None, KEY_ERROR

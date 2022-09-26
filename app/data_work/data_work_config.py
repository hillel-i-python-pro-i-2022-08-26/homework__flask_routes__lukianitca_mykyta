from pathlib import Path

STORAGE_DIR = Path(__file__).parent.joinpath("storage")

CSV_FILE = STORAGE_DIR.joinpath("people_data.csv")
TXT_FILE = STORAGE_DIR.joinpath("txt_for_read.txt")
USERS_DB = STORAGE_DIR.joinpath("users.db")

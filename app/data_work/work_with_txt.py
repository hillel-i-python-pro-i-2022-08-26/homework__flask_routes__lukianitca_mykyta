import pathlib

cur_dir = pathlib.Path(__file__).parent


def read_txt() -> str:
    with open(cur_dir.joinpath("storage/txt_for_read.txt")) as file:
        return file.read()

from .data_work_config import DataWorkConfig


def read_txt() -> str:
    file_txt_path = DataWorkConfig.storage_directory.joinpath("txt_for_read.txt")
    with open(file_txt_path) as file:
        return file.read()

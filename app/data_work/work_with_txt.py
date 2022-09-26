from .data_work_config import TXT_FILE


def read_txt() -> str:
    # file_txt_path = DataWorkConfig.storage_directory.joinpath("txt_for_read.txt")
    with open(TXT_FILE) as file:
        return file.read()

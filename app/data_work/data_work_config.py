from pathlib import Path


class DataWorkConfig:
    storage_directory = Path(__file__).parent.joinpath("storage")

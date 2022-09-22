import numpy as np
import pandas as pd

from .data_work_config import DataWorkConfig


def get_average_data() -> dict:
    file_csv_path = DataWorkConfig.storage_directory.joinpath("people_data.csv")
    df_users = pd.read_csv(file_csv_path)
    mean_data = df_users.mean(axis=0)
    dict_users_mean_data = {
        "avg_height": np.around(mean_data[1] * 2.54, 2),
        "avg_weight": np.around(mean_data[2] / 2.205, 2),
    }
    return dict_users_mean_data

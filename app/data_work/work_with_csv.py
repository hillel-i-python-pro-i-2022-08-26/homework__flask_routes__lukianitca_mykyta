import pandas as pd
import numpy as np


def get_average_data() -> dict:
    df_users = pd.read_csv("storage/people_data.csv")
    mean_d = df_users.mean(axis=0)
    dict_users_data = {
        "avg_height": np.around(mean_d[1] * 2.54, 2),
        "avg_weight": np.around(mean_d[2] * 2.205, 2),
    }
    return dict_users_data

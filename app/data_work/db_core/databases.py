import sqlite3
from abc import ABC, abstractmethod

from app.data_work.data_work_config import USERS_DB_PATH


class UsersDB(ABC):
    def __init__(self):
        self.connection = sqlite3.connect(USERS_DB_PATH)

    @abstractmethod
    def create_table(self):
        """Table creation"""

import sqlite3

from db_core import UsersDB


class TelephoneBookTable(UsersDB):
    def create_table(self):
        self.connection.execute(
            """CREATE TABLE IF NOT EXISTS telephones (
                pk INTEGER PRIMARY KEY,
                contact_name VARCHAR NOT NULL,
                phone_number VARCHAR NOT NULL
            )"""
        )
        self.connection.commit()

    def __enter__(self):
        self.connection.row_factory = sqlite3.Row
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

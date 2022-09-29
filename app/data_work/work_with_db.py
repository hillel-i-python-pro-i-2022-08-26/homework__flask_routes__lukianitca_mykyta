import sqlite3

from app.data_work.db_core import UsersDB


class ContactsTable(UsersDB):
    def create_table(self):
        self.connection.execute(
            """CREATE TABLE IF NOT EXISTS telephones (
                pk INTEGER PRIMARY KEY,
                contact_name VARCHAR NOT NULL,
                phone_number VARCHAR NOT NULL
            );"""
        )

    def add_new_contact(self, contact_info: dict):
        self.connection.execute(
            "INSERT INTO telephones (contact_name, phone_number) VALUES (:contact_name, :phone_number);", contact_info
        )
        self.connection.commit()

    def get_one_record(self, user_id: int):
        return self.connection.execute("SELECT * FROM telephones WHERE pk=:pk;", {"pk": user_id}).fetchone()

    def get_all_records(self):
        return self.connection.execute("SELECT * FROM telephones ORDER BY contact_name").fetchall()

    def update_record(self, user_id: int, updates: dict):
        if not updates:
            raise ValueError
        rows = ", ".join([f"{row}=:{row}" for row in updates])
        updates["pk"] = user_id
        self.connection.execute(f"UPDATE telephones SET {rows} WHERE pk=:pk;", updates)
        self.connection.commit()

    def delete_record(self, user_id: int):
        self.connection.execute("DELETE FROM telephones WHERE pk=:pk;", {"pk": user_id})
        self.connection.commit()

    def __enter__(self):
        self.connection.row_factory = sqlite3.Row
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


def tables_init():
    with ContactsTable() as contact_table:
        contact_table.create_table()

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

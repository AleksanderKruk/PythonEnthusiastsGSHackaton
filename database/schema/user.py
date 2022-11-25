from pydantic import BaseModel
import uuid
from badge import Badge
import sqlite3 as sql

table_name = "submissions"

class user(BaseModel):
    def __int__(
        self,
        nick: str,
        email: str,
        password: str,
        points: int = 0,
        address: str = None,
        phone_number: str = None,
        id: uuid.UUID = None,
    ):
        self.id = id or uuid.uuid4()
        self.nick = nick
        self.email = email
        self.password = password
        self.points = points
        self.address = address
        self.phone_number = phone_number

    def insert(self):
        query = "INSERT INTO " \
                f"{table_name} (ID, NICK, EMAIL, PASSWORD, POINTS, ADDRESS, PHONE_NUMBER)" \
                "VALUES(?, ?, ?, ?, ?, ?, ?);"

        values = (self.id, self.nick, self.email, self.password, self.points, self.address, self.phone_number)

        sql.connect(table_name).execute(query, values)

    def delete(self):
        query = f"DELETE FROM {table_name} WHERE ID=?;"

        sql.connect(table_name).execute(query, (self.id,))

    def update(self):
        query = f"UPDATE table SET " \
                f"NICK=?, EMAIL=?, PASSWORD=?, POINTS=?, ADDRESS=?, PHONE_NUMBER=?" \
                f"WHERE ID=?"

        sql.connect(table_name).execute(query, (self.id,))



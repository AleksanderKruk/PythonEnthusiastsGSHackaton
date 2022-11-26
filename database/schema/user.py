from pydantic import BaseModel
import uuid
from badge import Badge
import sqlite3 as sql


class User(BaseModel):
    nick: str
    email: str
    password: str
    points: int = 0
    address: str = None
    phone_number: str = None
    id: uuid.UUID = None

    def insert(self):
        query = "INSERT INTO " \
                "users (ID, NICK, EMAIL, PASSWORD, POINTS, ADDRESS, PHONE_NUMBER)" \
                "VALUES(?, ?, ?, ?, ?, ?, ?);"

        values = (self.id, self.nick, self.email, self.password, self.points, self.address, self.phone_number)

        sql.connect("users").execute(query, values)

    def delete(self):
        query = "DELETE FROM users WHERE ID=?;"

        sql.connect("users").execute(query, (self.id,))

    def update(self):
        query = "UPDATE users SET " \
                "NICK=?, EMAIL=?, PASSWORD=?, POINTS=?, ADDRESS=?, PHONE_NUMBER=?" \
                "WHERE ID=?"
        values = (self.nick, self.email, self.password, self.points, self.address, self.phone_number)
        params = values + (self.id,)
        sql.connect("users").execute(query, params)

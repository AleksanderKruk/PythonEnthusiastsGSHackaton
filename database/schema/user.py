from pydantic import BaseModel
import uuid
from badge import Badge
import sqlite3 as sql
from secrets import token_hex


class user(BaseModel):
    def __init__(
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


    def token(self):
        query = 'UPDATE users SET token=? WHERE id=?'
        token = token_hex(32)
        conn = sql.connect('gs.db')
        conn.execute(query, (token, self.id))
        conn.commit()

        


from pydantic import BaseModel
import uuid
import sqlite3 as sql


class User(BaseModel):
    id: str = uuid.uuid4().hex
    nick: str
    email: str
    password: str
    points: int = 0
    token: str = None
    address: str = None
    phone_number: str = None

    @staticmethod
    def from_tuple(tup):
        return User(
            id=tup[0],
            nick=tup[1],
            email=tup[2],
            password=tup[3],
            points=tup[4],
            token=tup[5],
            address=tup[6],
            phone_number=tup[7],
        )

    def insert(self, con):
        query = "INSERT INTO " \
                "users (ID, NICK, EMAIL, PASSWORD, POINTS, ADDRESS, PHONE_NUMBER, TOKEN)" \
                "VALUES(?, ?, ?, ?, ?, ?, ?, ?);"

        values = (
            self.id, self.nick, self.email, self.password, self.points, self.address, self.phone_number, self.token
        )

        con.execute(query, values)

    def delete(self, con):
        query = "DELETE FROM users WHERE ID=?;"

        con.execute(query, (self.id,))

    def update(self, con):
        query = "UPDATE users SET " \
                "NICK=?, EMAIL=?, PASSWORD=?, POINTS=?, ADDRESS=?, PHONE_NUMBER=?, TOKEN=?" \
                "WHERE ID=?"
        values = (self.nick, self.email, self.password, self.points, self.address, self.phone_number, self.token)
        params = values + (self.id,)
        con.execute(query, params)

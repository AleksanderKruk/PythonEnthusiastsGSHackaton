#from pydantic import BaseModel
import uuid
import sqlite3 as sql

class Gadgets:
    id: uuid.UUID
    name: str
    point_cost: int
    image_url: str

    def __init__(self, uuid: uuid, name: str, point_cost: int, image_url: str):
        self.id = uuid
        self.name = name
        self.point_cost = point_cost
        self.image_url = image_url

    def insert(self):
        sql.connect("database\gs.db").execute(
            "INSERT INTO ? (id, name, point_cost, image_url) VALUES(?, ?, ?, ?);",
            (self.__class__.__name__, self.id, self.name, self.point_cost, self.image_url)
        )


    def delete(self, condition: str):
        sql.connect("database\gs.db").execute(
            "DELETE FROM ? WHERE id = ?;", (self.__class__.__name__, self.id)
        )

    def update(self):
        sql.connect("database\gs.db").execute(
            "UPDATE ? SET name = ?, point_cost = ?, image_url = ?;",
            (self.__class__.__name__, self.name, self.point_cost, self.image_url)
        )

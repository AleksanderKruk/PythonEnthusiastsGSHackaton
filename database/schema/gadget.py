#from pydantic import BaseModel
import uuid
import sqlite3 as sql
from pydantic import BaseModel

class Gadget(BaseModel):
    id: uuid.UUID
    name: str
    point_cost: int
    image_url: str

    @staticmethod
    def from_tuple(tup):
        return Gadget(
            id=tup[0],
            name=tup[1],
            point_cost=tup[2],
            image_url=tup[3]
        )

    def insert(self, con):
        con.execute(
            "INSERT INTO ? (id, name, point_cost, image_url) VALUES(?, ?, ?, ?);",
            (self.__class__.__name__, self.id, self.name, self.point_cost, self.image_url)
        )

    def delete(self, con):
        con.execute(
            "DELETE FROM ? WHERE id = ?;", (self.__class__.__name__, self.id)
        )

    def update(self, con):
        con.execute(
            "UPDATE ? SET name = ?, point_cost = ?, image_url = ?;",
            (self.__class__.__name__, self.name, self.point_cost, self.image_url)
        )

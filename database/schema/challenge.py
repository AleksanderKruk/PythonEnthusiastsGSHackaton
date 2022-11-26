import sqlite3 as sql
from challenge import Difficulty


class WrongNameError(ValueError):
    def __init__(self, *args) -> None:
        super().__init__(*args)

class MissingContentError(ValueError):
    def __init__(self, *args) -> None:
        super().__init__(*args)



class Challenge:
    def __init__(self, id: int, name: str, content: str, difficulty: Difficulty):
        if not name:    raise WrongNameError
        if not content: raise MissingContentError
        self.id = id
        self.name = name
        self.content = content
        self.difficulty = difficulty

    def insert(self):
        sql.connect("database\gs.db").execute(
            "INSERT INTO ?s (id, name, content, difficulty) VALUES(?, ?, ?, ?);",
            (self.__class__.__name__, self.id, self.name, self.content, self.difficulty.value)
        )

    def delete(self):
        sql.connect("database\gs.db").execute(
            "DELETE FROM ?s WHERE id = ?;", (self.__class__.__name__, self.id)
        )

    def update(self):
        sql.connect("database\gs.db").execute(
            "UPDATE ?s SET name = ?, content = ?, difficulty = ?  WHERE id = ?;",
            (self.__class__.__name__, self.name, self.content, self.difficulty, self.id)
        )



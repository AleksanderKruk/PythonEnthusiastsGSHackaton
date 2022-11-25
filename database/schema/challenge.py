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

    def insert(self, database, id: int, name: str, content: str, difficulty: Difficulty):
        database.execute(
            "INSERT INTO =?s (id, name, content, difficulty) VALUES(=?, =?, =?, =?);",
            (self.__class__.__name__, self.id, self.name, self.content, self.difficulty.value)
        )

    def delete(self, database, given_id):
        database.execute(
            "DELETE FROM =?s WHERE id = =?;", (self.__class__.__name__, given_id)
        )

    def update(self, database, given_id, new_name, new_content, new_difficulty):
        new_name = self.name if new_name is None else new_name
        new_content = self.content if new_content is None else new_content
        new_difficulty = self.difficulty if new_difficulty is None else new_difficulty
        database.execute(
            "UPDATE =?s SET name = =?, content = =?, difficulty = =?  WHERE id = =?;",
            (self.__class__.__name__, new_name, new_content, new_difficulty, given_id)
        )



from pydantic import BaseModel
import uuid
import datetime
import sqlite3 as sql

db_path = '../gs.db'


class Submission(BaseModel):
    id: str = uuid.uuid4().hex
    user_id: str
    challenge_id: str
    posting_iso: datetime.datetime
    text: str

    def insert(self, con):
        query = "INSERT INTO " \
                "submissions (ID, USER_ID, CHALLENGE_ID, POSTING_ISO, TEXT)" \
                "VALUES(?, ?, ?, ?, ?);"
        values = (self.id, self.user_id, self.challenge_id, self.posting_iso, self.text)
        con.execute(query, values)

    def delete(self, con):
        query = "DELETE FROM submissions WHERE ID=?;"

        con.execute(query, (self.id,))

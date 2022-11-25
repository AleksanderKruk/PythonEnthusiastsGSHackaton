from pydantic import BaseModel
import uuid
import datetime
import sqlite3 as sql


class Submissions(BaseModel):
    def __int__(
            self,
            user_id: uuid.UUID,
            challenges_id: uuid.UUID,
            posting_iso: datetime.datetime,
            content: str,
            id: uuid.UUID = None,
    ):
        self.id = id or uuid.uuid4()
        self.user_id: uuid.UUID = user_id
        self.challenges_id = challenges_id
        self.posting_iso = posting_iso
        self.content = content

    def insert(self):
        query = "INSERT INTO " \
                "submissions (ID, USER_ID, CHALLANGES_ID, POSTING_ISO, CONTENT)" \
                "VALUES(?, ?, ?, ?, ?);"
        values = (self.id, self.user_id, self.challenges_id, self.posting_iso, self.content)
        sql.connect("submissions").execute(query, values)

    def delete(self):
        query = "DELETE FROM submissions WHERE ID=?;"

        sql.connect("submissions").execute(query, (self.id,))

from pydantic import BaseModel
import uuid
import datetime
import sqlite3 as sql

table_name = "submissions"


class Submissions(BaseModel):
    def __int__(
            self,
            post_time: datetime.datetime,
            content: str,
            user_id: uuid.UUID = None,
    ):
        self.user_id: uuid.UUID = user_id or uuid.uuid4()
        self.post_time = post_time
        self.content = content

    def insert(self):
        query = "INSERT INTO " \
                f"{table_name} (USER_ID, POST_TIME, CONTENT)" \
                "VALUES(?, ?, ?);"

        sql.connect(table_name).execute(query, (self.user_id, self.post_time, self.content))

    def delete(self):
        query = f"DELETE FROM {table_name} WHERE USER_ID=?;"

        sql.connect(table_name).execute(query, (self.user_id,))



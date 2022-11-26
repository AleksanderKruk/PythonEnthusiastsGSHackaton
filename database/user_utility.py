from database.schema.user import User
from database.schema.submission import Submission
from datetime import datetime
import uuid
from sqlite3 import Connection


def register(nick, email, password, con: Connection):
    is_taken = is_email_taken(email, con)
    if is_taken:
        return None

    User(nick=nick, email=email, password=password).insert(con)
    con.commit()
    return True


def login(email, password, con: Connection):
    query_get_user = "SELECT * FROM users WHERE EMAIL=? AND PASSWORD=?"
    user_data = con.execute(query_get_user, (email, password)).fetchone()

    print(user_data)

    if user_data is None:
        return None

    user = User.from_tuple(user_data)

    user.token = uuid.uuid4().hex
    user.update(con)
    con.commit()
    return user.token


def validate_token(token: str, con: Connection):
    query = 'SELECT * FROM users WHERE token=?'
    if token is None:
        return None
    res = con.execute(query, (token,)).fetchone()
    return res


def is_email_taken(email, con):
    query = "SELECT * FROM users WHERE EMAIL=?"
    user = con.execute(query, (email,)).fetchone()
    return user is not None


def submit_solution(user_id: str, challenge_id: str, text: str, con):
    Submission(user_id=user_id, challenge_id=challenge_id, posting_iso=datetime.now(), text=text).insert(con)

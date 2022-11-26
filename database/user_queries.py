from schema.user import User
from schema.submission import Submission
from datetime import datetime
import uuid


def register(nick, email, password, con):
    is_taken = is_email_taken(email, con)
    if is_taken:
        return None

    User(nick=nick, email=email, password=password).insert(con)


def login(email, password, con):
    query_get_user = "SELECT * FROM users WHERE EMAIL=? AND PASSWORD=?"
    user_data = con.execute(query_get_user, (email, password)).fetchone()

    user = User.from_tuple(user_data)
    if user is None:
        return None

    user.token = uuid.uuid4().hex
    user.update(con)
    return user.token


def is_email_taken(email, con):
    query = "SELECT * FROM users WHERE EMAIL=?"
    user = con.execute(query, (email,)).fetchone()
    return user is not None


def submit_solution(user_id: str, challenge_id: str, text: str, con):
    Submission(user_id=user_id, challenge_id=challenge_id, posting_iso=datetime.now(), text=text).insert(con)

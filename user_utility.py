from database.schema.user import User
import sqlite3 as sql


def register(nick, email, password):
    is_taken = is_email_taken(email)
    if is_taken:
        return None

    User(nick=nick, email=email, password=password).insert()


def login(email, password):
    query = "SELECT TOKEN FROM tokens WHERE EMAIL=? AND PASSWORD=?"
    return sql.connect("users").execute(query, (email, password)).fetchone()


def is_email_taken(email):
    query = "SELECT COUNT(ID) FROM users WHERE EMAIL=?"
    count = sql.connect("users").execute(query, (email,)).fetchmany()
    return count != 0

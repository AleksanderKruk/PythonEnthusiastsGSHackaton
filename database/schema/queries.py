from sqlite3 import connect
import database.schema.gadget as GD
import uuid

def get_all(con):
    return con.execute("SELECT * FROM users;").fetchall()

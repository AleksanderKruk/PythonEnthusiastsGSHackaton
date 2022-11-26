from sqlite3 import connect

def get_all(table_name):
    return connect("database\gs.db").execute("SELECT * FROM ?;", (table_name,)).fetchall()


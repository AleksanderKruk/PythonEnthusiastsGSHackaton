from sqlite3 import connect


def get_all(table_name, con):
    return con.execute("SELECT * FROM ?;", (table_name,)).fetchall()


def buy_gadget(self, gadgets_id, con):
    gadget_being_bought = con.execute("SELECT * FROM gadgets WHERE id = ?;", (gadgets_id,)).fetchone()
    price = gadget_being_bought.point_price
    difference = self.points - price
    if difference >= 0:
        self.points = difference
        self.update()
    else:
        pass

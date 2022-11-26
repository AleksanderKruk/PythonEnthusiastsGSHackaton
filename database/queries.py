from sqlite3 import connect
import database.schema.gadget as GD
import uuid
def get_all(table_name, con):
    return con.execute("SELECT * FROM ?;", (table_name,)).fetchall()


def buy_gadget(user, gadgets_id, con):
    gadget_being_bought = con.execute("SELECT * FROM gadgets WHERE id = ?;", (gadgets_id,)).fetchone()
    gadget_being_bought = GD.Gadget(uuid.UUID(gadget_being_bought[0]), gadget_being_bought[1], gadget_being_bought[2], gadget_being_bought[3])
    price = gadget_being_bought.point_price
    difference = user.points - price
    if difference >= 0:
        user.points = difference
        user.update()
    else:
        pass


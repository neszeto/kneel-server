import sqlite3
from models.metal import Metal

from models.order import Order
from models.size import Size
from models.style import Style


ORDERS = [
    {
        "id": 1, 
        "metalId": 3,
        "sizeId": 2, 
        "styleId": 3,
        "timestamp": 1614659931693
    }
]


def get_all_orders():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn: 
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            o.*,
            m.*,
            si.*,
            st.*
        FROM Orders o 
        JOIN Metals m ON m.id = o.metal_id
        JOIN Sizes si ON si.id = o.size_id
        JOIN Styles st ON st.id = o.style_id
        """)

        orders = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            order = Order(row["id"], row["metal_id"], row["size_id"], row["style_id"], row["timestamp"])

            metal = Metal(row["id"], row["metal"], row["price"])

            size = Size(row["id"], row["carets"], row["price"])

            style = Style(row["id"], row["style"], row["price"])

            order.metal = metal.__dict__
            order.size = size.__dict__
            order.style = style.__dict__

            orders.append(order.__dict__)
            

    return orders

def get_single_order(id):

    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn: 
        conn.row_factory = sqlite3.Row
        db_cursor =conn.cursor()

        db_cursor.execute("""
        SELECT 
            o.*,
            m.*,
            si.*,
            st.*
        FROM Orders o 
        JOIN Metals m ON m.id = o.metal_id
        JOIN Sizes si ON si.id = o.size_id
        JOIN Styles st ON st.id = o.style_id
        WHERE o.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        order = Order(data["id"], data["metal_id"], data["size_id"], data["style_id"], data["timestamp"])

        metal = Metal(data["id"], data["metal"], data["price"])

        size = Size(data["id"], data["carets"], data["price"])

        style = Style(data["id"], data["style"], data["price"])


        order.metal = metal.__dict__
        order.size = size.__dict__
        order.style = style.__dict__

    return order.__dict__


def create_order(order):

    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn: 
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Orders
            (metal_id, size_id, style_id, timestamp)
        VALUES
            (?, ?, ?, ?); 
        """, (order["metal_id"], order["size_id"], order["style_id"], order["timestamp"], ))

        id = db_cursor.lastrowid

        order["id"] = id

    return order


def delete_order(id):

    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Orders
        WHERE id = ?
        """, (id, ))



def update_order(id, new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Orders
            SET
                metal_id = ?,
                size_id = ?,
                style_id = ?,
                timestamp = ?
        WHERE id = ?
        """, (new_order["metal_id"], new_order["size_id"], new_order["style_id"], new_order["timestamp"], id, ))

        rows_affected = db_cursor.rowcount

        if rows_affected == 0:
            return False
        else: 
            return True
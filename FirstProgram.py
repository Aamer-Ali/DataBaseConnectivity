import sqlite3

# Global Variable for Table Name to avoid mistakes in string
TABLE_STORE = "tbl_store"
COL_ITEM = "item"
COL_QUNTITY = "quantity"
COL_PRICE = "price"


def create_table():
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS {} ({} TEXT, {} INTEGER, {} REAL)".format(TABLE_STORE, COL_ITEM, COL_QUNTITY,
                                                                              COL_PRICE))
    conn.commit()
    conn.close()


def insert_data(item, quntity, price):
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO {} VALUES (?,?,?)".format(TABLE_STORE), (item, quntity, price))
    conn.commit()
    conn.close()


def view_data():
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM {}".format(TABLE_STORE))
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_data(item):
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM {} WHERE {} = ?".format(TABLE_STORE, COL_ITEM), (item,))
    conn.commit()
    conn.close()


def update_date(item,quntity,price):
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE {} SET {} = ?,{} = ? WHERE {} = ?".format(TABLE_STORE, COL_QUNTITY, COL_PRICE, COL_ITEM),(quntity,price,item))
    conn.commit()
    conn.close()



print(view_data())

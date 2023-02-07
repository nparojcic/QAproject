import sqlite3 as sql

conn = sql.connect("ordersDatabase")
conn.execute("PRAGMA foreign_keys = 1 ")
cursor = conn.cursor()

def CreatingTable():
    sql_file = open("orders.sql")
    sql_string = sql_file.read()
    cursor.executescript(sql_string)

def selectQuery(query):
    return cursor.execute(query).fetchall()

def dataQuery(query):
    setupCursor.execute(query)
    return True

def commitChanges():
    conn.commit()



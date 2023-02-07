import sqlite3

def setupConn():
    conn = sqlite3.connect("ordersDatabase")
    conn.execute("PRAGMA foreign_keys = 1")
    return conn

def setupCursor():
    cursor = setupConn().cursor()
    return cursor

def CreatingTable():
    sql_file = open("orders.sql")
    sql_string = sql_file.read()
    setupCursor().executescript(sql_string)

def selectQuery(query):
    return setupCursor().execute(query).fetchall()

def dataQuery(query):
    setupCursor.execute(query)
    return True

def commitChanges():
    setupConn().commit()

setupConn()
setupCursor()
commitChanges()

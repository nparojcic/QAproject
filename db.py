# The DB file contains the processes and functions to create our Database or connect to it as well as run the initial SQL
# The DB file should also contain query functions that the Service file can use to read or modify the data

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

CreatingTable()

setupConn().commit() 
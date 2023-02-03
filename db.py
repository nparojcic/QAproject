# The DB file contains the processes and functions to create our Database or connect to it as well as run the initial SQL
# The DB file should also contain query functions that the Service file can use to read or modify the data

import sqlite3

def setupConn(orders):
    conn = sqlite3.connect(orders)
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()
    return conn, cursor




conn.commit() 
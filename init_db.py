#!/usr/bin/env python3
import sqlite3

from sqlite3 import Error

conn = None

try:
    conn = sqlite3.connect('dreamshop_dev.db')
    with open('schema.sql') as f:
        conn.executescript(f.read())
    print(sqlite3.version)
except Error as e:
    print(e)
finally:
    if conn:
        conn.close()

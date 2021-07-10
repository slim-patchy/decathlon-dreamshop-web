#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect('dreamshop_dev.db')

with open('dump.sql', 'w') as f:
    for line in conn.iterdump():
        f.write('%s\n' % line)

conn.close()

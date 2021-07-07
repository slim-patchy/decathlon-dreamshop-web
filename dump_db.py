import sqlite3

con = sqlite3.connect('dreamshop.db')

with open('dump.sql', 'w') as f:
    for line in con.iterdump():
        f.write('%s\n' % line)

con.close()

#!/usr/bin/python3
from sys import argv

import MySQLdb

# Ensure the arguments a 3"
if len(argv) != 4:
    print("Usage: python 0-select_states.py username password dbname")
    exit(1)

db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306)

c = db.cursor()
c.execute("SELECT id, name FROM states ORDER BY id")
rows = c.fetchall()
for row in rows:
    print(row)

c.close()
db.close()

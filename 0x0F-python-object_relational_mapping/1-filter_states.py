#!/usr/bin/python3
"""
    This Module contains a script for listing all states that
    starts with N
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Ensure the arguments a 3"
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306)

    c = db.cursor()
    c.execute("SELECT id, name FROM states WHERE name LIKE BINARY 'N%' \
              ORDER BY id")
    rows = c.fetchall()
    for row in rows:
        print(row)

    c.close()
    db.close()

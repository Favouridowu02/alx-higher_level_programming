#!/usr/bin/python3
"""
    This module contains a script that lists all cities
    from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            host="localhost",
            port=3306)
    c = db.cursor()
    c.execute("SELECT c.id, c.name, s.name FROM cities AS c INNER \
               JOIN states AS s ON s.id = c.state_id ORDER BY id")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()

#!/usr/bin/python3
"""
    This module contains a csript that takes in name of a state
    as an argument and lists all cities of that state, using
    the database hbtn_0e_4_usa
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
    match = argv[4]
    c.execute("SELECT c.name FROM cities AS c INNER JOIN \
               states AS s ON c.state_id = s.id WHERE s.name \
               = %s", (match,))
    rows = c.fetchall()
    temp = list(row[0] for row in rows)
    print(*temp, sep=", ")
    c.close()
    db.close()

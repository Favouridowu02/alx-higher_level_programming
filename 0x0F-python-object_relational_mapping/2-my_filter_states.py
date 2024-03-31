#!/usr/bin/python3
"""
    This module takes in four argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches the
    argument
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
    c.execute("SELECT id, name FROM states WHERE name LIKE
              BINARY '{}' ORDER BY id".format(argv[4]))

    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()

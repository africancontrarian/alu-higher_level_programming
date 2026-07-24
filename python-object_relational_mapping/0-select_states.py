#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa.

The script connects to a MySQL server on localhost using the username,
password and database name given as command line arguments, then prints
every row of the ``states`` table sorted by ``id``.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()

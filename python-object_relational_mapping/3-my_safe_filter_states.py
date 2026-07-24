#!/usr/bin/python3
"""Displays states matching a name argument, safe from SQL injection.

Unlike task 2, the state name is passed to ``execute`` as a bound
parameter, so the value can never alter the structure of the query.
Matching rows of the ``states`` table are printed sorted by ``id``.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC",
        (sys.argv[4],))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()

#!/usr/bin/python3
"""Displays states matching a name given as a command line argument.

This version builds the SQL query with ``str.format`` and is therefore
deliberately vulnerable to SQL injection; task 3 fixes that. Matching
rows of the ``states`` table are printed sorted by ``id``.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = ("SELECT * FROM states WHERE BINARY name = '{}' "
             "ORDER BY id ASC".format(sys.argv[4]))
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()

#!/usr/bin/python3
"""Lists all cities together with their state from hbtn_0e_4_usa.

A single ``JOIN`` query links the ``cities`` and ``states`` tables and
each resulting row ``(city id, city name, state name)`` is printed
sorted by ``cities.id``.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()

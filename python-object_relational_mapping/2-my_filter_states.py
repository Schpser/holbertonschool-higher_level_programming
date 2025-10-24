#!/usr/bin/python3
"""
Display states matching user input
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if (sys.argv) != 5:
        pass

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    query = "SELECT * FROM states.id WHERE name = '{}'"\
            "ORDER BY ASC".format(sys.argv[4])
    cur.execute(query)

    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    db.close()

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
        db=sys.argv[3],
        state_name=sys.argv[4]
    )

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}'"\
            " ORDER BY id ASC;".format(sys.argv[4])
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()

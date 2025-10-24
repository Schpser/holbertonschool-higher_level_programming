#!/usr/bin/python3
"""
List all cities of a state from the database
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT cities.name "
                "FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id",
                (sys.argv[4],))

    results = cur.fetchall()

    cities = [row[0] for row in results]
    print(", ".join(cities))

    cur.close()
    db.close()

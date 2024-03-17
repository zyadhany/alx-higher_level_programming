#!/usr/bin/python3
"""  list all element of table state """
import MySQLdb
import sys


if __name__ == "__main__":
    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=USER,
                         passwd=PASS, db=DB, port=3306)

    cur = db.cursor()

    cur.execute("""
        SELECT cities.name FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s;
    """, (sys.argv[4],))

    results = cur.fetchall()

    res = []

    for row in results:
        res.append(row[0])

    formatted_cities = ', '.join(city for city in res)
    print(formatted_cities)

    cur.close()
    db.close()

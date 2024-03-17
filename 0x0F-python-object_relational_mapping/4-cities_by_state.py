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

    cur.execute("""SELECT cities.id, cities.name, states.name AS state_name
                    FROM cities
                    INNER JOIN states ON cities.state_id = states.id;
                """)
    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()

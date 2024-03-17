#!/usr/bin/python3
import MySQLdb
import sys

USER = sys.argv[1]
PASS = sys.argv[2]
DB = sys.argv[3]


db = MySQLdb.connect(host='localhost', user=USER, passwd=PASS, db=DB, port=3306)

cur = db.cursor()

cur.execute("SELECT * FROM states")

results = cur.fetchall()

for row in results:
    print(row)

cur.close()
db.close()
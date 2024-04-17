#!/usr/bin/python3
"""Merges data from two tables and displays cities 
   along with their states"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities INNER JOIN states ON cities.state_id=states.id WHERE states.name = %s
                ORDER BY cities.id ASC""", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)

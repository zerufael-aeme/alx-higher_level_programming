#!/usr/bin/python3
"""Merges data from two tables and list cities that are 
   from the state passed in as an argument"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name\
                FROM cities LEFT JOIN states\
                ON cities.state_id=states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",port='3306' ,password=sys.argv[2],user=sys.argv[1],database=sys.argv[3])
cur = db.cursor()

cur.execute('Select * from states order by states.id ASC')
rows = cur.fetchall()
for row in rows:
    print(row)

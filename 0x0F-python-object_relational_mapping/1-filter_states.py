#!/usr/bin/python3
"""This module selects states that start with N """
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3], host="localhost", port=3306)
    cursor = db.cursor()
    cursor.execute("""select * from states where name like binary 'N%'
                    order by states.id ASC""")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()

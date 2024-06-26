#!/usr/bin/python3
"""This module selects states based on user input """
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3], host="localhost", port=3306)
    cursor = db.cursor()
    cursor.execute("""select * from states where name = '{}'
                    order by states.id ASC""".format(sys.argv[4]))
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()

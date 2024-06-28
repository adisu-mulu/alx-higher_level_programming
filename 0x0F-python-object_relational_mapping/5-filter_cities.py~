#!/usr/bin/python3
"""This module lists all cities """
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3], host="localhost", port=3306)
    cursor = db.cursor()
    cursor.execute("""select cities.id, cities.name, states.name
                     from cities inner join
                     states on states.id = cities.state_id""")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()

#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == '__main__':
    arg1 = sys.argv[1];
    arg2 = sys.argv[2];
    arg3 = sys.argv[3];

    db = MySQLdb.connect(host="localhost", user=arg1,
                         passwd=arg2, db=arg3, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

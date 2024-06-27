#!/usr/bin/python3
"""
we will develop a script that will list all the cities
from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    We will connect to a MySQL database 
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
    """
    We will use the cursor to help us execute SQL queries and start a Session
    """
    cur = db.cursor()
    cur.execute("SELECT * from cities JOIN states ON cities.state_id \
            = states.id ORDER BY cities.id ASC")
    results = cur.fetchall()

    for result in results:
        print(result)
    """
    We will close any connection we have to the database 
    """
    cur.close
    db.close()

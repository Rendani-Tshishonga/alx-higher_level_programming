#!/usr/bin/python3
"""
We will write a script that lists all states from the database hbtn_0e_0_usa
Import the module MySQLdb
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    We will pass command line arguments as input to database parameters
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=db_name)
    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)
    
    """
    The cursor function will help execute the ORM MySql scripts in python
    """

    cur = conn.cursor
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    results = cur.fetchall()

    for result in results:
        print(result)
    """
    The ORM will require us to close any open connections once we are done executing for this current Session
    """
    cur.close
    conn.close


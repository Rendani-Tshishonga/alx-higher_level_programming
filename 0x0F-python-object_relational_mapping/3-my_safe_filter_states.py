#!/usr/bin/python3
"""
Write a script that takes in argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argumwnt. Ensure that your script
is safe from MySQL injections
"""
import MySQLdb
import sys

if __name__ == "__main__":

    """
    We will try to connect to the database using command line arguments
    which will be passed in by the user
    """
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

    """
    We will use the cursor to execute SQL queries 
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %(name)s\
            ORDER BY states.id ASC", {'name': sys.argv[4]})
    results = cur.fetchall()

    for result in results:
        print(result)

    """
    We are required to close any connection to the database once we
    are done executing the queries
    """
    cur.close()
    conn.close()

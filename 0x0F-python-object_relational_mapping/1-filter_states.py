#!/usr/bin/python3

"""
Write a script that lists all states with a name starting with N (Upper N) from the database hbtn_0e_0_usa)
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    """
    We willl try to connect to the database except if there is an error 
    """

    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=db_name)
    except MySQLdb.Error as e:
        print("Error Connecting to database: {}".format(e))
        sys.exit(1)

    """
    We will use cursor to execute queries on the database
    """
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
    ORDER BY states.id ASC")
    results = cur.fetchall()

    for result in results:
        print(result)
    """
    We are required to close all connections to the database once we are done
    executing the queries
    """
    
    cur.close()
    conn.close()

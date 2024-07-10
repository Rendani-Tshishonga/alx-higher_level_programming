#!/usr/bin/python3
"""
We will write a script that is safe from MySQL injections which will take as 
argument command-line arguments tp display all values in the states table of the hbtn_0e_0_usa where 
name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
"""
We will try to connect to a MySQL database using 
command-line arguments and it will throw an error if there is a problem connecting to the server

"""

    try:
        conn = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))

    cur = conn.cursor()
    """
    We will need to execute the scripts in such a way that our code will not be prone to a 
    MySQL injection
    """
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
    ORDER BY states.id ASC".format(sys.argv[4]))
    results = cur.fetchall()
    """
    We will return the result from the results tuple once our results have been processed by the server for 
    this session of the execution.
    """
    for result in results:
        print(result)
    """
    We are required to close the any connections to the database using the close function
    """
    cur.close()
    conn.close()

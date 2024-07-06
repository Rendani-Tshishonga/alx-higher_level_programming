#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

"""
We will connect to a database using MySQLdb.connect()
"""
if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
"""
We will use the cursor function to connect to the database and execute SQL queries
"""
    cur = db.cursor()
"""
We will execute Sql queries using the execute function to fetch all cities 
with the state name passed in as an argument
"""
    cur.execute("SELECT citites.name FORM cities JOIN states ON \
            citites.state_id = state.id WHERE states.name LIKE BINARY %(state_name) \
            ORDER BY cities.id ASC", {'state_name':sys.argv[4]})
    results = cur.fetchall()
    
    for result in results:
        print(", ".join(result))
"""
We will close all the connections to the database once we have fetched all the results

"""
    db.close()
    cur.close()

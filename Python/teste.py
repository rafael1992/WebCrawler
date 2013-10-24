import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect( 'eduardosenac.db' )

    cur = con.cursor()
    cur.execute( 'Select ds_ip from sys_log' )

    data = cur.fetchone()

    print "SQLite version: %s" % data.nextval   

except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:
    if con:
        con.close();

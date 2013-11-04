import sqlite3 as lite
import sys


con = None

try:
    con = lite.connect('test.db')
    cursor = con.cursor()

    cursor.execute('SELECT SQLITE_VERSION()')
    data = cursor.fetchone()
    print "SQLite version: %s" % data

    # Create tables and add rows
    # pa table
    cursor.execute("DROP TABLE IF EXISTS pa")
    cursor.execute("CREATE TABLE pa (asia, p)")
    cursor.execute("INSERT INTO pa VALUES ('Y', '0.01')")
    cursor.execute("INSERT INTO pa VALUES ('N', '0.99')")

    # pta table
    cursor.execute("DROP TABLE IF EXISTS pta")
    cursor.execute("CREATE TABLE pta (tub, asia, p)")
    cursor.execute("INSERT INTO pta VALUES ('Y', 'Y', '0.05')")
    cursor.execute("INSERT INTO pta VALUES ('Y', 'N', '0.01')")
    cursor.execute("INSERT INTO pta VALUES ('N', 'Y', '0.95')")
    cursor.execute("INSERT INTO pta VALUES ('N', 'N', '0.99')")

    # ps table
    cursor.execute("DROP TABLE IF EXISTS ps")
    cursor.execute("CREATE TABLE ps (smoke, p)")
    cursor.execute("INSERT INTO ps VALUES ('Y', '0.50')")
    cursor.execute("INSERT INTO ps VALUES ('N', '0.50')")

    # pls table
    cursor.execute("DROP TABLE IF EXISTS pls")
    cursor.execute("CREATE TABLE pls (lc, smoke, p)")
    cursor.execute("INSERT INTO pls VALUES ('Y', 'Y', '0.10')")
    cursor.execute("INSERT INTO pls VALUES ('Y', 'N', '0.01')")
    cursor.execute("INSERT INTO pls VALUES ('N', 'Y', '0.90')")
    cursor.execute("INSERT INTO pls VALUES ('N', 'N', '0.99')")

    # pbs table
    cursor.execute("DROP TABLE IF EXISTS pbs")
    cursor.execute("CREATE TABLE pbs (bron, smoke, p)")
    cursor.execute("INSERT INTO pbs VALUES ('Y', 'Y', '0.60')")
    cursor.execute("INSERT INTO pbs VALUES ('Y', 'N', '0.30')")
    cursor.execute("INSERT INTO pbs VALUES ('N', 'Y', '0.40')")
    cursor.execute("INSERT INTO pbs VALUES ('N', 'N', '0.70')")

    # pxe table
    cursor.execute("DROP TABLE IF EXISTS pxe")
    cursor.execute("CREATE TABLE pxe (xray, elt, p)")
    cursor.execute("INSERT INTO pxe VALUES ('Y', 'Y', '0.98')")
    cursor.execute("INSERT INTO pxe VALUES ('Y', 'N', '0.05')")
    cursor.execute("INSERT INTO pxe VALUES ('N', 'Y', '0.02')")
    cursor.execute("INSERT INTO pxe VALUES ('N', 'N', '0.95')")

    # pelt table
    cursor.execute("DROP TABLE IF EXISTS pelt")
    cursor.execute("CREATE TABLE pelt (elt, lc, tub, p)")
    cursor.execute("INSERT INTO pelt VALUES ('Y', 'Y', 'Y', '1')")
    cursor.execute("INSERT INTO pelt VALUES ('Y', 'Y', 'N', '1')")
    cursor.execute("INSERT INTO pelt VALUES ('Y', 'N', 'Y', '1')")
    cursor.execute("INSERT INTO pelt VALUES ('Y', 'N', 'N', '0')")
    cursor.execute("INSERT INTO pelt VALUES ('N', 'Y', 'Y', '0')")
    cursor.execute("INSERT INTO pelt VALUES ('N', 'Y', 'N', '0')")
    cursor.execute("INSERT INTO pelt VALUES ('N', 'N', 'Y', '0')")
    cursor.execute("INSERT INTO pelt VALUES ('N', 'N', 'N', '1')")

    # pdeb table
    cursor.execute("DROP TABLE IF EXISTS pdeb")
    cursor.execute("CREATE TABLE pdeb (dys, elt, bron, p)")
    cursor.execute("INSERT INTO pdeb VALUES ('Y', 'Y', 'Y', '0.90')")
    cursor.execute("INSERT INTO pdeb VALUES ('Y', 'Y', 'N', '0.70')")
    cursor.execute("INSERT INTO pdeb VALUES ('Y', 'N', 'Y', '0.80')")
    cursor.execute("INSERT INTO pdeb VALUES ('Y', 'N', 'N', '0.10')")
    cursor.execute("INSERT INTO pdeb VALUES ('N', 'Y', 'Y', '0.10')")
    cursor.execute("INSERT INTO pdeb VALUES ('N', 'Y', 'N', '0.30')")
    cursor.execute("INSERT INTO pdeb VALUES ('N', 'N', 'Y', '0.20')")
    cursor.execute("INSERT INTO pdeb VALUES ('N', 'N', 'N', '0.90')")

    # Commit changes
    con.commit()

except lite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)
finally:
    if con:
        con.close()

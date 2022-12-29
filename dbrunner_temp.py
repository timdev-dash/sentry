from dbmanager import Database
import sqlite3

test_database = Database('testdb.sqlite')


test_database.db_execute('INSERT INTO table_test VALUES (More Testing)')
test_database.close()
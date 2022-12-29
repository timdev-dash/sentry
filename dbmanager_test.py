import unittest
import sqlite3
from dbmanager import Database

class TestDatabaseClass(unittest.TestCase):
    
    def setUp(self):
        self.test_database = Database('testdb.sqlite')
        create_name = 'table_test'
        create_data = ['header1_test TEXT',]
        self.test_database.db_create(create_name, create_data)
        insert_name = 'table_test'
        insert_text = ['More Testing',]
        self.test_database.db_insert(insert_name, insert_text)


    ## 1. Returns true if Database returns a Database
    def test_database_creation(self):
        test_database1 = Database('testdb1.sqlite')
        type_string = str(type(test_database1))
        self.assertEqual(type_string, "<class 'dbmanager.Database'>")
    
    ## 2. Returns true if the saved name of the database is the same as the one provided to the __init__
    def test_database_name(self):
        test_name = 'testdb2.sqlite'
        test_database2 = Database(test_name)
        self.assertEqual(test_name, test_database2.file_name)
    
    ## 3. Returns true if the execute function creates a table with the correct table name
    def test_execute_create_table_name(self):
        test_query3 = "CREATE TABLE IF NOT EXISTS test_table (test_header1 TEXT, test_header2 INTEGER)"
        self.test_database.db_execute(test_query3)
        data3 = sqlite3.connect('testdb.sqlite')
        cursor = data3.cursor()
        test_result3 = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        test_value3 = test_result3.fetchall()[0][0]
        self.assertEqual('test_table', test_value3)
        data3.commit()
        data3.close()

    ## 4. Returns true if the execute function creates a table with the correct header name
    def test_execute_create_table_header1(self):
        data4 = sqlite3.connect('testdb.sqlite')
        cursor = data4.cursor()
        header_list = cursor.execute("PRAGMA table_info(test_table)")
        header_1 = cursor.fetchone()
        header_2 = cursor.fetchone()
        self.assertEqual('test_header1', header_1[1])
        data4.commit()
        data4.close()

    ## 5. Returns true if the execute function creates a table with the correct header name    
    def test_execute_create_table_header2(self):
        data5 = sqlite3.connect('testdb.sqlite')
        cursor = data5.cursor()
        header_list = cursor.execute("PRAGMA table_info(test_table)")
        header_1 = cursor.fetchone()
        header_2 = cursor.fetchone()
        self.assertEqual('test_header2', header_2[1])
        data5.commit()
        data5.close()

    ## 6. Returns true if the execute function inserts into a table with the correct data
    def test_execute_insert1(self):
        test_query6 = "INSERT INTO test_table VALUES ('Testing', 1234)"
        self.test_database.db_execute(test_query6)
        data6 = sqlite3.connect('testdb.sqlite')
        cursor = data6.cursor()
        test_result6 = cursor.execute('SELECT test_header1 FROM test_table').fetchone()[0]
        self.assertEqual('Testing', test_result6)
        data6.commit()
        data6.close()

    ## 7. Returns true if the execute function inserts into a table with the correct data
    def test_execute_insert2(self):
        data7 = sqlite3.connect('testdb.sqlite')
        cursor = data7.cursor()
        test_result7 = cursor.execute('SELECT test_header2 FROM test_table').fetchone()[0]
        self.assertEqual(1234, test_result7)
        data7.commit()
        data7.close()

    ## 8. Returns true if the create function creates a table with the correct table name
    def test_create_table_name(self):
        data8 = sqlite3.connect('testdb.sqlite')
        cursor = data8.cursor()
        test_result8 = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';") 
        name_1 = test_result8.fetchone()[0]
        name_2 = test_result8.fetchone()[0]
        self.assertEqual('table_test', name_2)
        data8.commit()
        data8.close()
    
    ## 9. Returns true if the create function creates a table with the correct header name
    def test_create_table_header(self):
        data9 = sqlite3.connect('testdb.sqlite')
        cursor = data9.cursor()
        header_list = cursor.execute("PRAGMA table_info(table_test)")
        header_1 = cursor.fetchone()
        self.assertEqual('header1_test', header_1[1])
        data9.commit()
        data9.close() 

    ## 10. Returns true if the insert function inserts into at table with the correct data as text
    def test_insert_data_text(self):
        data10 = sqlite3.connect('testdb.sqlite')
        cursor = data10.cursor()
        test_result10 = cursor.execute('SELECT header1_test FROM table_test').fetchone()[0]
        self.assertEqual('More Testing', test_result10)
        data10.commit()
        data10.close()
    
    ## 11. Returns true if the insert function inserts into a table with the correct data as integers
    def test_insert_data_number(self):
        test11_database = Database('testdb11.sqlite')
        test11_table = 'test11_table'
        test11_header = ['test11_int_header INTEGER',]
        test11_int = ['4321',]
        test11_database.db_create(test11_table, test11_header)
        test11_database.db_insert(test11_table, test11_int)
        data11 = sqlite3.connect('testdb11.sqlite')
        cursor = data11.cursor()
        test_result11 = cursor.execute('SELECT test11_int_header FROM test11_table').fetchone()[0]
        self.assertEqual(4321, test_result11)
        data11.commit()
        data11.close()


### Makes sure the unittests run, important!!! ###
if __name__ == "__main__":
    unittest.main()

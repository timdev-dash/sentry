'''Database manager for webhooks

Details the Database class and provides the tools to update/modify the databases used for receiving/parsing webhooks'''

import sqlite3


class Database():
    '''Database class for webhooks
    
    Attributes:
        file_name(str): The name of the file for the database
    '''

    ### Setting up the file_name for the class ###
    file_name = ""

    ### Creating the initialization method for the Database class ###
    def __init__(self, name: str):
        ''' The __init__ method of the Database class
        
        Parameters:
            name(str): The file_name to be used for the database
        '''

        self.file_name = name

        ### Creating the Database file for use and closing the connection ###
        data = sqlite3.connect(self.file_name)
        data.close()

    ### Creating the db_execute method for the Database using a provided query ###
    def db_execute(self, query: str):
        ''' The db_execute method for the Database class
        
        Parameters:
            query(str): The string containing the query being sent to the database
        '''

        ### Opening a connection to the Database and creating a cursor ###
        data = sqlite3.connect(self.file_name)
        cursor = data.cursor()

        ### Executing the provided query ###
        cursor.execute(query)

        ### Committing the changes and closing the Database ###
        data.commit()
        data.close()

    ### Creating the 'create' method for the Database using a provided name and a list headers ###
    def db_create(self, table_name: str, table_headers: list):
        ''' The db_create method for the Database class
        
        Parameters:
            table_name(str): The name of the table to create in the database
            table_headers(list): The headers and their data types for the table
        '''

        ### Starting the create statement to be sent to the database ###
        cq = "CREATE TABLE IF NOT EXISTS "
        cq += table_name + " ("

        ### Error checking that the list has at least 1 entry ###
        if len(table_headers) < 1:
            raise ValueError("The list of headers has no headers in it")
        else:
            ### Adds the headers and their types to the create statement ###
            i = 0
            while i < len(table_headers):
                cq += table_headers[i] 
                if i == len(table_headers) - 1:
                    pass
                else: 
                    cq += ', '
                i += 1
        
        ### Closes out the create statement with the final text ###
        cq += ")"

        ### Sends the query to the db_execute method to run the query ###
        self.db_execute(cq)
 
    ### Creating the insert method for the Database for single items, using a list of data ###
    def db_insert(self, table_name: str, insert_data: list):
        ''' The db_insert method for the Database class
        
        Parameters:
            table_name(str): The name of the table to add the data to
            insert_data(list): The list of items to add to the table'''

        ### Starting the insert statement to be sent to the database table ###
        iq = "INSERT INTO "
        iq += table_name + " VALUES ("

        ### Error checking that the list has at least 1 entry ###
        if len(insert_data) < 1:
            raise ValueError("The list of data has no data in it")
        else:
            ### Adds the table data to the insert statement ###
            i = 0
            while i < len(insert_data):
                iq += insert_data[i]
                if i == len(insert_data) - 1:
                    pass
                else:
                    iq += ', '
                i += 1
            
        ### Closes out the insert statement with final text ###
        iq += ")"

        ### Sends the query to the db_execute method to run the query ###
        self.db_execute(iq)

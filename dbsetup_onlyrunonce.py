'''Setup file for databases to be used for sentry

Only run when creating new databases, being kept as a record of the structure built out
'''

from dbmanager import Database

### The catering_in Database setup ###
def catering_in():
    ''' The method to create the catering_in Database

    The webhooks sent in to the catering_in Database will be raw JSON payloads. The 
    intention is for the catering_in Database to hold them until processed and added 
    to an additional Database build out for parsed JSON data. Once operational, this
    Database would only hold the messages until processing.
    '''    
    
    ### The database file name should be catering_in.sqlite ###
    db_name = 'catering_in.sqlite'

    ### There will only be one table in the database containing the text of the complete JSON ###
    ### payload sent from OLO. The table name will be incoming, the header name will be payload ###
    ### and the data type will be text. ###

    table_name = 'Incoming'
    header1 = 'Header TEXT'
    header2 = 'Payload TEXT'

    ### Creates the database file for use ###
    db = Database(db_name)

    ### Creates the table for use ###
    db.db_create(table_name, [header1, header2])

"""
### The online_in Database setup
def online_in():
    ''' The method to create the online_in Database

    The webhooks sent in to the online_in Database will be raw JSON payloads. The 
    intention is for the online_in Database to hold them until processed and added 
    to an additional Database build out for parsed JSON data. Once operational, this
    Database would only hold the messages until processing.
    '''    
    
    ### The database file name should be online_in.sqlite ###
    db_name = 'online_in.sqlite'

    ### There will only be one table in the database containing the text of the complete JSON ###
    ### payload sent from OLO. The table name will be incoming, the header name will be payload ###
    ### and the data type will be text. ###

    table_name = 'Incoming'
    header1 = 'Payload TEXT'

    ### Creates the database file for use ###
    db = Database(db_name)

    ### Creates the table for use ###
    db.db_create(table_name, [header1,])
"""
if __name__ == "__main__":
    #online_in()
    catering_in()

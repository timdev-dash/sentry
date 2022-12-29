from flask import Flask, jsonify, request
from dbmanager import Database

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey123"

@app.route("/")  # this sets the route to this page
def home():
        return jsonify({'Message': "Testing1"})

@app.route("/catering", methods=['POST', 'GET']) # creating reception point for catering webhooks
def catering_receipt():
        ## Setting default database settings for insert functions
        db_name = 'catering_in.sqlite'
        table_name = 'Incoming'
        db = Database(db_name)

        ## Setting logic to receive and file received webhooks 
        if request.method == 'POST':
                text_to_insert = str(request.json)
                db.db_insert(table_name, [text_to_insert,])
                
                ### Sending the required HTTP 200 response communicating receipt of webhook
                return '', 200
        elif request.method == 'GET':
                return 'Test Succesful', 201



@app.route("/monitor", methods=['POST']) # creating receotpion point for mealtime webhooks
def monitor_receipt():
        ## Setting default database settings for insert functions
        db_name = 'online_in.sqlite'
        table_name = 'Incoming'
        db = Database(db_name)

        ## Setting logic to receive and file received webhooks 
        if request.method == 'POST':
                text_to_insert = str(request.json)
                db.db_insert(table_name, [text_to_insert,])
                
                ### Sending the required HTTP 200 response communicating receipt of webhook
                return '', 200

if __name__ == "__main__":
    app.run()

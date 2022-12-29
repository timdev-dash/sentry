from flask import Flask, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey123"

@app.route("/")  # this sets the route to this page
def home():
        return jsonify({'Message': "Testing1"})

@app.route("/catering") # creating reception point for catering webhooks
def catering_receipt():
        pass

@app.route("/monitor") # creating receotpion point for mealtime webhooks
def monitor_receipt():
        pass

if __name__ == "__main__":
    app.run()

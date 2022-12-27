'''A script to listen for webhooks and properly reply'''

from Flask import Flask, request, abort
import json

app = Flask(__name__)

@app.route('/catering', methods=['POST'])
def webhook():
    pass

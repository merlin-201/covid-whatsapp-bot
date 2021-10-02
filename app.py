from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/',methods=["GET"])
def hello():
    return "hello there"

initiated = False

def write_suffix(msg):
    with open('suffix.txt', 'w') as f:
        f.write(f"\n{msg}")

def read_suffix():
    with open('suffix.txt', 'r') as f:
        suffix = f.read()
    return suffix

def add_field(key, value):
    with open('data.json',)as f:
        data = json.load(f)
    
    data[key]=value

    with open('data.json', 'w') as f:
        json.dump(data, f)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '')
    incoming_msg = read_suffix() + incoming_msg
    resp = MessagingResponse()
    msg = resp.message()

    responded = False
    if incoming_msg == "test":
        msg.body("Working")

    if incoming_msg == "/bed":
        msg.body('''
        Hello, Welcome to the Covid bed allocation helpline.
        Please provide me your basic details :
        ''')
        write_suffix('/name')

    if '/name' in incoming_msg:
        name = incoming_msg[5:]
        add_field('name',name)
        msg.body('''
        Name Added\n\nSend me your contact number..
        ''')
        write_suffix('/contact')
    
    if '/contact' in incoming_msg:
        contact = incoming_msg[8:]
        add_field('contact',contact)
        msg.body('''
        Contact Added\n\n
        ''')

    return str(resp)

@app.route('/data', methods=['GET'])
def get_data():
    with open('data.json',)as f:
        data = json.load(f)
    
    return jsonify(data)



if __name__ == '__main__':
    app.run()
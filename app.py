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

def write_log(msg):
    with open('logs.txt', 'a') as f:
        f.write(f"\n{msg}")

def add_field(key, value):
    with open('data.json',)as f:
        data = json.load(f)
    
    data[key]=value

    with open('data.json', 'w') as f:
        json.dump(data, f)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()

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
        write_log("Prompt Given")

    if '/name' in incoming_msg:
        name = incoming_msg[5:]
        add_field('name',name)
        msg.body('''
        Name Added\n\nSend me your contact number..
        ''')
    
    if '/contact' in incoming_msg:
        contact = incoming_msg[8:]
        add_field('contact',contact)
        msg.body('''
        Contact Added\n\nSend me your aadhar number
        ''')


    return str(resp)

@app.route('/data', methods=['GET'])
def get_data():
    with open('data.json',)as f:
        data = json.load(f)
    
    return jsonify(data)



if __name__ == '__main__':
    app.run()
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from flask import jsonify
import json
from database import upload_json

app = Flask(__name__)


@app.route('/',methods=["GET"])
def hello():
    return "hello there"


def write_suffix(msg):
    with open('suffix.txt', 'w') as f:
        f.write(f"\n{msg}")

def read_suffix():
    with open('suffix.txt', 'r') as f:
        suffix = f.read()
    return suffix

def clear_json():
    with open('data.json',) as f:
        empty = {}
        json.dump(empty,f)

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

    if incoming_msg == "test":
        msg.body("Working")

    if incoming_msg == "/bed":
        clear_json()
        msg.body('''
        Hello, Welcome to the Covid bed allocation helpline.\nPlease provide me your name :
        ''')
        write_suffix('/name')

    if '/name' in incoming_msg:
        name = incoming_msg[6:]
        add_field('name',name)
        msg.body('''
        Name Added\n\nSend me your contact number..
        ''')
        write_suffix('/contact')
    
    if '/contact' in incoming_msg:
        contact = incoming_msg[9:]
        add_field('contact',contact)
        with open('data.json',)as f:
            data = json.load(f)
        msg.body(
        f'Contact Added\n Type "confirm" if these are your details : \nName : {data["name"]}\nContact : {data["contact"]}'
        )
        write_suffix("")

    if "confirm" in incoming_msg:
        upload_json()
        msg.body('''
        Your details have been succesfully uploaded\n\nOur Call Team will reach out to you soon
        ''')

    return str(resp)

@app.route('/data', methods=['GET'])
def get_data():
    with open('data.json',)as f:
        data = json.load(f)
    
    return jsonify(data)



if __name__ == '__main__':
    app.run()
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/',methods=["GET"])
def hello():
    return "hello there"

initiated = False

def write_log(msg):
    with open('logs.txt', 'a') as f:
        f.write(f"\n{msg}")

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
    if initiated:
        name, contact, aadhar = incoming_msg.split().apply(lambda s:s.strip())
        msg.body(f'''
        Your details are as follows :\n
        Name : {name}\n
        Contact : {contact}\n
        Aadhar : {aadhar}
        ''')
        responded = True
    return str(resp)

@app.route('/logs', methods=['GET'])
def logs():
    with open('logs.txt','r') as f:
        logs = f.readlines()
        return logs



if __name__ == '__main__':
    app.run()
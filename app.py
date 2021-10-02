from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/',methods=["GET"])
def hello():
    return "hello there"

initiated = False


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    global initiated
    responded = False
    if incoming_msg == "test":
        msg.body("Working")
    if '/need_a_bed' in incoming_msg:
        msg.body('''
        Hello, Welcome to the Covid bed allocation helpline.
        Please provide me your basic details :
        ''')
        initiated = True
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


if __name__ == '__main__':
    app.run()
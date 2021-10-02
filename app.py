from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/',methods=["GET"])
def hello():
    return "hello there"


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if '/need_a_bed' in incoming_msg:
        msg.body('''
        Hello, Welcome to the Covid bed allocation helpline.
        \n\nPlease provide me your basic deatils in the following format :\n
        Full Name,contact number,12-digit aadhar card
        ''')
        responded = True
    if 'rahul' in incoming_msg:
        msg.body("neha bhabhi kidhar hain")
        responded = True
    if not responded:
        msg.body('kya re rahul')
    return str(resp)


if __name__ == '__main__':
    app.run()
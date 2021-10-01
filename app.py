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
    if 'hi' in incoming_msg:
        msg.body("what is your name ?")
        responded = True
    if 'rahul' in incoming_msg:
        msg.body("neha bhabhi kidhar hain")
        responded = True
    if not responded:
        msg.body('kya re rahul')
    return str(resp)


if __name__ == '__main__':
    app.run()
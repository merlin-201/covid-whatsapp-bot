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
    if 'cat' in incoming_msg:
        msg.body("Meow Meow")
        responded = True
    if 'dog' in incoming_msg:
        msg.body("Woof Woof")
        responded = True
    if not responded:
        msg.body('i hate humans')
    return str(resp)


if __name__ == '__main__':
    app.run()
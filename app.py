from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


def get_reply(message):
    
    message = message.lower()
    reply_text = ''
    if "google" in message:
        message = message.replace("google ","")
        reply_text = "getting results for {}".format(message)
    elif "directions from" and "to" in message:
        removal_list = ["directions ","from ","to "]
    
        for word in removal_list:
            message = message.replace(word, "")
        message = message.split()
        origin = message[0]
        destination = message [1]
        reply_text = "finding directions from your curret location of {} to {}".format(origin,destination)
    else:
        reply_text = "i can only google and provied direction as of right now"

    return reply_text


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    
    message_body = request.form['Body']
    resp = MessagingResponse()


    reply_text = get_reply(message_body)
    print(reply_text)
    
    resp.message(reply_text)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

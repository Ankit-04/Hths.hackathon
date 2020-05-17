from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import directions as map
import search as search
import area_result as find


def get_reply(message):
    
    message = message.lower()
    reply_text = ""

    if "google" in message:
        message = message.replace("google ","")
        return search.google_search(message)
    
    elif "directions from" and "to" in message:
        removal_list = ["directions ","from ","to "]
    
        for word in removal_list:
            message = message.replace(word, "")
        message = message.split()
        origin = message[0]
        destination = message [1]
        return map.get_directions(origin,destination)
    
    elif "search" in message:
        message = message.replace("search ","")
        return search.wiki_search(message)

    elif "find" in message:
        removal_list = ["find ","meters ","near "]
        for word in removal_list:
            message = message.replace(word, "")
        message = message.split()
        address = "{}%{}%{}".format(message[2],message[3],message[4])

        return find.locations_around(address,message[1],message[0])
    
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
    #Use for production
    app.run(debug=True)



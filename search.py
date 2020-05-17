import wikipedia
from googlesearch import search 

def google_search(query):
    reply_text = ""
    
    for link in search(query, tld="co.in", num=10, stop=10, pause=2): 
        reply_text += link + "\n\n"
    return reply_text

def wiki_search(message):
    try:
        reply_text = wikipedia.summary(message)
    except:
        google_search(message)
    return reply_text

import requests 
import json
import html
import re

def cleanhtml(raw_html):
  
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def get_directions(origin,destination):
    origin = origin.replace(" ","+")
    destination = destination.replace(" ","+")
    
    with open('creds.json') as f:
        data =  (json.load(f))
    request = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin={}&destination={}&key={}'.format(origin,destination,data["google_map_key"]))
   
    requestJsonText = json.loads(request.text)
    steps = requestJsonText["routes"][0]["legs"][0]["steps"]
    step_string = ''

    for step in steps:
        step_string += html.unescape(step['html_instructions'])
        step_string +=  "\n\n"
    
    directions = cleanhtml(step_string)
    return directions






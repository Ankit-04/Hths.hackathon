import requests
import json

with open('creds.json') as f:
        data =  (json.load(f))
address = 'new%jersy'
response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(address,data["google_map_key"]))


resp_json_payload = response.json()

print(resp_json_payload['results'][0]['geometry']['location']['lng'])
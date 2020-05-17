import requests, json

def get_latitude(origin):
    with open('creds.json') as f:
        data =  (json.load(f))

    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(origin,data["google_map_key"]))


    resp_json_payload = response.json()

    latitude = resp_json_payload['results'][0]['geometry']['location']['lat']
    return latitude

def get_longitude(origin):
    with open('creds.json') as f:
        data =  (json.load(f))
    
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(origin,data["google_map_key"]))


    resp_json_payload = response.json()

    longitude = resp_json_payload['results'][0]['geometry']['location']['lng']    
    return longitude


def locations_around(origin, raduis,place_type):
    origin = origin.replace(" ","%")
    with open('creds.json') as f:
            data =  (json.load(f))

    api_key = data["google_map_key"]

    latitude = get_latitude(origin)
    longitude = get_longitude(origin)

    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&type={}&key={}'.format(latitude,longitude,raduis,place_type,api_key)
    response = requests.get(url)

    resp_json_payload = response.json()
    locations = resp_json_payload['results']
    restaurants = ''
    for location in locations:
        restaurants += '\n'+location['name'] +'\n'
    return restaurants
    

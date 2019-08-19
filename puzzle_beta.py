import requests
import json
import base64

#The URL to be used the base
baseUrl = 'http://fasttrack.herokuapp.com'

#The main function to make the calls to the x amount of pages
def fetch(link):
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    #Looking for the /auth page
    if link.endswith("/auth"):
        #passing the username and password in a base64 format
        headers ["authorization"] = "Basic " + base64.b64encode(b"ATRR:PORR").decode("UTF-8")
    r = requests.get(link, headers=headers)
    jsonResponse = (json.loads(r.content.decode("UTF-8")))
    #For debugging purposes
    print(link)
    print (jsonResponse)
    print (headers)
    fetch(baseUrl + jsonResponse['next'])

fetch(baseUrl)

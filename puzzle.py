import requests
import json
import base64

#The URL to be used the base
baseUrl = 'http://fasttrack.herokuapp.com'

#The main function to make the calls to the x amount of pages
def fetch(link, content_type="application/json"):
    headers = {'Content-Type': content_type, 'Accept': content_type}
    #Looking for the /auth page
    if link.endswith("/auth"):
        #passing the username and password in a base64 format
        headers ["authorization"] = "Basic " + base64.b64encode(b"ATRR:PORR").decode("UTF-8")
    r = requests.get(link, headers=headers)
    #Trying to parse the decoded content however if unable priting the content of the request and quitting
    try:
        jsonResponse = (json.loads(r.content.decode("UTF-8")))
    except:
        print ("Another test " + link)
        print (r.content)
        quit()
    #For debugging purposes
    print(link)
    print (jsonResponse)
    print (headers)
    #Looking for the page that needs to be printed as html
    if jsonResponse["next"] == "Try this page in html":
        fetch(link, "text/html")
    else:
        fetch(baseUrl + jsonResponse['next'])

fetch(baseUrl)

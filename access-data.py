#load dependencies

import os as os
import sys as sys
import pandas as pd
import freesound 
import requests as requests

#set project working directory

os.chdir(os.path.dirname(sys.argv[0]))
print(os.getcwd())


#test api with requests library

path = 'private/api-key.txt'

keyfile = open(path, "rt")

key = keyfile.read()

key = key.rstrip("\n")

keyfile.close()

url = "https://freesound.org/apiv2/search/text"

payload = {'query': 'piano', 'token': key}

resp = requests.get(url, params = payload)

##check for successful request 

print(resp)


#test api with freesound library

client = freesound.FreesoundClient()
client.set_token(key,"token")

results = client.text_search(query="piano",fields="id,name,preview")

#list basic query results of first 15 with piano in query

for sound in results:
    #sound.retrieve_preview(".",sound.name+".mp3")
    print(sound.name)

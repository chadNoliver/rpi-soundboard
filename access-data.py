import os as os
import sys as sys
import pandas as pd

import requests as requests

os.chdir(os.path.dirname(sys.argv[0]))
print(os.getcwd())

path = 'private/api-key.txt'

keyfile = open(path, "rt")

key = keyfile.read()

keyfile.close()

url = "https://freesound.org/apiv2/search/text/?query=piano&token="
urlkey = url + key
resp = requests.get(urlkey)




 

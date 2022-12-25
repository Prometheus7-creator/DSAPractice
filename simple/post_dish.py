import os
import requests
import json
path = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\Nosh_Recipes-main"
url = "https://a5morsuyy6.execute-api.ap-south-1.amazonaws.com/dev/dish"
for file in os.listdir(path):
    for i in os.listdir(os.path.join(path,file)):
        try:
            if i.split('.')[1].lower()=='json':
                f = open(os.path.join(path, file, i))
                d = f.read().strip()
                obj =  json.loads(d)
                x = requests.post(url, json=obj)
                print(x.text)
        except:
            pass
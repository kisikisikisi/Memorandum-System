import requests
import os
import json
from time import sleep

def create_thumbnail(file):
    for i in range(len(file)):
        url = "https://s.wordpress.com/mshots/v1/" + str(file[i]["url"])
        try:
            res = requests.get(url)
            for j in range(10):
                if not "jpeg" in res.headers['Content-Type']:
                    res = requests.get(url)
                    sleep(10)
                else:
                    break
        except:
            continue
        #print(res.headers['Content-Type'],i)
        save_image(file)

def save_image(file)
    with open("/create-chunk/history/idata/"
            + str(file[i]["id"]) + "t.jpeg", 'wb') as output_file:
        output_file.write(res.content)

if __name__ == "__main__":
    json_open = open('history/history.json', 'r', encoding='utf8')
    json_load = json.load(json_open)
    create_thumbnail(json_load)

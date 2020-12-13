import requests
import os
import json
from time import sleep

json_open = open('history/history.json', 'r', encoding='utf8')
json_load = json.load(json_open)

def judge_jpeg(url):
    for j in range(10):
        if "jpeg" in res.headers['Content-Type']:
            return True
        sleep(10)

for i in range(len(json_load)):
    url = "https://s.wordpress.com/mshots/v1/" + str(json_load[i]["url"])
    # Responseオブジェクトの生成
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
    # レスポンスの中身（最初の200文字）
    print(res.headers['Content-Type'],i)
    
    with open("/create-chunk/history/idata/"
              + str(json_load[i]["id"]) + "t.jpeg", 'wb') as f:
        f.write(res.content)

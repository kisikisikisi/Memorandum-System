import json
import random

json_open = open('history/history.json', mode='r', encoding='utf8')
json_load = json.load(json_open)
ls = []
for i in range(len(json_load)):
    ls.append(i)

if len(json_load) <= 100:
    exit()

choice_ls = random.sample(ls, 100)

with open('history/history.json', mode='w') as f:
    f.write('[')
    for di in choice_ls:
        print("selected id:{}".format(di))
        json.dump(json_load[di], f, indent=4)
        if di != choice_ls[-1]:
            f.write(",")
    f.write(']')

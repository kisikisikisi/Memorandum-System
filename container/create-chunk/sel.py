import json
import random

def select_history(history):
    json_open = open(history, mode='r', encoding='utf8')
    json_load = json.load(json_open)
    if len(json_load) <= 100:
        exit()
        
    ls = [i for i in range(len(json_load))]
    choice_ls = random.sample(ls, 100)

    with open(history, mode='w') as f:
        f.write('[')
        for di in choice_ls:
            print("selected id:{}".format(di))
            json.dump(json_load[di], f, indent=4)
            if di != choice_ls[-1]:
                f.write(",")
        f.write(']')

if __name__ == "__main__":
    select_history('history/history.json')

import re
import os
import pathlib
from pathlib import Path

topic = []
with open('topic.txt', mode='r', encoding='utf8') as f:
    for i in f.readlines():
        topic.append(i)
topic = str(topic)

def thresh(topic):
    flag = False
    global di
    for i in range(len(topic)):
        if flag == True:
            if topic[i] == '[':
                flag = False
                di = ''.join(tmp)
            else:
                tmp.append(topic[i])
        if topic[i] == ':':
            tmp = []
            flag = True
    #print(di)
    topic = topic[0:20].replace(di,'')+topic[20:]
    return topic.replace('id:','')
    
def thresh2(topic):
    return re.split('[,]', topic)

def make_topic_list(ls2):
    topic_ls = []
    for i in range(len(ls2)):
        if i % 2 == 0:
            per = ls2[i].replace(']','').replace('[','').replace(' ','').replace("'",'').replace('d:','')
        else:
            num = ls2[i].replace(']','').replace('[','').replace(' ','').replace('i','')
            topic_ls.append([per, num])

    for i in range(len(topic_ls)):
        topic_ls[i][0] = float(topic_ls[i][0])

    topic_ls = sorted(topic_ls, reverse=True)

    topic_ls2 = []
    for i in range(len(topic_ls)):
        if topic_ls[i][0] < 0.01:
            break
        else:
            topic_ls2.append(topic_ls[i])
    return topic_ls2

def write_idata(topic_ls):
    sx = 5
    with open("visicon/idata/"+di+"T.lisp", mode='w', encoding='utf8') as f:
        f.write("(setf *image-struct* '" + '(("' + di + 'T" ' + '10 10 10 10 BLUE)' + '\n')
        for i in range(len(topic_ls)):
            for j in range(int(topic_ls[i][0]//0.01)):
                f.write('("topic' + topic_ls[i][1] + '" ' + '5 5 '+str(sx)+' 400 GREEN)\n')
                sx += 5
        f.write("))")

check = 0
check2 = 2
di = ""
ls = []
print(len(topic))
for i in range(len(topic)):
    ls.append(topic[i])
    if topic[i] == 'i':
        check += 1
    if check == check2:
        check2 += 1
        ls = ''.join(ls)
        ls = thresh(ls)
        ls2 = thresh2(ls)
        topic_ls = make_topic_list(ls2)
        write_idata(topic_ls)
        ls = []


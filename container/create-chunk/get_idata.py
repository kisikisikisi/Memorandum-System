import re
import os

def create_idata(topic_file):
    """ターゲットページの情報を書き込み"""
    topic_ls = []
    for line in topic_file.readlines():
        topic_ls.append(line)
    topic_ls = str(topic_ls)

    topic_ls = re.split('\\[|\\]|,', topic_ls)
    topics = []
    for i in range(len(topic_ls)):
        try:
            if float(topic_ls[i]) > 0.01 and float(topic_ls[i+1]):
                print(topic_ls[i], topic_ls[i+1])
                topics.append([topic_ls[i], topic_ls[i+1]])
        except:
            continue
    write_idata(topics)

def write_idata(topic_ls):
    sx = 5
    with open("visicon/idata/"+di+"T.lisp", mode='w', encoding='utf8') as f:
        f.write("(setf *image-struct* '" + '(("' + di + 'T" ' + '10 10 10 10 BLUE)' + '\n')
        for i in range(len(topic_ls)):
            for j in range(int(topic_ls[i][0]//0.01)):
                f.write('("topic' + topic_ls[i][1] + '" ' + '5 5 '+str(sx)+' 400 GREEN)\n')
                sx += 5
        f.write("))")

if __name__ == "__main__":
    topic = []
    with open('topic.txt', mode='r', encoding='utf8') as topic_file
        create_idata(topic_file)

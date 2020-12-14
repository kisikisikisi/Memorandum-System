import glob
import os
import json

"""
example chunk:
(sdp 781 :creation-time 12313 :reference-list())
"""

def image_data(files, new_file, json_load):
    for file in files:
        with open(file ,mode="r", encoding='utf8') as f:
            with open(new_file,mode="a", encoding='utf8') as f2:
                s = ""
                tmp = 0
                for line in f.readlines():
                    for text in line:
                        if text == '"':
                            tmp += 1
                            if tmp == 1:
                                continue
                        if tmp == 1:
                            s += text
                        elif tmp == 2:
                            break
                    #f2.write('(sdp '+s+' :creation-time '+str(time)+' :reference-count '+leng+')\n')
                    for i in range(len(json_load)):
                        if json_load[i]["id"] == s[:-1]:
                            f2.write('(sdp '+s+
                                    ' :creation-time '+str(json_load[i]["lastVisitTimeTimestamp"])[0:10]+
                                    ' :reference-count '+str(json_load[i]["visitCount"])+')\n')
                                    #' :reference-count '+"1"+')\n')
                            break
                    break
            print(file)

"""
Create label data
example chunk:
(sdp 781-Chrome :creation-time 12313 :reference-count 3)
"""

def label_data(files, new_file, json_load):
    for file in files:
        with open(file ,mode="r", encoding='utf8') as f:
            with open(new_file,mode="a", encoding='utf8') as f2:
                ls = []
                text = ""
                tmp2 = 0
                for line in f.readlines():
                    for t in line:
                        if t == '"':
                            tmp2 += 1
                            if tmp2 == 1:
                                continue
                        if tmp2 == 1:
                            text += t
                        elif tmp2 == 2:
                            break
                            
                    s = ""
                    tmp = 0
                    for i in range(len(line)):
                        if line[i] == '"':
                            tmp += 1
                            if tmp == 1:
                                continue
                        if tmp == 2:
                            break
                        elif tmp == 1:
                            s += str(line[i])
                    if s == "":
                        break
                    ls.append(s)
                    if ls[0] == s:
                        continue
                        
                    #f2.write('(sdp '+str(ls[0])+"-"+s+" :creation-time "+str(time)+' :reference-count '+leng+')\n')
                    #f2.write('(sdp '+"l-"+s+" :creation-time "+str(time)+' :reference-count '+leng+')\n')
                    for i in range(len(json_load)):
                        if json_load[i]["id"] == text[:-1]:
                            f2.write('(sdp '+str(ls[0])+"-"+s+
                                    ' :creation-time '+str(json_load[i]["lastVisitTimeTimestamp"])[0:10]+
                                    ' :reference-count '+str(json_load[i]["visitCount"])+')\n')
                                    #' :reference-count '+"1"+')\n')
                            f2.write('(sdp l-'+s+
                                    ' :creation-time '+str(json_load[i]["lastVisitTimeTimestamp"])[0:10]+
                                    ' :reference-count '+str(json_load[i]["visitCount"])+')\n')
                                    #' :reference-count '+"1"+')\n')
                            break
            print(file)
        

if __name__ == "__main__": 
    print("create-param start")  
    json_open = open('history/history.json', 'r', encoding='utf8')
    json_load = json.load(json_open)
    files = glob.glob("visicon/idata/*")
    new_file = "param/img-param.lisp"

    with open(new_file,mode="w", encoding='utf8')as f:
        f.read

    image_data(files, new_file, json_load)
    print("create-param 1/2 finish")
    label_data(files, new_file, json_load)
    print("create-param 2/2 finish")
    
    

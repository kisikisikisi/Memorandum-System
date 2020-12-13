#create image data
import glob
import os

"""
example chunk
#image0 isa image-data text "image0" type image
"""

def image_data(files, new_file):
    for i,file in enumerate(files):
        with open(file ,mode="r", encoding='utf8') as f:
            with open(new_file, mode="a", encoding='utf8') as f2:
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
                    f2.write('('+s+' isa image-data text "'+s+'" type image)\n')
                    break

#create label data
"""
example chunk:
#l-Chrome isa label-data text "Chrome")
#(687-無料 isa inc-label idata 687 lebel l-無料)
"""

def label_data(files, new_file):
    temp2 = []
    for i,file in enumerate(files):
        with open(file ,mode="r", encoding='utf8') as f:
            with open(new_file, mode="a", encoding='utf8') as f2:
                ls = []
                s = ""
                for line in f.readlines():
                    if len(line.split('"')) >= 2:
                        temp2.append(line.split('"')[1])
                        if len(temp2) >= 2:
                            if temp2[-1] == temp2[-2]:
                                continue
                        if "topic" in line.split('"')[1]:
                            s = line.split('"')[1]
                        else:
                            page = line.split('"')[1]
                        if not line.split('"')[1] in temp2[:-1] and s != "":
                            f2.write('(l-'+s+' isa label-data text "'+s+'")\n')
                        if s != "":
                            f2.write('('+str(page)+"-"+s+" isa inc-label idata "+str(page)+' label l-'+s+' looking1 l-'+s+ ' looking2 l-'+s+' looking3 l-'+s+')\n')
                        #f2.write('('+s+' isa meaning word "'+s+'")\n')
        

if __name__ == '__main__':
    print("create-dm start")
    files = glob.glob("visicon/idata/*")
    new_file = "dm/img-dm.lisp"

    with open(new_file, mode="w", encoding='utf8') as f2:
        f2.write("(add-dm-fct '(")

    image_data(files, new_file)
    label_data(files, new_file)

    with open(new_file, mode="a", encoding='utf8') as f2:
        f2.write("))")
    print("create-dm finish")
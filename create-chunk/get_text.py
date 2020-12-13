import json
import requests as req
from bs4 import BeautifulSoup
"""
2020年10月9日更新
load()でget_textを試しに5回実行
"""

class Get_text:

    def __init__(self, history, text):
        self.history = history
        self.text = text

    def get_text(self, url, output_file):
        try:
            html = req.get(url).content
            soup = BeautifulSoup(html, 'html.parser')
            self.append_text('p', soup, output_file)
            self.append_text('h1', soup, output_file)
            self.append_text('h2', soup, output_file)
            self.append_text('h3', soup, output_file)
            return 
        except:
            return
        
    def check_tag(self, tag, soup):
        try:
            texts = soup.find_all(tag)
            return texts
        except:
            return
        
    def append_text(self, tag, soup, output_file):
        texts = self.check_tag(tag, soup)
        for p in texts:
            output_file.write(p.get_text())
            

    def load(self):
        json_open = open(self.history, mode='r', encoding='utf8')
        json_load = json.load(json_open)
        with open('web_text.txt', mode='a', encoding='utf8') as output_file:
            for i in range(len(json_load)):
                self.get_text(json_load[i]['url'], output_file)
                print(str(i+1) + '/' + str(len(json_load)) + ' done')
                #debug
                #if i == 5:
                #    break

if __name__ == '__main__':
    with open('./web_text.txt', mode='w') as f:
        f.read
    Gt = Get_text('history/history.json', [])
    Gt.load()

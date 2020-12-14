import sys
import gensim
import string
import nltk
import copy
import json
import numpy as np
import requests as req
import pyLDAvis
from time import sleep
from collections import Counter
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer


class Topic_model:
"""トピックモデルによる文書分類"""
    def __init__(self, text_file, history, output):
        self.text_file = text_file
        self.history = history
        self.output = output

    def load(self):
        """テキストのロード"""
        all_lines = []
        with open(self.text_file, mode='r', encoding='utf8') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                all_lines.append(lines[i])
        self.janome(all_lines, False)

    def janome(self, text, flag):
        """形態素解析"""
        tokenizer = Tokenizer()
        stopwords_en = stopwords.words('english')
        lines = []
        for sentence in text:
            tmp = []
            for token in tokenizer.tokenize(sentence):
                pos = token.part_of_speech.split(',')[0]
                if pos in ["名詞", "動詞", "形容詞"]:   # 対象とする品詞
                    string = str(token.surface).lower()
                    if (not string in stopwords_ja) and string != " " and (not string in stopwords_en):
                        tmp.append(string)
            lines.append(tmp)
  
        if flag == True:
            return lines
        self.clean_empty(lines)

    def clean_empty(self, lines):
        """空のリストを削除"""
        for line in lines:
            if line == []:
                lines.remove([])
                continue
        self.topic_model(lines)


    def get_text_new(self, url, text):
        """テキストの抽出"""
        try:
            html = req.get(url).content
            soup = BeautifulSoup(html, 'html.parser')
            self.append_text('p', soup, text)
            self.append_text('h1', soup, text)
            self.append_text('h2', soup, text)
            self.append_text('h3', soup, text)
            return text
        except:
            return False
        
    def check_tag(self, tag,soup):
        """HTMLタグのチェック"""
        try:
            texts = soup.find_all(tag)
            return texts
        except:
            return
        
    def append_text(self, tag, soup, text):
        """テキストの追加"""
        texts = self.check_tag(tag, soup)
        for p in texts:
            text.append(p.get_text())

    def topic_model(self, pages):
        """文書分類"""
        dic = gensim.corpora.Dictionary(pages)
        corpus = [dic.doc2bow(p) for p in pages]
        num_topics = 50

        lda = gensim.models.ldamodel.LdaModel(
            corpus=corpus,
            num_topics=num_topics,
            id2word=dic,
            random_state = 1)
        
        lda.save("lda.model")

        json_open = open(self.history, mode='r', encoding='utf8')
        json_load = json.load(json_open)
        for i in range(len(json_load)):
            di = json_load[i]['id']
            web_text = self.get_text_new(json_load[i]['url'],[])
            print(str(i)+'/'+str(len(json_load)))
            if web_text != False:
                self.get_topic_number(web_text, lda, di)
            #debug
            #if i == 5:
            #    break
        #sys.exit()
        #visualize(lda, corpus, dic, num_topics)

    def get_topic_number(self, corpus, lda, di):
        """トピックの推定"""
        text = self.janome(corpus, True)
        dic = gensim.corpora.Dictionary(text)
        corpus = [dic.doc2bow(p) for p in text]
        topics = lda.get_document_topics(corpus, per_word_topics=False)
        self.save_topic(topics, di)

    def save_topic(self, topic, di):
        """トピックの保存"""
        topic_num = [[0, i+1] for i in range(50)]
        topic_ls = []
        topic_len = 0
        try:
            for t in topic:
                topic_ls.append(t)
            topic_len = len(topic)
            for i in range(len(topic_ls)):
                for j in range(len(topic_ls[i])):
                    topic_num[topic_ls[i][j][0]][0] += topic_ls[i][j][1]
            for num in topic_num:
                num[0] = num[0]/topic_len
            with open(self.output, mode='a', encoding='utf8') as f:
                f.write("id:"+str(di)+str(topic_num))
        except:
            return


if __name__ == '__main__':
    with open('topic.txt', mode='w') as f:
        f.read
    tm = Topic_model('web_text.txt', 'history/history.json', 'topic.txt')
    nltk.download('stopwords')
    stopwords_ja = ["し", "い", "よう", "こと", "いる", "あり", "ある", "これ", "さ", "する", "れ",
                "て", "くれる", "やっ", "でき", "ため", "も", "なり"]
    tm.load()

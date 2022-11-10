import requests as rq
import xlsxwriter as xlsxwriter
from bs4 import BeautifulSoup as bs
import xlsxwriter
import nltk
from nltk import word_tokenize
import string
import spacy
from spacy import displacy
from textblob import TextBlob
import pandas as pd

nlp = spacy.load("en_core_web_sm")

pg=0

headers = {'Host': 'www.goodreturns.in',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}

df = pd.read_csv("word_list_big2small.csv", header=None, usecols=[1])

for x in df:
    data=df[x].values
    print(data)
    print(type(data))

    for y in data:
        row=y

        workbook = xlsxwriter.Workbook(row + "_quotes" + ".xlsx")
        worksheet = workbook.add_worksheet("all_quotes")
        worksheet.write(0, 0, '#')
        worksheet.write(0, 1, 'topic')
        worksheet.write(0, 2, 'quote')
        worksheet.write(0, 3, 'author')
        worksheet.write(0, 4, 'title')
        worksheet.write(0, 5, 'NER')
        worksheet.write(0, 6, 'POS')

        for page in range(1,61):
            p=str(page)
            url = "https://www.goodreads.com/quotes/tag/"+ row +"/?page=" + p
            print(url)

            if page > 1:
                pg += 30

            html_text = rq.get(url, headers=headers, allow_redirects=False).text
            soup = bs(html_text, 'lxml')
            anchor1 = soup.find_all('div', class_='quoteDetails')

            for index, job in enumerate(anchor1):
                skill3=""

                if job.find('div', class_='quoteText').text:
                    skill1 = job.find('div', class_='quoteText').text

                if job.find('span', class_='authorOrTitle').text:
                    skill2 = job.find('span', class_='authorOrTitle').text

                if job.find('a', {'class': 'authorOrTitle', 'href': True}):
                    skill3 =job.find('a', {'class': 'authorOrTitle', 'href': True})
                    skill3=skill3.text

                skill=skill1[:skill1.index("―")]
                quote = skill.strip()
                quote = quote.replace('“', '')
                quote = quote.replace('”', '')

                skill2=skill2.strip()
                author = skill2.rstrip(',')

                sentence= quote+" "+author+" "+skill3
                res = sentence.translate(str.maketrans('', '', string.punctuation))

                blob_object = TextBlob(sentence)
                pos_res=blob_object.tags

                l=[]
                doc = nlp(res)
                entities = []
                labels = []

                for ent in doc.ents:
                    entities.append(ent)
                    labels.append(ent.label_)
                    l = list(zip(entities, labels))


                worksheet.write(pg + index + 1, 0, str(index + 1 + pg))
                worksheet.write(pg + index + 1, 1, row)
                worksheet.write(pg + index + 1, 2, quote)
                worksheet.write(pg + index + 1, 3, author)
                worksheet.write(pg + index + 1, 4, skill3)
                worksheet.write(pg + index + 1, 5, str(l))
                worksheet.write(pg + index + 1, 6, str(pos_res))
        pg=0
        workbook.close()
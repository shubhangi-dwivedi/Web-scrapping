import requests as rq
from bs4 import BeautifulSoup as bs
import xlsxwriter
import nltk
from nltk import word_tokenize
import string
import spacy
from spacy import displacy
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")

pg=0

topic="Love"

workbook = xlsxwriter.Workbook(topic+"_quotes" + ".xlsx")
worksheet = workbook.add_worksheet("all_jobs")

worksheet.write(0, 0, '#')
worksheet.write(0, 1, 'topic')
worksheet.write(0, 2, 'quote')
worksheet.write(0, 3, 'author')
worksheet.write(0, 4, 'title')
worksheet.write(0, 5, 'NER')
worksheet.write(0, 6, 'POS')

i=0
j=0
for page in range(1,101):
    p=str(page)
    url = "https://www.goodreads.com/quotes/tag/"+ topic +"/?page=" + p
    print(url)

    if page > 1:
        pg += 30

    html_text = rq.get(url).text
    soup = bs(html_text, 'lxml')
    anchor1 = soup.find_all('div', class_='quoteDetails')

    for index, temp1 in enumerate(anchor1):
        authOrTitle2= ""

        if temp1.find('div', class_='quoteText').text:
            quoteText = temp1.find('div', class_='quoteText').text

        if temp1.find('span', class_='authorOrTitle').text:
            authOrTitle1 = temp1.find('span', class_='authorOrTitle').text

        if temp1.find('a', {'class': 'authorOrTitle', 'href': True}):
            authOrTitle2 =temp1.find('a', {'class': 'authorOrTitle', 'href': True})
            authOrTitle2=authOrTitle2.text

        temp2= quoteText[:quoteText.index("―")]
        quote = temp2.strip()
        quote = quote.replace('“', '')
        quote = quote.replace('”', '')

        authOrTitle1=authOrTitle1.strip()
        author = authOrTitle1.rstrip(',')

        sentence= quote +" " + author +" " + authOrTitle2
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
        worksheet.write(pg + index + 1, 1, topic)
        worksheet.write(pg + index + 1, 2, quote)
        worksheet.write(pg + index + 1, 3, author)
        worksheet.write(pg + index + 1, 4, authOrTitle2)
        worksheet.write(pg + index + 1, 5, str(l))
        worksheet.write(pg + index + 1, 6, str(pos_res))

workbook.close()
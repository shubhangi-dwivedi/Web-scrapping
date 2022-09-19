import inline as inline
import matplotlib
import nltk as nltk
import requests
import xlsxwriter
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re
import matplotlib.pyplot as plt
import seaborn as sns
from openpyxl.reader.excel import load_workbook


def plot_word_freq(url):
    """Takes a url (from Project Gutenberg) and plots a word frequency
    distribution"""
    # Make the request and check object type
    r = requests.get(url)
    # Extract HTML from Response object and print
    html = r.text
    # Create a BeautifulSoup object from the HTML
    soup = BeautifulSoup(html, "html5lib")
    # Get the text out of the soup and print it
    text = soup.get_text()
    # Create tokenizer
    tokenizer = RegexpTokenizer('\w+')
    # Create tokens
    tokens = tokenizer.tokenize(text)
    # Initialize new list
    words = []
    # Loop through list tokens and make lower case
    for word in tokens:
        words.append(word.lower())
    # Get English stopwords and print some of them
    sw = nltk.corpus.stopwords.words('english')
    # Initialize new list
    words_ns = []
    # Add to words_ns all words that are in words but not in sw
    for word in words:
        if word not in sw:
            words_ns.append(word)
    # Create freq dist and plot
    freqdist1 = nltk.FreqDist(words_ns)

    topWords = freqdist1.most_common()

    workbook= xlsxwriter.Workbook(filename='pride_and_prejudice.xlsx')
    worksheet= workbook.add_worksheet('words_record')

    worksheet.write(0, 0, '#')
    worksheet.write(0, 1, 'word')
    worksheet.write(0, 2, 'frequency')

    count=0
    print(len(topWords))

    for i in range(len(topWords)):
        worksheet.write(count + 1, 0, str(count+1))
        worksheet.write(count + 1, 1, str(topWords[count][0]))
        worksheet.write(count + 1, 2, str(topWords[count][1]))
        count+=1

    workbook.close()

    freqdist1.plot(25)

plot_word_freq('https://www.gutenberg.org/files/42671/42671-h/42671-h.htm')
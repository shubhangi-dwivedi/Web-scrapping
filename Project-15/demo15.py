import json
from bs4 import BeautifulSoup
import requests as rq
import xlsxwriter

workbook= xlsxwriter.Workbook("iconfinder_search2_4.xlsx")
worksheet= workbook.add_worksheet('synon')

with open("words_dictionary2_4.json") as json_file:
    jsondata = json.load(json_file)

i=0
for allKeys in jsondata:
    word=allKeys

    worksheet.write(0, 0, '#')
    worksheet.write(0, 1, 'word')
    worksheet.write(0, 2, 'suggestions')

    url = 'https://www.iconfinder.com/search?q=' + word

    skills = ''

    l1 = []

    html_text = rq.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('a', class_='btn btn-light btn-sm rounded-pill px-3')
    x = ''

    for index, job in enumerate(jobs):
        x = job.text
        l1.append(x)

    print(allKeys)
    print(l1)

    if len(l1)!=0:
        worksheet.write(i+ 1, 0, str(1 + i))
        worksheet.write(i + 1, 1, word)
        worksheet.write(i + 1, 2, str(l1))
        i+=1

workbook.close()
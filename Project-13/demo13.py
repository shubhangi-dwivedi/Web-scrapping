from bs4 import BeautifulSoup
import requests as rq
import xlsxwriter

workbook= xlsxwriter.Workbook("synon.xlsx")
worksheet= workbook.add_worksheet('synon')

word='vacation'

worksheet.write(0,0,'#')
worksheet.write(0,1,'word')
worksheet.write(0,2,'synonyums')

url= 'https://www.iconfinder.com/search?q='+word
pg=0
skills=''

l1=[]

html_text = rq.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('a', class_='btn btn-light btn-sm rounded-pill px-3')
x=''

for index,job in enumerate(jobs):
    x=job.text
    l1.append(x)

print(l1)

worksheet.write(pg+1, 0, str(1+pg))
worksheet.write(pg+1, 1, word)
worksheet.write(pg+1, 2, str(l1))

workbook.close()
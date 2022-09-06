from bs4 import BeautifulSoup
import requests as rq

url= 'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence='

file1 = open("job_skills.txt", "a")

for page in range(1,10):
    html_text = rq.get(url+str(page)+'&startPage=1').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        file1.write(skills)

file1.close()

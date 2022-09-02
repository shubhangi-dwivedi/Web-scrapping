from bs4 import BeautifulSoup
import requests as rq
import xlsxwriter

workbook= xlsxwriter.Workbook("job_records.xlsx")
worksheet= workbook.add_worksheet('python_jobs')

worksheet.write(0,0,'#')
worksheet.write(0,1,'Company_name')
worksheet.write(0,2,'skills')
worksheet.write(0,3,'more_info')

url= 'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence='
pg=0

for page in range(1,10):

    html_text = rq.get(url+str(page)+'&startPage=1').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    if page>1:
        pg+=25

    for index,job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text

        #pinting all jobs that are posted few days ago
        #'few' word should be present in published_date data
        if 'few' in published_date:
            company_name= job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills= job.find('span', class_='srp-skills').text.replace(' ','')
            more_info=job.header.h2.a['href'] #gettinf the href value i.e. link

            worksheet.write(pg+index+1, 0, str(index+1+pg))
            worksheet.write(pg+index+1, 1, company_name.strip())
            worksheet.write(pg+index+1, 2, skills.strip())
            worksheet.write(pg+index+1, 3, more_info)

workbook.close()


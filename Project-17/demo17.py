import json

import requests
from bs4 import BeautifulSoup
import requests as rq
import xlsxwriter


#------------------------

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

#-------------------------


workbook= xlsxwriter.Workbook("exp1.xlsx")
worksheet= workbook.add_worksheet('synon')

with open("exp.json") as json_file:
    reader = json.load(json_file)

i=0
str1=""
for row in reader:
    str1=row

    worksheet.write(0, 0, '#')
    worksheet.write(0, 1, 'word')
    worksheet.write(0, 2, 'suggestions')

    url = "https://relatedwords.org/relatedto/" + str1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}

    print(url)
    req = requests.get(url, headers=headers)
    l1 = []
    soup = BeautifulSoup(req.text, "html.parser")

    #l1.append(str1)
    for data in soup.find_all("script"):
        str1 = data.get_text()

        isValid = validateJSON(str1)
        if isValid == True:
            if str1 != "":
                l1.append(str1)

    print(l1)

    if len(l1) != 0:
        worksheet.write(i + 1, 0, str(1 + i))
        worksheet.write(i + 1, 1, row)
        worksheet.write(i + 1, 2, str(l1))
        i += 1


workbook.close()
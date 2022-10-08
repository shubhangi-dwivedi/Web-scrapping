import json

import requests
from bs4 import BeautifulSoup
import requests as rq
import xlsxwriter


# ------------------------

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True


# -------------------------


workbook= xlsxwriter.Workbook("related_words1.xlsx")
worksheet= workbook.add_worksheet('synon')

text = open("kw1.txt",'r')


#with open("relatedwords_23.json") as json_file:
 #   reader = json.load(json_file)

i = 0
str1 = ""
for row in text:

    worksheet.write(0, 0, '#')
    worksheet.write(0, 1, 'word')
    worksheet.write(0, 2, 'First 5')
    worksheet.write(0, 3, 'Next 10')
    worksheet.write(0, 4, 'Others')

    partitioned_string = row.partition(' :')
    str1 = partitioned_string[0]
    str1=str1.lstrip()

    curr_word=str1
    res = len(str1.split())

    if res>1:
         str2 = str1.replace(" ", "%20")
         url = "https://relatedwords.org/relatedto/" + str2

    else:
        url = "https://relatedwords.org/relatedto/" + str1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}

    print(url)
    req = requests.get(url, headers=headers)
    l1 = []
    l2=[]
    l3=[]
    soup = BeautifulSoup(req.text, "html.parser")

    # l1.append(str1)
    for data in soup.find_all("script"):
        str1 = data.get_text()

        isValid = validateJSON(str1)
        if isValid == True:
            if str1 != "":
                json_object = json.loads(str1)
                j=1
                for each in json_object['terms']:
                    #print(each['word'])
                    if j<=5:
                        l1.append(each['word'])
                    elif j<=15:
                        l2.append(each['word'])
                    else:
                        l3.append(each['word'])

                    j+=1


        if len(l1) != 0:
            worksheet.write(i + 1, 0, 1 + i)
            worksheet.write(i + 1, 1, curr_word)
            worksheet.write(i + 1, 2, str(l1))
            worksheet.write(i + 1, 3, str(l2))
            worksheet.write(i + 1, 4, str(l3))

            i += 1
            break

workbook.close()
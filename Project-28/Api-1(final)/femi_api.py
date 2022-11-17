import json
import requests
import xlsxwriter
from bs4 import BeautifulSoup
from flask_restful import Resource
from urllib.request import urlopen
import pandas as pd
import openpyxl
from textblob import TextBlob

class returnjson(Resource):

    def get2(self, json_without_slash,workbook,worksheet):
        # url = json_without_slash
        s1 = json.dumps(json_without_slash)
        #d2 = json.loads(s1)

        json_object = json.loads(s1)
        for each in json_object['data']:
            l = []
            l.append(json_object['category'])
            l.append(each['title'])
            l.append(each['snippet'])
            l.append(each['url'])

            x=each['title'].replace("...","")
            title_noun = TextBlob(x)
            title_noun = title_noun.noun_phrases
            l.append(str(title_noun))

            data = tuple(l)
            worksheet.append(data)

        workbook.save('output.xlsx')



    def get(self):
        #seed="apple"
        wb = openpyxl.Workbook()
        ws = wb.active

        with open('input_file.txt', 'r') as file:
            for seed in file:

                seed=seed.strip("\n")
                seed=seed.replace(" ","+")

                URL="https://www.femina.in/search/tag_"+ seed +"&sort=score+desc?pg=10"

                page = requests.get(URL)

                soup = BeautifulSoup(page.content, "html.parser")

                data1= soup.find_all("div", class_="search-section")

                data=[]
                for d in data1:
                    short_description = d.find("div", class_="clearfix")
                    title = d.find("h3")
                    snippet = d.find("p")
                    url = title.find("a")["href"]

                    short_description=short_description.text.strip("\n")

                    data.append({"short_description":short_description,  "title":title.text ,"snippet": snippet.text, "url":url})

                    data2={"category": seed, "data": data}
                jsonData = json.dumps(data2)
                json_without_slash = json.loads(jsonData)

                self.get2(json_without_slash,wb,ws)

        wb.close()
        return json_without_slash

'''
    def get2(self,json_without_slash):
        #url = json_without_slash

        jsonData = json.dumps(json_without_slash)
        data_json = json.loads(str(jsonData))

        with open('femi_data.txt', 'a') as json_file:
            json.dump(data_json, json_file)

        json_file.close()
    '''

'''
class readjson(Resource):
    def get(self):
        url = "http://127.0.0.1:5000/"

        response = urlopen(url)

        data_json = json.loads(response.read())

        with open('femi_data.txt', 'w') as json_file:
            json.dump(data_json, json_file)

        json_file.close()
'''
import json
import requests
from bs4 import BeautifulSoup
from flask_restful import Resource
from urllib.request import urlopen

class returnjson(Resource):
    def get2(self,json_without_slash):
        #url = json_without_slash

        jsonData = json.dumps(json_without_slash)
        data_json = json.loads(str(jsonData))

        with open('femi_data.txt', 'w') as json_file:
            json.dump(data_json, json_file)

        json_file.close()

    def get(self):
        seed="apple"

        URL="https://femina.in/search/tag_" + seed

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

        self.get2(json_without_slash)

        return json_without_slash


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
from flask import Flask
from flask_restful import Api
from  scraper import *

app = Flask(__name__)
api = Api(app)

api.add_resource(anOtherScraper,'/anOtherScraper') #1
api.add_resource(architecturalDigestScraper,'/architecturalDigestScraper') #2 #nonetype
api.add_resource(countryLivingScraper,'/countryLivingScraper') #3
api.add_resource(elleDecorScraper,'/elleDecorScraper') #4
api.add_resource(femina,'/femina') #5
api.add_resource(foodAndWineScraper,'/foodAndWineScraper')#6
api.add_resource(gfmagScraper,'/gfmagScraper')#7
api.add_resource(hotelierScraper,'/hotelierScraper') #8
api.add_resource(houseBeautifulScraper,'/houseBeautifulScraper')#9
api.add_resource(lodgingScraper,'/lodgingScraper')#10
api.add_resource(nationalGeographicScraper,'/nationalGeographicScraper')#11
api.add_resource(nylonScraper,'/nylonScraper')#12
api.add_resource(romanticHomesScraper,'/romanticHomesScraper')#13
api.add_resource(theSpruceScraper,'/theSpruceScraper')#14
api.add_resource(verandaScraper,'/verandaScraper')#15
api.add_resource(instoreScraper,'/instoreScraper')#16
api.add_resource(gjepcScraper,'/gjepcScraper')#17
api.add_resource(flowerScraper,'/flowerScraper')#18
api.add_resource(elleDecor2Scraper,'/elleDecor2Scraper')#19
api.add_resource(allureScraper,'/allureScraper')#20
api.add_resource(stampingtonScraper,'/stampingtonScraper')#21
api.add_resource(indianJewelerScraper,'/indianJewelerScraper')#22
api.add_resource(metropolisScraper,'/metropolisScraper')#23
api.add_resource(moneyScraper,'/moneyScraper')#24
api.add_resource(motoringScraper,'/motoringScraper')#25
api.add_resource(professionalWomanScraper,'/professionalWomanScraper')#26
api.add_resource(townAndCountryScraper,'/townAndCountryScraper')#27
api.add_resource(travelAndLeisureIndiaScraper,'/travelAndLeisureIndiaScraper')#28
api.add_resource(travelPeacockScraper,'/travelPeacockScraper')#29
api.add_resource(vanityFairScraper,'/vanityFairScraper')#30
api.add_resource(womensHealthScraper,'/womensHealthScraper')#31
api.add_resource(theJewelryScraper,'/theJewelryScraper')#32
api.add_resource(theEnglishGardenScraper,'/theEnglishGardenScraper')#33
api.add_resource(teenVogueScraper,'/teenVogueScraper')#34
api.add_resource(solitaireScraper,'/solitaireScraper')#35
api.add_resource(southernLivingScraper,'/southernLivingScraper')#36
api.add_resource(styleAtHomeScraper,'/styleAtHomeScraper')#37
api.add_resource(realSimpleScraper,'/realSimpleScraper')#38
api.add_resource(realHomesScraper,'/realHomesScraper')#39
api.add_resource(newYorkerScraper,'/newYorkerScraper')#40
api.add_resource(moneySenseScraper,'/moneySenseScraper')#41
api.add_resource(maximScraper,'/maximScraper')#42
api.add_resource(livingetcScraper,'/livingetcScraper')#43
api.add_resource(inStyleScraper,'/inStyleScraper')#44
api.add_resource(harpersBazaarScraper,'/harpersBazaarScraper')#45
api.add_resource(graziaScraper,'/graziaScraper')#46
api.add_resource(glamourScraper,'/glamourScraper')#47
api.add_resource(gardensIllustratedScraper,'/gardensIllustratedScraper')#48
api.add_resource(dwellScraper,'/dwellScraper')#49
api.add_resource(cosmopolitanScraper,'/cosmopolitanScraper')#50
api.add_resource(cntravellerScraper,'/cntravellerScraper')#51
#api.add_resource(businessTodayScraper,'/businessTodayScraper')#52
api.add_resource(bhgScraper,'/bhgScraper')#53

if __name__ == '__main__':
    app.run(debug = True)
import scrapy
import pickle

class MySpider(scrapy.Spider):

    # name of my crawler 
    name = "coronaCrawler"

    def start_requests(self):

        pageUrl = ['https://www.worldometers.info/coronavirus/']

        for url in pageUrl :
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):

        tempList = response.xpath("//div[@class='maincounter-number']/span/text()").extract()
        coronavirusCases = tempList[0]
        coronavirusCasesDeath = tempList[1]
        coronavirusCasesRecovered = tempList[2]

        numberOfCountry = len(response.xpath("//tbody/tr/td[3]/text()").extract())

        tableInfo = [] 
        country = []
        for i in range(1, numberOfCountry):
            thisCountry = response.xpath("//tbody/tr["+str(i)+"]/td[2]/text()").extract()
            self.deleteKeyFromList(thisCountry, " ")
            if thisCountry == []:
                thisCountry = response.xpath("//tbody/tr["+str(i)+"]/td[2]/a/text()").extract()
                if thisCountry == []:  
                    thisCountry = response.xpath("//tbody/tr["+str(i)+"]/td[2]/span/text()").extract()
            self.deleteKeyFromList(thisCountry, " ")
            if thisCountry == [] :
                thisCountry.append("") 

            country.append(thisCountry[0])
            self.deleteKeyFromList(thisCountry, "")


                

        totalcases = response.xpath("//tbody/tr/td[3]/text()").extract()
        newCases = response.xpath("//tbody/tr/td[4]/text()").extract()
        totalDeath = response.xpath("//tbody/tr/td[5]/text()").extract()
        newDeath = response.xpath("//tbody/tr/td[6]/text()").extract()
        totalRecovered = response.xpath("//tbody/tr/td[7]/text()").extract()
        activeCases = response.xpath("//tbody/tr/td[8]/text()").extract()
        seriousCritical = response.xpath("//tbody/tr/td[9]/text()").extract()
        totalCaseIn1Mpop = response.xpath("//tbody/tr/td[10]/text()").extract()

        tableInfo.append(country)
        tableInfo.append(totalcases)
        tableInfo.append(newCases)
        tableInfo.append(totalDeath)
        tableInfo.append(newDeath)
        tableInfo.append(totalRecovered)
        tableInfo.append(activeCases)
        tableInfo.append(totalCaseIn1Mpop)
        tableInfo.append(seriousCritical)



        f = open("statics\DB\CoronaDB.dat", "wb")
        pickle.dump(coronavirusCases, f)
        pickle.dump(coronavirusCasesDeath, f)
        pickle.dump(coronavirusCasesRecovered, f)
        pickle.dump(tableInfo, f)
        f.close()

    def deleteKeyFromList(self, myList, key):
        while key in myList :
            myList.remove(key)
        return myList



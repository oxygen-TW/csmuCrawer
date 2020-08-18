from bs4 import BeautifulSoup
import requests
import re
import datetime
from datetime import datetime
import json

class News():

    def __init__(self, date):
        self.date = date
            
    def __MessageRegex(self, part):
        result = re.findall(r">(.+)<\/td>", str(part))
        result[0] = re.findall(r">(.+)<", result[0])[0]
        result[2] = re.findall(r"href=\"(.+)\">(.+)<", result[2])[0]
        return result


    #Formate require YY/MM/DD
    def __GenerateFormatDate(self):
        #datetimeYesterday = datetime.date.today() + datetime.timedelta(days=-1)
        dateStr = self.date
        datetimeobj = object()

        if(dateStr == "today"):
             datetimeobj = datetime.date.today()
        elif(dateStr == "yesterday"):
            datetimeobj = datetime.date.today() + datetime.timedelta(days=-1)
        else:
            datetimeobj = datetime.strptime(dateStr, "%Y/%m/%d")

        year = str(int(datetimeobj.strftime("%Y")) - 1911)
        date = year + datetimeobj.strftime("/%m/%d")
        return date

    def get(self):
        url = "http://message.csmu.edu.tw/main2List.asp"
        baseurl = "https://message.csmu.edu.tw/"
            
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
            
        rr = soup.find_all("tr",class_="whitetablebg")


        date = self.__GenerateFormatDate()

        msg = date+" 中山醫大校園公告 \n"
        #     ^m ^x  ^p  ^|^i ^v   ^h ^a  ^z^dflag
        haveNews = False
        NewsList = {
            "status": bool(),
            "date": date,
            "data": []
        }

        for item in rr:
            if(date in str(item)):
                haveNews = True
                news = self.__MessageRegex(item)

                NewsList["data"].append({
                    "Name": news[2][1],
                    "Category": news[0],
                    "Apartment": news[3],
                    "Url": baseurl + news[2][0]
                })

        if(haveNews):
            NewsList["status"] = True
        else:
            NewsList["status"] = False
        return NewsList

if __name__ == "__main__":
    n = News("2019/06/15")
    print(n.get())

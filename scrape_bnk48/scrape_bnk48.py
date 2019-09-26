import urllib.request
from bs4 import BeautifulSoup
import urllib
import sys

class ScrapeBnk48:
    url = "https://www.bnk48.com/index.php?page=members"
    
    def scrape(self):
        fp = urllib.request.urlopen(self.url)
        html = fp.read()
        page = BeautifulSoup(html, "html.parser")
        for div in page.findChildren("div", {"class": "boxMemx"}):
            imgMemDiv = div.findChildren("div", {"class": "ImgMem"})[0]
            tmp = imgMemDiv["style"]
            index = tmp.find("(")
            actualUrl = tmp[index+1: len(tmp) - 2]
            actualUrl = "https://www.bnk48.com/" + actualUrl
            nameMemDiv = div.findChildren("div", {"class": "nameMem"})[0]
            fileName = nameMemDiv.text.strip() + ".png"
            fileName = fileName.encode("utf8")
            print(fileName)
            urllib.request.urlretrieve(actualUrl, fileName)

if __name__ == '__main__':
    scraper = ScrapeBnk48()
    scraper.scrape()
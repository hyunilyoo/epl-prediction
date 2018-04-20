import scrapy
import time
from selenium import webdriver
from scrapy.selector import Selector
from epl_crawler.items import EPLItem

class EPLSpider(scrapy.Spider):
    name = "PremierLeague"
    allowed_domains = ["premierleague.com"]
    start_urls = [
        "https://www.premierleague.com/tables"
    ]
    
    def __init__(self):
        scrapy.Spider.__init__(self)
        self.browser = webdriver.Chrome("C:\sta\chromedriver.exe")
    
    def parse(self, response):
        self.browser.get(response.url)
        time.sleep(5)
        
        html = self.browser.find_element_by_xpath('//*').get_attribute('outerHTML')
        selector = Selector(text=html)
        rows = selector.xpath('//*[@id="mainContent"]/div[2]/div[1]/div[3]/div/div/div/table/tbody/tr[not(@class="expandable")]')
        
        for row in rows:
            item = EPLItem()
            item["club_name"] = row.xpath('./td[3]/a/span[2]/text()')[0].extract()
            item["position"] = row.xpath('./td[2]/span[1]/text()')[0].extract()
            item["won"] = row.xpath('./td[5]/text()')[0].extract()
            item["lost"] = row.xpath('./td[7]/text()')[0].extract()
            item["drawn"] = row.xpath('./td[6]/text()')[0].extract()
            item["goal"] = row.xpath('./td[8]/text()')[0].extract()
            item["goal_against"] = row.xpath('./td[9]/text()')[0].extract()
            item["points"] = row.xpath('./td[11]/text()')[0].extract()
            yield item
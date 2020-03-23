import scrapy
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from scrapy.selector import Selector
from table_crawler.items import TableItem

class TableSpider(scrapy.Spider):
    name = "Tables"
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
        
        for i in range(2,30):
            self.browser.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[1]/div[1]/section/div[2]/div[2]').click()
            self.browser.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[1]/div[1]/section/div[2]/ul/li'+str([i])).click()
            time.sleep(8)
            
            html = self.browser.find_element_by_xpath('//*').get_attribute('outerHTML')
            selector = Selector(text=html)
            rows = selector.xpath('//*[@id="mainContent"]/div[2]/div[1]/div[3]/div/div/div/table/tbody/tr[not(@class="expandable")]')
            for row in rows:
                item = TestItem()
                item["club_name"] = row.xpath('./td[3]/a/span[2]/text()')[0].extract()
                item["position"] = row.xpath('./td[2]/span[1]/text()')[0].extract()
                item["won"] = row.xpath('./td[5]/text()')[0].extract()
                item["lost"] = row.xpath('./td[7]/text()')[0].extract()
                item["drawn"] = row.xpath('./td[6]/text()')[0].extract()
                item["goal"] = row.xpath('./td[8]/text()')[0].extract()
                item["goal_against"] = row.xpath('./td[9]/text()')[0].extract()
                item["points"] = row.xpath('./td[11]/text()')[0].extract()
                yield item


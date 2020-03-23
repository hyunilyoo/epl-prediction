import scrapy
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from scrapy.selector import Selector
from clubstats_crawler.items import ClubItem

class CLUBSpider(scrapy.Spider):
    name = "Leicestats"
    allowed_domains = ["premierleague.com"]
    start_urls = [
        "https://www.premierleague.com/clubs/26/Leicester-City/stats?se=42"
    ]

    def __init__(self):
        scrapy.Spider.__init__(self)
        self.browser = webdriver.Chrome("C:\sta\chromedriver.exe")

    def parse(self, response):
        self.browser.get(response.url)
        time.sleep(5)
        html = self.browser.find_element_by_xpath('//*').get_attribute('outerHTML')
        selector = Selector(text=html)
# 2015/16
        item = ClubItem()
        item["club_name"] = selector.xpath('//*[@id="mainContent"]/header/div[2]/div/div/div[2]/h1/text()')[0].extract()
        item["goal_per_match"] = selector.xpath('//*[@id="mainContent"]/div[3]/div/div/ul/li[1]/div/div[3]/span/span/text()')[0].extract()
        item["shot_on_target"] = selector.xpath('//*[@id="mainContent"]/div[3]/div/div/ul/li[1]/div/div[5]/span/span/text()')[0].extract()
        item["shooting_accuracy"] = selector.xpath('//*[@id="mainContent"]/div[3]/div/div/ul/li[1]/div/div[6]/span/span/text()')[0].extract()
        item["big_chance_created"] = selector.xpath('//*[@id="mainContent"]/div[3]/div/div/ul/li[1]/div/div[8]/span/span/text()')[0].extract()
        item["pass_per_game"] = selector.xpath('//*[@id="mainContent"]/div[3]/div/div/ul/li[2]/div/div[3]/span/span/text()')[0].extract()
        item["pass_accuracy"] = selector.xpath('//*[@id="mainContent"]/div[3]/div/div/ul/li[2]/div/div[4]/span/span/text()')[0].extract()
        item["cross"] = selector.xpath('//*[@id="mainContent"]/div[3]/div/div/ul/li[2]/div/div[5]/span/span/text()')[0].extract()
        item["cross_accuracy"] = selector.xpath('//*[@id="mainContent"]/div[3]/div/div/ul/li[2]/div/div[6]/span/span/text()')[0].extract()
        item["goal_conceded_per_match"] = selector.xpath('//*[@id="mainContent"]/div[3]/div/div/ul/li[3]/div/div[4]/span/span/text()')[0].extract()
        item["tackle_success"] = selector.xpath('//*[@id="mainContent"]/div[3]/div/div/ul/li[3]/div/div[7]/span/span/text()')[0].extract()
        item["clearance"] = selector.xpath('//*[@id="mainContent"]/div[3]/div/div/ul/li[3]/div/div[10]/span/span/text()')[0].extract()
        item["aerial_battles"] = selector.xpath('//*[@id="mainContent"]/div[3]/div/div/ul/li[3]/div/div[12]/span/span/text()')[0].extract()
        item["interceptions"] = selector.xpath('//*[@id="mainContent"]/div[3]/div/div/ul/li[3]/div/div[9]/span/span/text()')[0].extract()
        yield item

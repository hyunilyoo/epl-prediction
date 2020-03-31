import scrapy
import time
from selenium import webdriver
from scrapy.selector import Selector
from clubstats_crawler.items import ClubstatsCrawlerItem


class ClubSpider(scrapy.Spider):
    name = "Clubstats"
    allowed_domains = ["premierleague.com"]
    start_urls = ["https://www.premierleague.com/clubs"]

    def __init__(self):
        scrapy.Spider.__init__(self)
        self.browser = webdriver.Chrome("C:\sta\chromedriver.exe")

    def parse(self, response):
        self.browser.get(response.url)
        time.sleep(5)
        html = self.browser.find_element_by_xpath('//*').get_attribute('outerHTML')
        selector = Selector(text=html)
        clubnames = []
        name = None
        season_count = None

        for i in range(1, 29):
            time.sleep(3)
            self.browser.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/section/div[1]/div[2]').click()
            time.sleep(3)
            self.browser.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/section/div[1]/ul/li'+str([i])).click()
            for j in range(1, 21):
                time.sleep(3)
                html = self.browser.find_element_by_xpath('//*').get_attribute('outerHTML')
                selector = Selector(text=html)
                name = selector.xpath('//*[@id="mainContent"]/div[2]/div/div/div[1]/div/ul/li'+str([j])+'/a/div[3]/div[2]/h4/text()')[0].extract()
                if name not in clubnames:
                    clubnames.append(name)
                    # Into Club
                    self.browser.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div/div[1]/div/ul/li'+str([j])+'/a/div[3]/div[3]/span').click()
                    time.sleep(3)
                    # navigate to stats
                    self.browser.find_element_by_xpath('//*[@id="mainContent"]/nav/ul/li[5]/a').click()
                    time.sleep(3)
                    html = self.browser.find_element_by_xpath('//*').get_attribute('outerHTML')
                    selector = Selector(text=html)
                    season_count = len(selector.xpath('//*[@id="mainContent"]/div[3]/div/div/section/div[1]/ul/li'))+1
                    # navigate to dropdown menu for seasons`
                    for k in range(2, season_count):
                        # This is for scrolling down the dropdown menu
                        if k < 10:
                            self.browser.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div/div/section/div[1]/div[2]').click()
                            time.sleep(3)

                            self.browser.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div/div/section/div[1]/ul/li'+str([k])).click()
                            time.sleep(5)

                            html = self.browser.find_element_by_xpath('//*').get_attribute('outerHTML')
                            selector = Selector(text=html)

                            item = ClubstatsCrawlerItem()
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
                            item["season"] = selector.xpath('//*[@id="mainContent"]/div[3]/div/div/section/div[1]/div[2]/text()')[0].extract()
                            yield item

                        elif k >= 10 and k < 19:
                            self.browser.execute_script('window.scrollTo(0, 150)')
                            self.browser.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div/div/section/div[1]/div[2]').click()
                            time.sleep(3)

                            self.browser.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div/div/section/div[1]/ul/li'+str([k])).click()
                            time.sleep(5)

                            html = self.browser.find_element_by_xpath('//*').get_attribute('outerHTML')
                            selector = Selector(text=html)

                            item = ClubstatsCrawlerItem()
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
                            item["season"] = selector.xpath('//*[@id="mainContent"]/div[3]/div/div/section/div[1]/div[2]/text()')[0].extract()
                            yield item

                        elif k >= 19:
                            self.browser.execute_script('window.scrollTo(0, 330)')
                            self.browser.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div/div/section/div[1]/div[2]').click()
                            time.sleep(3)

                            self.browser.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div/div/section/div[1]/ul/li'+str([k])).click()
                            time.sleep(5)

                            html = self.browser.find_element_by_xpath('//*').get_attribute('outerHTML')
                            selector = Selector(text=html)

                            item = ClubstatsCrawlerItem()
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
                            item["season"] = selector.xpath('//*[@id="mainContent"]/div[3]/div/div/section/div[1]/div[2]/text()')[0].extract()
                            yield item

                    self.browser.find_element_by_xpath('/html/body/header/div/nav/ul/li[8]/a').click()
                    time.sleep(3)
                    self.browser.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/section/div[1]/div[2]').click()
                    time.sleep(3)
                    self.browser.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/section/div[1]/ul/li'+str([i])).click()
            self.browser.find_element_by_xpath('/html/body/header/div/nav/ul/li[8]/a').click()

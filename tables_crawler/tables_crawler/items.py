# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TablesCrawlerItem(scrapy.Item):

    club_name = scrapy.Field()
    position = scrapy.Field()
    won = scrapy.Field()
    drawn = scrapy.Field()
    lost = scrapy.Field()
    goal = scrapy.Field()
    goal_against = scrapy.Field()
    points = scrapy.Field()

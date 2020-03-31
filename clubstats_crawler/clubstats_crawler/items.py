# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ClubstatsCrawlerItem(scrapy.Item):

    club_name = scrapy.Field()
    goal_per_match = scrapy.Field()
    shot_on_target = scrapy.Field()
    shooting_accuracy = scrapy.Field()
    big_chance_created = scrapy.Field()
    pass_per_game = scrapy.Field()
    pass_accuracy = scrapy.Field()
    cross = scrapy.Field()
    cross_accuracy = scrapy.Field()
    goal_conceded_per_match = scrapy.Field()
    tackle_success = scrapy.Field()
    clearance = scrapy.Field()
    aerial_battles = scrapy.Field()
    interceptions = scrapy.Field()
    season = scrapy.Field()

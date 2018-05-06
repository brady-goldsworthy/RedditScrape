# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RedditscrapeItem(scrapy.Item):
    subreddit = scrapy.Field() #subreddit name
    title = scrapy.Field() #post title
    domain = scrapy.Field() #link domain
    postid = scrapy.Field() #unique post id
    pass

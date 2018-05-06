# -*- coding: utf-8 -*-
import scrapy
from RedditScrape.items import RedditScrapeItem
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

'''
Brady Goldsworthy
Simple spider to scrape reddit
'''

class RedditbotSpider(scrapy.Spider):
	name = 'redditbot'
	allowed_domains = ['www.reddit.com']
	start_urls = ['http://www.reddit.com/']

	def parse(self, response):
		#extracting content from site
		sel = Selector(response)

#thing_t3_8hgx52

#//*[@id="thing_t3_8hgx52"]

		subreddit = response.css('.subreddit.hover.may-blank::text').extract()
		title = response.css('.title.may-blank::text').extract()
		domain = response.css('.domain a:nth-child(1)::text').extract()
		postid = response.xpath("//div[contains(@id, 'thing_t3')]/@id").extract()

		#Processing extracted info
		for data in zip(subreddit, title, domain, postid):
			item = RedditScrapeItem()
			item['subreddit'] = data[0]
			item['title'] = data[1]
			item['domain'] = data[2]
			item['postid'] = data[3]
			
			yield item

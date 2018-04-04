# -*- coding: utf-8 -*-
import scrapy

'''
Brady Goldsworthy

Simple spider to scrape reddit
Returns subreddit and title

'''

class RedditbotSpider(scrapy.Spider):
	name = 'redditbot'
	allowed_domains = ['www.reddit.com']
	start_urls = ['http://www.reddit.com/']

	def parse(self, response):
		#extracting content from site
		subreddit = response.css('.subreddit.hover.may-blank::text').extract()
		title = response.css('.title.may-blank::text').extract()

		#Processing extracted info
		for item in zip(subreddit, title):
			#store info in dictionary
			scraped_info = {
				'subreddit' : item[0],
				'title' : item[1]
			}

			#yield scraped info to scrapy
			yield scraped_info
# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
#from models import Posts, db_connect, create_deals_table
from . import models

class RedditScrapePipeline(object):

	def __init__(self):
		"""
		Initializes database connection and sessionmaker.
		Creates table.
		"""
		engine = models.db_connect()
		models.create_posts_table(engine)
		self.Session = sessionmaker(bind = engine)

	def process_item(self, item, spider):
		"""
		Save post info in the database.

		This method is called for every item pipeline component.

		"""
		session = self.Session()
		post = models.Posts(**item)

		try:
			session.merge(post)
			session.commit()
		except:
			session.rollback()
			raise
		finally: 
			session.close()

		return item
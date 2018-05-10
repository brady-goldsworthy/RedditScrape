from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

from . import settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

def create_posts_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Posts(DeclarativeBase):
    """Posts database model"""
    __tablename__ = "Posts"

    postid = Column('postid', String, primary_key=True)
    subreddit = Column('subreddit',String)
    title = Column('title', String)
    domain = Column('domain', String)
    date = Column('date', Date)
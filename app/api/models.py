# -*- encoding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from datetime import datetime
from app import db
import os
from sqlalchemy import create_engine
import pandas as pd
#
# basedir    = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../../db.sqlite3')
# engine = create_engine(SQLALCHEMY_DATABASE_URI)

class Tweets(db.Model):
    __tablename__ = 'Tweets'

    tweetID = Column(Integer, primary_key=True)
    tweetText = Column(String())
    userID = Column(Integer())
    userScreen = Column(String())
    userName = Column(String())
    userCreateDt = Column(db.DateTime, default=datetime.utcnow)
    userDesc = Column(String())
    userFollowerCt = Column(Integer())
    userLocation = Column(String())

    def __repr__(self):
        return f"Tweets('{self.tweetID}')"

    # file_name = 'twitter_api_1.csv'
    # df = pd.read_csv(file_name)
    # df.to_sql(con=engine, index_label='id', name=db.__tablename__, if_exists='replace')

class News(db.Model):
    __tablename__ = 'News'

    article_id = Column(Integer, primary_key=True)
    Source = Column(String())
    Title = Column(String())
    Author = Column(String())
    Description = Column(String())
    Pub_Date = Column(db.DateTime, nullable=False)
    url = Column(String())
    urlToImage= Column(String())
    Content = Column(String())

    def __repr__(self):
        return f"News('{self.article_id}')"
#
# class Activism_Info(db.Model):
#     __tablename__ = 'Activism_Info'
#
#     a_id = Column(Integer, primary_key=True)
#     Group_Name = Column(String())
#     Cause = Column(String())
#     #Need to figure out what other info to grab for activism info
#
#     def __repr__(self):
#         return f"Activism_Info('{self.a_id}')"
#
#
# class (db. Model):
#     __tablename__ = ''
#
#     s_id = Column(Integer, primary_key=True)
#
#     # Need to figure out what other info to grab for sustainability info
#
#     def __repr__(self):
#         return f"Activism_Info('{self.s_id}')"
#
#
# class Organization(db.Model):
#     __tablename__ = 'Organizations'
#
#     h_id = Column(Integer, primary_key=True)
#     Group_Name = Column(String())
#     Cause = Column(String())
#
#     # Need to figure out what other info to grab for mental health info
#
#     def __repr__(self):
#         return f"Organizations('{self.h_id}')"
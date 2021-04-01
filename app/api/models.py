# -*- encoding: utf-8 -*-

from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String
from datetime import datetime

from app import db, login_manager

from app.base.util import hash_pass

class Tweet(db.Model):
    __tablename__ = 'Tweets'

    tweetID = db.Column(db.Integer, primary_key=True)
    tweetText = db.Column(db.String())
    userID = db.Column(db.Integer())
    userScreen = db.Column(db.String())
    userName = db.Column(db.String())
    userCreateDt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    userDesc = db.Column(db.String())
    userFollowerCt = db.Column(db.Integer())
    userLocation = db.Column(db.String())

    def __repr__(self):
        return f"Tweets('{self.tweetID}')"


class News(db.Model):
    __tablename__ = 'News'

    article_id = db.Column(db.Integer, primary_key=True)
    Source = db.Column(db.String())
    Title = db.Column(db.String())
    Author = db.Column(db.String())
    Description = db.Column(db.String())
    Pub_Date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    url = db.Column(db.String())
    urlToImage= db.Column(db.String())
    Content = db.Column(db.String())

    def __repr__(self):
        return f"News('{self.article_id}')"
#
# class Activism_Info(db.Model):
#     __tablename__ = 'Activism_Info'
#
#     a_id = db.Column(db.Integer, primary_key=True)
#     Group_Name = db.Column(db.String())
#     Cause = db.Column(db.String())
#     #Need to figure out what other info to grab for activism info
#
#     def __repr__(self):
#         return f"Activism_Info('{self.a_id}')"
#
#
# class (db.Model):
#     __tablename__ = ''
#
#     s_id = db.Column(db.Integer, primary_key=True)
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
#     h_id = db.Column(db.Integer, primary_key=True)
#     Group_Name = db.Column(db.String())
#     Cause = db.Column(db.String())
#
#     # Need to figure out what other info to grab for mental health info
#
#     def __repr__(self):
#         return f"Organizations('{self.h_id}')"

# -*- encoding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from datetime import datetime

# rom flask_script import Manager
# from flask _migrate import Migrate, MigrateCommand

from app import db

# migrate = Migrate(app, db)
# #anager = Manager(app)
# manager.add_commaned('db', MigrateCommand)


class Tweet(db.Model):
    __tablename__ = 'Tweets'

    tweetID = Column(Integer, primary_key=True)
    tweetText = Column(String())
    userID = Column(Integer())
    userScreen = Column(String())
    userName = Column(String())
    userCreateDt = Column(db.DateTime, default=datetime.utcnow)
    userUpdateDt = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    userDesc = Column(String())
    userFollowerCt = Column(Integer())
    userLocation = Column(String())

    def __repr__(self):
        return f"Tweets('{self.tweetID}')"


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

# if __name__ == '__main__':
#    manager.run()

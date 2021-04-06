# -*- encoding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from app import db
from datetime import datetime

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

# Update Tweets table with CSV
    try:
        file_name = "csv/twitter_api.csv"
        data = Load_Data(file_name)

        for i in data:
            record = Tweets(**{
                'tweetID': i[1],
                'tweetText': i[2],
                'userID': i[3],
                'userScreen': i[4],
                'userName': i[5],
                'userCreateDt': i[6]
                'userDesc': i[7],
                'userFollowerCt': i[8],
                'userLocation': i[9],
            })
            s.add(record)  # Add all the records

        s.commit()  # Attempt to commit all the records
    except:
        s.rollback()  # Rollback the changes on error
    finally:
        s.close()  # Close the connection
    print
    "Time elapsed: " + str(time() - t) + " s."  # 0.091s


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
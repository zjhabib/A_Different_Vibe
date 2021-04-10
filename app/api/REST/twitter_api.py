from sqlalchemy import create_engine
from app import db
import sys
import pandas as pd
import itertools
import tweepy
import os
from flask_sqlalchemy import SQLAlchemy

# TwitterAPI

consumer_key ='uXITGCvoR4d0UsbEmpE6rkwKu'
consumer_secret_key = 'PGhpXYnwr1UQqQRpKch05vrPEBX0F2GVvwtN0S8KAdiEeazdap'
access_token = '1293071076377804800-Xd2ar7Nfo4hfykqdBuAbekHd6PHIox'
access_token_secret = 'F1CvtAPwFEng6MGqtzcnrZLTz19enf4wVf0pwk0qxZ5OO'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Race
race_list = ['black lives matter', 'racial inequity', 'racial oppression']
race_tweet_data = []

# Environment
environment_list = ['climate change', 'sustainability', 'green energy', 'global warming']
environment_tweet_data = []

# Addiction
addiction_list = ['drug addiction', 'alcohol addiction']
addiction_tweet_data = []

# Current Hot Topics
current_list = ['india farmers', 'myanmar', 'asian-american hate']
current_tweet_data = []

# LGBT
lgbt_list = ['lgbt rights', 'gay rights', 'transgender rights', 'gay marriage']
lgbt_tweet_data = []

# Poverty
poverty_list = ['poverty', 'homeless right']
poverty_tweet_data = []

# Refugee
refugee_list = ['refugee human rights', 'border control']
refugee_tweet_data = []

# Womens Rights
women_list = ['female wages', 'womens rights']
women_tweet_data = []

# Mental Health
mental_list = ['mental health', 'mental illness', 'coping with mental illness', 'living with anxiety']
mental_tweet_data = []

# Disability rights
disability_list = ['Disability rights']
disability_tweet_data = []

# This list will continue so users have can have experience with nearly endless social causes.

# Generate query template
def tweet_query_generator(kwd, data):
    for tweet in tweepy.Cursor(api.search, q=kwd, lang='en', result_type='popular').items(30):
        data.append(tweet)


# Generate query for each topic
# Cannot go over 500 hits in a day
def get_all_tweet_queries(use_list, tweetdata):
    count = 0
    for item in use_list:
        count += 1
        tweet_query_generator(item, tweetdata)


# Function to convert a given list of tweets into a Pandas DataFrame.
def tweettoDataFrame(tweets, list_name):
    DataSet = pd.DataFrame()

    DataSet['tweetID'] = [tweet.id for tweet in tweets]
    DataSet['tweetText'] = [tweet.text for tweet in tweets]
    DataSet['tweetRetweetCt'] = [tweet.retweet_count for tweet in tweets]
    DataSet['tweetFavoriteCt'] = [tweet.favorite_count for tweet in tweets]
    DataSet['tweetCreated'] = [tweet.created_at for tweet in tweets]
    DataSet['userScreen'] = [tweet.user.screen_name for tweet in tweets]
    DataSet['userName'] = [tweet.user.name for tweet in tweets]
    DataSet['userLocation'] = [tweet.user.location for tweet in tweets]
    DataSet['cause'] = [list_name[0] for tweet in tweets]
    # this needs to be set to the name of the list but having trouble so just tagging with
    # the first index

    return (DataSet)

# Function to create a dataframe depending on the keyword list provided.
def CreateTweetdf(key_list, tweetdata):
    get_all_tweet_queries(key_list, tweetdata)
    Tweet_DF = tweettoDataFrame(tweetdata, key_list)
    Tweet_DF.drop_duplicates().sort_values(by=['tweetCreated'], ascending=False)
    return (Tweet_DF)

#Race Tweets
race_tw_df = CreateTweetdf(race_list,race_tweet_data)

# Environment Tweets
env_tw_df = CreateTweetdf(environment_list,environment_tweet_data)

# Current Tweets
cur_tw_df = CreateTweetdf(current_list,current_tweet_data)

# LGBT Tweets
lgbt_tw_df = CreateTweetdf(lgbt_list,lgbt_tweet_data)

# Poverty Tweets
pov_tw_df = CreateTweetdf(poverty_list,poverty_tweet_data)

# Refugee Tweets
ref_tw_df = CreateTweetdf(refugee_list,refugee_tweet_data)

# Womens Rights Tweets
wom_tw_df = CreateTweetdf(women_list,women_tweet_data)

# Addictions Tweets
add_tw_df = CreateTweetdf(mental_list,mental_tweet_data)

# Mental Health Tweets
men_tw_df = CreateTweetdf(mental_list,mental_tweet_data)

# Disability Tweets
dis_tw_df = CreateTweetdf(disability_list,disability_tweet_data)

# Create 1 Df with all tweets
frames = [race_tw_df, env_tw_df, cur_tw_df, lgbt_tw_df, pov_tw_df, ref_tw_df, wom_tw_df, men_tw_df, add_tw_df, dis_tw_df]
all_tw_df = pd.concat(frames)

# Read CSV into dataframe
twitter_db = pd.read_csv('../csv/twitter_api.csv')

# Remove CSV with plan to re-add after updating. This is so that
os.remove('../csv/twitter_api.csv')

# Update dataframe with new tweets
frames = [twitter_db,all_tw_df]
Updated_twitter_dataframe = pd.concat(frames).drop_duplicates()

# Recreate same csv and use flask call to update db.
# Will allow for update on startup of application
Updated_twitter_dataframe.to_csv ('twitter_api.csv', index = False, header=True)

# basedir    = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../../db.sqlite3')
# engine = create_engine(SQLALCHEMY_DATABASE_URI)
#
#
# file_name = '../csv/twitter_api.csv'
# Updated_twitter_dataframe = pd.read_csv(file_name)
Updated_twitter_dataframe.to_sql(con=engine, index_label='id', name=db.__tablename__, if_exists='replace')

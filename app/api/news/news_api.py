from newsapi.newsapi_client import NewsApiClient
import sys
import pandas as pd
import itertools
import tweepy

# Credentials for APIs

# NewsAPI
newsapi = NewsApiClient(api_key="82a3d51da38f4c48ae8a375ab0246e80")
news_sources = newsapi.get_sources()

# Cannot go over 500 hits in a day. 1 hit for every permutation.

# Race
race_list = ['black lives matter', 'racial inequity', 'racial oppression']
race_news_data = []

# Environment
environment_list = ['climate change', 'sustainability', 'green energy', 'global warming']
environment_news_data = []

# Addiction
addiction_list = ['drug addiction', 'alcohol addiction']
addiction_news_data = []

# Current Hot Topics
current_list = ['india farmers', 'myanmar', 'asian-american hate']
current_news_data = []

# LGBT
lgbt_list = ['lgbt rights', 'gay rights', 'transgender rights', 'gay marriage']
lgbt_news_data = []

# Poverty
poverty_list = ['poverty', 'homeless right']
poverty_news_data = []

# Refugee
refugee_list = ['refugee rights']
refugee_news_data = []

# Womens Rights
women_list = ['female wages', 'womens rights']
women_news_data = []

# Mental Health
mental_list = ['mental health', 'mental illness', 'coping with mental illness', 'living with anxiety']
mental_news_data = []

# Disability rights
disability_list = ['Disability rights']
disability_news_data = []


# Generate query template
def query_generator(kwd, data):
    all_articles = newsapi.get_everything(
        q=kwd,
        language='en',
    )
    for article in all_articles['articles']:
        data.append([article['source']['name'], article['title'], article['author'],
                     article['description'], article['publishedAt'], article['url'], article['urlToImage'],
                     article['content']])


# Generate query for each permutation
def get_all_article_queries(use_list, newsdata):
    for item in use_list:
        query_generator(item, newsdata)


# Function to create dataframe for articles from each topic area
def CreateArticledf(key_list, newsdata):
    news_col_names = ['Source', 'Title', 'Author', 'Description', 'Pub_Date', 'url', 'urlToImage', 'Content']
    get_all_article_queries(key_list, newsdata)
    News_DF = pd.DataFrame(newsdata, columns=news_col_names)
    News_DF.drop_duplicates().sort_values(by=['Pub_Date'], ascending=False)
    return (News_DF)

#Race Tweets
race_art_df = CreateArticledf(race_list,race_news_data)

#Environment Tweets
env_art_df = CreateArticledf(environment_list,environment_news_data)

#Current Tweets
cur_art_df = CreateArticledf(current_list,current_news_data)

#LGBT Tweets
lgbt_art_df = CreateArticledf(lgbt_list,lgbt_news_data)

#Poverty Tweets
pov_art_df = CreateArticledf(poverty_list,poverty_news_data)

#Refugee Tweets
ref_art_df = CreateArticledf(refugee_list,refugee_news_data)

#Womens Rights Tweets
wom_art_df = CreateArticledf(women_list,women_news_data)

#Mental Health Tweets
men_art_df = CreateArticledf(mental_list,mental_news_data)

#Disability Tweets
dis_art_df = CreateArticledf(disability_list,disability_news_data)
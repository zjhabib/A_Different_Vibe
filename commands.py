import click
from flask import Blueprint
from flask import current_app
from app import db
import pandas as pd
import os
import re

commands = Blueprint('commands', __name__)

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
engine = create_engine(SQLALCHEMY_DATABASE_URI)

@commands.cli.command('update_db')
def update_db():

    file_name = 'app/api/csv/twitter_api.csv'
    Updated_twitter_dataframe = pd.read_csv(file_name)
    Updated_twitter_dataframe.to_sql(con=engine, index_label='id', name=db.__tablename__, if_exists='replace')
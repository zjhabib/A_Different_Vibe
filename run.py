# -*- encoding: utf-8 -*-

from flask_migrate import Migrate
from os import environ
from sys import exit
from decouple import config
import logging
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from config import config_dict
from app import create_app, db



# WARNING: Don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:
    
    # Load the configuration using the default values 
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

# the toolbar is only enabled in debug mode:

app = create_app( app_config )
Migrate(app, db)

app.debug = True
app.config['SECRET_KEY']
toolbar = DebugToolbarExtension(app)
toolbar.init_app(app)

if DEBUG:
    app.logger.info('DEBUG       = ' + str(DEBUG)      )
    app.logger.info('Environment = ' + get_config_mode )
    app.logger.info('DBMS        = ' + app_config.SQLALCHEMY_DATABASE_URI )

if __name__ == "__main__":
    app.run()

import os
import praw
import pandas as pd
import datetime as dt
from dotenv import load_dotenv
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

load_dotenv()

#Getting data from .env (Developer application info. Check README)
reddit_api_key = os.getenv('reddit_api_key', default = 'Not found')
reddit_api_secret = os.getenv('reddit_api_secret', default = 'Not found')
app_name = os.getenv('app_name', default = 'Not found')
user_name = os.getenv('user_name', default = 'Not found')
login_password = os.getenv('login_password', default = 'Not found')

#Accessing the Reddit API
reddit = praw.Reddit(client_id = reddit_api_key,
                     client_secret = reddit_api_secret,
                     user_agent = app_name,
                     username = user_name,
                     password = login_password
)


#Flask app (Just returns 'Hello World')
@app.route('/')
def index():
    return 'Hello World'

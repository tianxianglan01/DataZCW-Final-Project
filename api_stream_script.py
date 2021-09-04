import tweepy

from sqlite3 import connect
from os.path import isfile
from os import access, R_OK
from api_keys import consumer_key, consumer_secret, access_token, access_token_secret
# access and R_OK is just to test the readabilit of a path
from sys import exit

db_file = "/Users/sean/labs/Capstone/covid_19_tweets.db"

def oauth_authenticate():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)

def check_path(path):
    return isfile(path) and access(path, R_OK)

def db_connect(sqlite_file):
    return connect(sqlite_file)

def create_db(sqlite_file):
    conn = connect(sqlite_file)

    # user.screen_name (VARCHAR)
    # created_at (DATETIME)
    # text (VARCHAR)
    # user.location (VARCHAR)
    # retweeted (boolean)

    create_table = 'CREATE TABLE tweets('
    create_table += 'screen_name VARCHAR(255), '
    create_table += 'created_at DATETIME, '
    create_table +='text VARCHAR(255), '
    create_table += 'user_location VARCHAR(255), '
    create_table += 'retweeted INTEGER'
    create_table += (')')

    conn.cursor().execute(create_table)
    conn.commit()
    conn.close()

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        screen_name = status.user.screen_name
        created_at = status.created_at
        text = status.text
        retweet = status.retweeted


if __name__ == "__main__":
    api = oauth_authenticate()

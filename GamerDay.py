import tweepy
import json
import os
from datetime import datetime


def get_key(key):
    # Gets API key from local file.
    os.chdir("c:/users/bill/documents")
    secrets_filename = 'gamerkey.txt'
    with open(secrets_filename, 'r') as f:
        api_key = json.loads(f.read())
    return api_key[key]


def connect_twitter():
    # Initiate connection to Twitter API.
    auth = tweepy.OAuthHandler(get_key('TWITTER_API_KEY'), get_key('TWITTER_API_SECRET'))
    auth.set_access_token(get_key('TWITTER_ACCESS_TOKEN'), get_key('TWITTER_ACCESS_SECRET'))
    return tweepy.API(auth)


def main():
    # Initiate API connection.
    twitter = connect_twitter()

    # Get day, tweet that shit.
    today = datetime.today().strftime('%A').lower()
    twitter.update_status(f"gamer {today}")


if __name__ == "__main__":
    main()

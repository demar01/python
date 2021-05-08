import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    '''
    This code uses os.getenv() to read environment variables and then creates the Tweepy auth object. Then the API object is created.
    '''
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    # wait_on_rate_limit and wait_on_rate_limit_notify in the creation of the tweepy.API object makes Tweepy wait and print a message when the rate limit is exceeded.
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
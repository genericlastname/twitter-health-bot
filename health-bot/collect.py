import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

# constants
_max_tweets = 100


def init():
    consumer_key = 'wka2iuZW3Aky7SFhwA8PhAGnl'
    consumer_secret = 'Swqq8AgjFRnKTEg3gmyBJDUZ8fnzqdfhfDirhn8owj0czog2vf'
    access_token = '869984091692822528-ykmxl5GO0FnISwSXjLMGmTC6FOvmgkU'
    access_secret = 'vUR9RmBvmAu5EJI2ijZKHBFfJafMpkI6EoDxulNvsigK5'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    return tweepy.API(auth)


class HealthListener(StreamListener):
    def __init__(self):
        self.tweet_num = 1

    def on_data(self, data):
        tweet = json.loads(data)
        text = tweet['text']
        print('Tweet #{}: {}'.format(self.tweet_num, text))

        self.tweet_num += 1
        return True

    def on_error(self, status):
        print(status)
        return True


def collect(api, query):
    tweets = [
            status for status in
            tweepy.Cursor(api.search, q=query).items(_max_tweets)
            ]
    return tweets

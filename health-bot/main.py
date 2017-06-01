import tweepy
from tweepy import OAuthHandler
import json
from nltk.tokenize import word_tokenize


path = 'tweet_data.json'
file = open(path, 'w+')


def dump_data(tweet):
    #file.write(json.dumps(tweet))
    file.write(tweet)
    file.write('\n')


def collect_tweets():
    consumer_key = 'wka2iuZW3Aky7SFhwA8PhAGnl'
    consumer_secret = 'Swqq8AgjFRnKTEg3gmyBJDUZ8fnzqdfhfDirhn8owj0czog2vf'
    access_token = '869984091692822528-ykmxl5GO0FnISwSXjLMGmTC6FOvmgkU'
    access_secret = 'vUR9RmBvmAu5EJI2ijZKHBFfJafMpkI6EoDxulNvsigK5'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    print('Using file {}'.format(path))

    for tweet in tweepy.Cursor(api.home_timeline).items(10):
        dump_data(tweet.text)

    file.close()


def tokenize_tweets():
    with open(path, 'r') as f:
        line = f.readline()
        print(word_tokenize(line))

        f.close()


if __name__ == '__main__':
    collect_tweets()
    tokenize_tweets()

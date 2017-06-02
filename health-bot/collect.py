import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# constants
_max_tweets = 500


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
        self.tweet_num = 0
        self.f = open('tweets.json', 'w+')

    def on_data(self, data):

        if self.tweet_num < _max_tweets:
            # Continue writing to file
            self.f.write(data)
            print('{} tweet(s) collected'.format(self.tweet_num+1))

            self.tweet_num += 1
        else:
            self.f.close()
            print('Finished. Ending stream...')
            return False  # finish

    def on_error(self, status):
        print(status)
        return True

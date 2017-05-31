import tweepy
from tweepy import OAuthHandler


def main():
    consumer_key = 'wka2iuZW3Aky7SFhwA8PhAGnl'
    consumer_secret = 'Swqq8AgjFRnKTEg3gmyBJDUZ8fnzqdfhfDirhn8owj0czog2vf'
    access_token = '869984091692822528-ykmxl5GO0FnISwSXjLMGmTC6FOvmgkU'
    access_secret = 'vUR9RmBvmAu5EJI2ijZKHBFfJafMpkI6EoDxulNvsigK5'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    for status in tweepy.Cursor(api.home_timeline).items(10):
        print(status.text)


if __name__ == '__main__':
    main()

from collect import init
from collect import HealthListener
from tweepy import Stream


if __name__ == '__main__':
    api = init()

    keywords = [
            'starbucks',
            'little ceasar\'s',
            'domino\'s',
            'subway',
            'dunkin donuts',
            'pizza hut',
            'papa john\'s',
            'panera bread',
            'chipotle',
            'chick fil a',
            ]
    # start stream
    health_stream = Stream(api.auth, HealthListener())
    health_stream.filter(track=keywords)

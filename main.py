from collect import init
from collect import HealthListener
from tweepy import Stream


def collect():
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
    location = [-91.7468, 30.1594, -88.0554, 35.0165]

    # start stream
    health_stream = Stream(api.auth, HealthListener())
    health_stream.filter(track=keywords, locations=location)


if __name__ == '__main__':
    collect()

from collect import init
from collect import HealthListener
from tweepy import Stream


api = init()

if __name__ == '__main__':
    health_stream = Stream(api.auth, HealthListener())
    health_stream.filter(track=['#NationalDonutDay'])

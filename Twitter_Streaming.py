# Python file to collect and store a stream of tweets

# Import Libraries
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

# Authentification
consumer_key = 'gSmxxxxxxxxxx'
consumer_secret = 'lkHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token = '788xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_secret = '0f9xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
# Create a Listener that prints the received tweets
class MyListener(StreamListener):
 
    def on_data(self, data):
        print(data)
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
# Connect to Twitter Streaming API and filter tweets 
stream = Stream(auth, MyListener())

keywords = ['xxxxx', 'xxxxxxxx', 'xxxxxx']

stream.filter(track=keywords)

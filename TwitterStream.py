
# coding: utf-8

# In[1]:

import tweepy
from tweepy import OAuthHandler
import codecs
from time import time, sleep


# In[2]:

consumer_key = 'jmCRzWWRZjuhNo5Q2gHUXpOGd'
consumer_secret = '1wxvlRAjjRcP9TIuE2wnI7LlJ32pkxEc21wMkghMULNLCtKUyD'
access_token = '794344198312849408-vknnh03URiVLo4ijoNGYxYN7ZAmjYxB'
access_secret = 'PxWES0uBWpw7EcEv7IhG18kWn9yB8Kqsmwn6GbfwMRhrH'


# In[3]:
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    # dic = list()
    # with open("dict_twitter","r+",encoding="utf8") as test:



    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    # stream.filter(track=dic, async=True)
    stream.filter(track=['ดี'], async=True)
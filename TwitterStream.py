
# coding: utf-8

# In[1]:

import tweepy
from tweepy import OAuthHandler
import codecs
import time
from datetime import date, datetime
import json

# In[2]:

consumer_key = 'jmCRzWWRZjuhNo5Q2gHUXpOGd'
consumer_secret = '1wxvlRAjjRcP9TIuE2wnI7LlJ32pkxEc21wMkghMULNLCtKUyD'
access_token = '794344198312849408-vknnh03URiVLo4ijoNGYxYN7ZAmjYxB'
access_secret = 'PxWES0uBWpw7EcEv7IhG18kWn9yB8Kqsmwn6GbfwMRhrH'


# In[3]:
class StdOutListener(tweepy.StreamListener):

    def on_data(self, data):
        decoded = json.loads(data)
        del decoded['in_reply_to_status_id']
        del decoded['in_reply_to_status_id_str']
        del decoded['filter_level']
        del decoded['truncated']
        del decoded['lang']
        del decoded['in_reply_to_screen_name']
        del decoded['in_reply_to_user_id']
        del decoded['favorited']
        del decoded['geo']
        del decoded['source']
        del decoded['place']
        del decoded['in_reply_to_user_id_str']
        del decoded['id_str']
        del decoded['contributors']
        del decoded['entities']['urls']
        del decoded['user']['profile_background_tile']
        del decoded['user']['profile_link_color']
        del decoded['user']['url']
        del decoded['user']['default_profile_image']
        del decoded['user']['protected']
        del decoded['user']['geo_enabled']
        del decoded['user']['notifications']
        del decoded['user']['utc_offset']
        del decoded['user']['profile_background_image_url']
        del decoded['user']['profile_background_color']
        del decoded['user']['time_zone']
        del decoded['user']['description']
        del decoded['user']['profile_sidebar_fill_color']
        del decoded['user']['follow_request_sent']
        del decoded['user']['is_translator']
        del decoded['user']['favourites_count']
        del decoded['user']['profile_image_url']
        del decoded['user']['profile_use_background_image']
        del decoded['user']['profile_text_color']
        del decoded['user']['profile_background_image_url_https']
        del decoded['user']['listed_count']
        del decoded['user']['verified']
        del decoded['user']['id_str']
        del decoded['user']['profile_image_url_https']
        del decoded['user']['contributors_enabled']
        del decoded['user']['profile_sidebar_border_color']
        del decoded['user']['default_profile']
        decoded['user']['created_at'] = time.mktime(datetime.strptime(decoded['user']['created_at'],'%a %b %d %H:%M:%S %z %Y').timetuple())
        print(x)
        if not decoded['retweeted']:
            print(json.dumps(decoded),"\n")
            return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = tweepy.Stream(auth, l)
    # dic = list()
    # with open("dict_twitter","r+",encoding="utf8") as test:



    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    # stream.filter(track=dic, async=True)
    stream.filter(track=['แอพเด็กดี','เว็บเด็กดี','เว็ปเด็กดี','ในเด็กดี','นิยายเด็กดี','งานเด็กดี','ควิซเด็กดี','admissionเด็กดี','คะแนนเด็กดี','Quizเด็กดี','เม้นเด็กดี','ทวิตด็กดี','เข้าเด็กดี','Dek-D','Dekd','dekd','เว็บสีส้ม','เว็ปสีส้ม','คำนวนคะแนนAdmission','คำนวนคะแนน Admission','พี่ลาเต้','ลาเต้เด็กดี'])
import tweepy
from tweepy import OAuthHandler
import codecs
import time
from datetime import date, datetime
import json

consumer_key = 'jmCRzWWRZjuhNo5Q2gHUXpOGd'
consumer_secret = '1wxvlRAjjRcP9TIuE2wnI7LlJ32pkxEc21wMkghMULNLCtKUyD'
access_token = '794344198312849408-vknnh03URiVLo4ijoNGYxYN7ZAmjYxB'
access_secret = 'PxWES0uBWpw7EcEv7IhG18kWn9yB8Kqsmwn6GbfwMRhrH'

class StdOutListener(tweepy.StreamListener):

    def on_data(self, data):
        decoded = json.loads(data)
        if not decoded['retweeted'] and 'RT @' not in decoded['text']:
            buf = dict()
            decoded['user']['created_at'] = time.mktime(datetime.strptime(decoded['user']['created_at'],'%a %b %d %H:%M:%S %z %Y').timetuple())
            buf.update(
            {
                "user_id": decoded['user']['id'],
                "user_name": str(decoded['user']['name']),
                "user_screenname": str(decoded['user']['screen_name']),
                "user_friend": decoded['user']['friends_count'],
                "user_follower": decoded['user']['followers_count'],
                "user_lang": decoded['user']['lang'],
                "user_status": decoded['user']['statuses_count'],
                "user_create": str(decoded['user']['created_at']),
                "post_id": decoded['id'],
                "post_create": decoded['timestamp_ms']
            }
            )
            if 'quoted_status' in decoded:
                if 'extended_tweet' in decoded['quoted_status']:
                    buf.update(
                {
                    "quoted": str(decoded['quoted_status']['extended_tweet']['text'])
                }
                )
                else:
                    buf.update(
                {
                    "quoted": str(decoded['quoted_status']['text'])
                }
                )
            else:
                buf.update(
                {
                    "quoted": "Null"
                }
                )
            
            if 'extended_tweet' in decoded:
                buf.update(
                {
                    "text": str(decoded['extended_tweet']['full_text'])
                }
                )
            else:
                buf.update(
                {
                    "text": str(decoded['text'])
                }
                )
            if len(decoded['entities']['hashtags']) > 0:
                x = ""
                for i in range(len(decoded['entities']['hashtags'])-1):
                    x += decoded['entities']['hashtags'][i]['text'] + ","
                x += decoded['entities']['hashtags'][len(decoded['entities']['hashtags'])-1]['text']
                buf.update(
                {
                    "hashtags": str(x)
                }
                )
            else:
                buf.update(
                {
                    "hashtags": "Null"
                }
                )
            with codecs.open("Result.txt","a","utf-8") as test:
                test.write(json.dumps(buf))
            del buf
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['555'])

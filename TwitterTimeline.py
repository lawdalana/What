
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

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
buf = set()
listword = []
listusername = []
listuserad = []


# In[4]:

def writefile():
    global buf
    global listword
    global listusername
    global listuserad
    with codecs.open('Text.txt', 'a+', "utf-8") as f:
        for i in range(0,len(listword)):
            f.write(listusername[i]+ ",;," +listuserad[i]+ ",;," +listword[i]+ u";,;");
    buf = set()
    if(len(listword)>0):
        buf.add(listword[len(listword)-1])
        listword = []
        listusername = []
        listuserad = []
    
def trusty_sleep(n):
    start = time()
    while (time() - start <= n):
        sleep(3)


# In[6]:

while True:
    try:
        for status in tweepy.Cursor(api.home_timeline).items(400):
            if(status.text not in buf):
                buf.add(status.text)
                listword.append(status.text)
                listusername.append(status.user.name)
                listuserad.append(status.user.screen_name)
            else:
                break
        writefile()
        trusty_sleep(15 * 60)
    except:
        writefile()
        trusty_sleep(15 * 60)


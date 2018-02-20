# -*- coding: utf-8 -*-
import  os, random, time, tweepy

#This code will publish a random tweet from a file
#The file has one tweet written per line (csv or txt)

#Authenticating the access

CONSUMER_KEY = 'AppConsumerKey'
CONSUMER_SECRET = 'AppConsumerSecret'
ACCESS_KEY = 'UserAccessKey'
ACCESS_SECRET = 'UserAccessSecret'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Number of tweets I want to publish and the interval (minutes) between each one of them

numoftweets = 10
interval = 15

#The path of your file, considering it is the same folder than the Python file

path = os.getcwd() + '/yourfile.csv'

#Creating a list with the tweets available in my file

tweets_list = []
f = codecs.open(path, encoding='utf-8')
for line in f:
    tweets_list += [line]
f.close()

#Selecting random tweets from my list

topublish = random.sample(tweets_list, numoftweets)

#Publishing tweets

for tweet in topublish:
  api.update_status(tweet)
  print 'Published: ' + str(tweet)
  time.sleep(interval * 60)

# -*- coding: utf-8 -*-
import tweepy, time, unicodedata

#This code will delete the tweets that contain/don't contain certain texts

#Authenticating the access

CONSUMER_KEY = 'AppConsumerKey'
CONSUMER_SECRET = 'AppConsumerSecret'
ACCESS_KEY = 'UserAccessKey'
ACCESS_SECRET = 'UserAccessSecret'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#words list that will filter your tweets

words = ['Filter', 'Bot']
        
#This will normalize the text 

def textnormalizer(text):
    return ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))

#This function will delete the filtered tweets
#to delete tweets that contain word (including = True)
#to delete tweets that do not contain word (including = False)

def tweetsdeleting(tweets, words, including, waitingtime):
    for tweet in tweets:
        twtxt = tweet.text
        twnorm = textnormalizer(twtxt).lower()
        isornot = False
        for word in words:
            if word.lower() in twnorm:
                isornot = True
                break
        if including == isornot:
            api.destroy_status(int(tweet.id))
            print 'Tweet ' + str(int(tweet.id)) + ' deleted'
        else:
            continue                
        #One second wait between tweets deleted
        time.sleep(waitingtime)
    
#List of tweets, if you want to include RTs change from False to True
status_user = api.user_timeline('YourTwAccount, count = 3200, include_rts = False)

#Delete tweets that contain "filter" or "bot" using the function
tweetsdeleting(status_user, words, True, 1)
#Delete tweets that do not contain "filter" or "bot" using the function
tweetsdeleting(status_user, words, False, 1)

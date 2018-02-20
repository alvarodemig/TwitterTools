# -*- coding: utf-8 -*-
import tweepy

#If you work with multiple Twitter accounts and you want to use your app
#with all of them you need User Access and Access token keys for each of them

#App keys (https://apps.twitter.com/app/yourappid/keys)
CONSUMER_KEY = 'YourAppConsumerKey'
CONSUMER_SECRET = 'YourAppConsumerSecretKey'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

session = dict()
dir(auth)

#redirect_url is the url that you need to visit to authenticate your app in a new account
try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print 'Error! Failed to get request token.'
 
session['request_token'] = auth.request_token

#You need to introduce this url in your browser and accept
print redirect_url  

#Twitter will provide you a code to verify your account. You need to introduce it in Python
verifier = raw_input('Verifier:')

#Requesting and saving your token
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
token = session['request_token']
del session['request_token']
auth.request_token = token

try:
    auth.get_access_token(verifier)
except tweepy.TweepError:
    print 'Error! Failed to get access token.'
    
key = auth.access_token
secret = auth.access_token_secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(key, secret)

#Save the following keys, you will need them to use your app in the account you just associated
print 'KEY --------------------------------------'
print key
print '\nSECRET ---------------------------------'
print secret
print '\n\n'

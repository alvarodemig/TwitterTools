import tweepy, time, unicodedata

#This code will undo the retweets that your account have performed

#Authenticating the access

CONSUMER_KEY = 'AppConsumerKey'
CONSUMER_SECRET = 'AppConsumerSecret'
ACCESS_KEY = 'UserAccessKey'
ACCESS_SECRET = 'UserAccessSecret'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Return TRUE if the tweet is a Retweet and FALSE if it is not
def isretweet(status):
    try:
        isrt = status.retweeted_status
        return True
    except:
        return False
 
#Return the last 1000 published tweets      
status_user = api.user_timeline('YourTwitterAccount', count = 1000, include_rts = True)

#Check if it is a RT and delete it
for tweet in status_user:
    try:
        if isretweet(tweet) == True:
            api.destroy_status(tweet.id)
            print 'Deleted tweet: ' + str(tweet.id)
    except:
        print '----- ERROR DELETING TWEET ' + str(tweet.id) + ' -----'

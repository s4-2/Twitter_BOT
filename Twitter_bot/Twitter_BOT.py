import tweepy
from time import sleep
#from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME

#auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token_key, access_token_secret)
#api=tweepy.API(auth)
twitter_keys = {
    'consumer_key':'xxxxxxxxxxxxxx',
    'consumer_secret':'xxxxxxxxxxxxxx',
    'access_token_key':'xxxxxxxxxxxxxx',
    'access_token_secret':'xxxxxxxxxxxx'
}

auth=tweepy.OAuthHandler(twitter_keys['consumer_key'],twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'],twitter_keys['access_token_secret'])

api=tweepy.API(auth)

print("Twitter bot which retweets, like tweets and follow users")
print("Bot Setting")
print("Like Tweets",LIKE)
print("Follow users",FOLLOW)

for tweet in tweepy.Cursor(api.search,q=QUERY).items():
    try:
        print("\nTweet by: @" + tweet.user.screen_name)

        tweet.retweet()
        print("Retweeted the tweet")

        # Favourite Tweets
        if LIKE:
            tweet.Favourite()
            print("Favourited the tweet")

        # Follow the user who tweeted
        # Check that bot is not already following the user
        if FOLLOW:
            if not tweet.user.following:
                tweet.user.follow()
                print("Followed the user")
        sleep(SLEEP_TIME)

    except tweepy.TweepError as e:
        print(e.reason)
    
    except StopIteration:
        break

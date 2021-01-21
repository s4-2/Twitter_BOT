import tweepy
from time import sleep
#from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME

#auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token_key, access_token_secret)
#api=tweepy.API(auth)
twitter_keys = {
    'consumer_key':'UjnTabcyaFg5jgmr82QYlCdba',
    'consumer_secret':'oM92b48qH5EiSPCl35PfiuAtpzlPrDWpNwguGitz2u1xzNpV7s',
    'access_token_key':'1314298938644549633-JEdgNNtNVyBz9Tj7Wn3fA7De6G1N5v',
    'access_token_secret':'ULNlAuWyaJRCaEKbuPAn78JhbfN45Ly5a1gxzaLQrr3PY'
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
#!/usr/bin/env python3
"""
Component Name: TweetRequestor

Component Purpose: This component will parse the User Preference Database for a list of accounts that MyTwitter users follow. Then it will automatically retrieve recent tweets from those accounts and store it in the Tweet Database for other components to access.
"""

import csv
import requests
import json
import pandas as pd

bearer_token = "AAAAAAAAAAAAAAAAAAAAAL2YVQEAAAAA%2Fad7ErJJAFH0S%2FEtYLnD%2FzGvCm0%3Dxcrv7RU1UCdBlQjq59xg0UEUr113FMURapS37c9prll3pfkkmD"
standardHeader = "Bearer $BEARER_TOKEN"
header = standardHeader.replace('$BEARER_TOKEN', bearer_token)
TweetRequest = "https://api.twitter.com/2/users/user_id/tweets"
FollowingListFile= "../UserPreferenceDatabase/FollowingTable.csv"
TweetTableFile = "../TweetDatabase/TweetTable.csv"
maxNumberOfAccounts = 10 #Use this to not breach the request limit for Twitter APIs

def request_public_metrics(tweet_id):
    tweet_fields = "tweet.fields=public_metrics,author_id,created_at"
    id_template = "ids=tweet_id_here"
    ids = id_template.replace('tweet_id_here', str(tweet_id))
    public_metric_url = "https://api.twitter.com/2/tweets?{}&{}".format(ids, tweet_fields)
    tweetMetrics = requests.get(public_metric_url, headers={"Authorization":header}).json()
    print(tweetMetrics)
    return tweetMetrics

def store_tweets(tweetStats):
    with open(TweetTableFile, "a") as tweetTable:
        for f in range(len(tweetStats['data'])):
            tweetId        = str(tweetStats['data'][f]['id'])
            tweetText      = str(tweetStats['data'][f]['text'])
            tweetAuthor    = str(tweetStats['data'][f]['author_id'])
            tweetTime      = str(tweetStats['data'][f]['created_at'])
            tweetLikes     = str(tweetStats['data'][f]['public_metrics']['like_count'])
            tweetRetweets  = str(tweetStats['data'][f]['public_metrics']['retweet_count'])
            #Remove commas from text for csv storage purposes
            tweetText = tweetText.replace(',', '')
            #Remove newlines for csv storage purposes 
            tweetText = tweetText.replace('\n', '')
            tweetTable.write(tweetId       + "," +
                             tweetAuthor   + "," +
                             tweetTime     + "," + 
                             tweetLikes    + "," + 
                             tweetRetweets + "," +
                             tweetText     + "\n") 
    tweetTable.close()
    return 0

def parse_tweets(tweetList):
    print ("Processing " + str(range(len(tweetList['data']))) + " tweets...")
    for f in range(len(tweetList['data'])):
        tweetId     = tweetList['data'][f]['id']
        tweetText   = tweetList['data'][f]['text']
        tweetStats = request_public_metrics(tweetId)
        store_tweets(tweetStats)

print('Reading Following Table...')
df = pd.read_csv(FollowingListFile) 
df1 = df['FollowingId']
   
print('Retrieving Tweets from Accounts Listed')

n=1
for key, followingId in df1.iteritems():
    print(followingId)
    url = TweetRequest.replace('user_id', str(followingId))
    accountTweetList = requests.get(url, headers={"Authorization":header}).json()
    print(accountTweetList)
    parse_tweets(accountTweetList)
    if n > maxNumberOfAccounts:
        break
    else:
        n=n+1


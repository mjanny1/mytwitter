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

def request_public_metrics(tweet_id):
    tweet_fields = "tweet.fields=public_metrics,author_id,created_at"
    id_template = "ids=tweet_id_here"
    ids = id_template.replace('tweet_id_here', str(tweet_id))
    public_metric_url = "https://api.twitter.com/2/tweets?{}&{}".format(ids, tweet_fields)
    tweetMetrics = requests.get(public_metric_url, headers={"Authorization":header}).json()
    print(tweetMetrics)
    return tweetMetrics

def parse_tweets(tweetList):
    for f in range(len(tweetList['data'])):
        tweetId     = tweetList['data'][f]['id']
        tweetText   = tweetList['data'][f]['text']
        print('Tweet ID: ' + str(tweetId) + '. Tweet Text: ' + str(tweetText))
        request_public_metrics(tweetId)

#def store_tweets(tweetList):


print('Reading Following Table...')
df = pd.read_csv(FollowingListFile) 
df1 = df['FollowingId']
   
print('Retrieving Tweets from Accounts Listed')
for key, followingId in df1.iteritems():
    print(followingId)
    url = TweetRequest.replace('user_id', str(followingId))
    accountTweetList = requests.get(url, headers={"Authorization":header}).json()
    print(accountTweetList)
    parse_tweets(accountTweetList)
    break

#            print ("User has " + str(len(followingListDict['data'])) + " followers")
#    if 'errors' not in response.keys():
#        num_users += 1
#        response = response['data']
#        for tweet in response:
#            num_tweets += 1
#            author_info = [following_user_dict[following_user_id]['name'], following_user_dict[following_user_id]['username'], following_user_dict[following_user_id]['verified']]
#            csvWriter.writerow([tweet[key] for key in good_keys]+author_info)
#            print(f'Created timeline_{target_user_id}.csv with {num_tweets} tweets from {num_users} users') 
#            tweets_file.close()



#        if 'errors' not in response.keys():
#            num_users += 1
#            response = response['data']
#            for tweet in response:
#                num_tweets += 1
#                author_info = [following_user_dict[following_user_id]['name'], following_user_dict[following_user_id]['username'], following_user_dict[following_user_id]['verified']]
#                csvWriter.writerow([tweet[key] for key in good_keys]+author_info)


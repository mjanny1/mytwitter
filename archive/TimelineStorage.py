#!/usr/bin/env python
# coding: utf-8

import socket
import requests
import csv
import json

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT =  12347       # Port to listen on (non-privileged ports are > 1023)

# fields used when pulling the user
tweet_fields = 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,reply_settings,source,text,withheld'
tweet_results = 10

good_keys = ['author_id', 'id', 'created_at', 'text', 'public_metrics', 'source', 'lang', 'conversation_id', 'reply_settings', 'possibly_sensitive']


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = access_token
    return r

# Represents the app and enables us to authenticate requests that require OAuth 2.0 authentication
bearer_token = "AAAAAAAAAAAAAAAAAAAAAL2YVQEAAAAA%2Fad7ErJJAFH0S%2FEtYLnD%2FzGvCm0%3Dxcrv7RU1UCdBlQjq59xg0UEUr113FMURapS37c9prll3pfkkmD"

# token that represents the twitter account that owns the app
access_token = "2736768003-shFrt7F6HpKfpXgCmVOvvgE8cV1Sz76DYtlHB7K"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print ("Listening...")
    s.listen()
    conn, addr = s.accept()
    print ("Connection Found!")
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(8192)
            if data:
                break

data = json.loads(data)
target_user_id, following_user_dict = data['id'], data['following']

tweets_querystring = {"max_results":tweet_results, "tweet.fields": tweet_fields}

num_users, num_tweets = 0, 0

with open(f'timeline_{target_user_id}.csv', 'w', newline='', encoding='UTF-8') as tweets_file:
    csvWriter = csv.writer(tweets_file)
    csvWriter.writerow(good_keys+['author_name', 'author_username', 'author_verified'])

    for following_user_id in list(following_user_dict.keys()):
        following_tweets_url = f"https://api.twitter.com/2/users/{following_user_id}/tweets"

        response = requests.request("GET", following_tweets_url, params=tweets_querystring, auth=bearer_oauth).json()
        
        if 'errors' not in response.keys():
            num_users += 1
            response = response['data']
            for tweet in response:
                num_tweets += 1
                author_info = [following_user_dict[following_user_id]['name'], following_user_dict[following_user_id]['username'], following_user_dict[following_user_id]['verified']]
                csvWriter.writerow([tweet[key] for key in good_keys]+author_info)
print(f'Created timeline_{target_user_id}.csv with {num_tweets} tweets from {num_users} users') 
tweets_file.close()
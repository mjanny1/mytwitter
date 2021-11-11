#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from uuid import uuid4
import requests

# Represents the app and enables us to authenticate requests that require OAuth 2.0 authentication
bearer_token = "AAAAAAAAAAAAAAAAAAAAAL2YVQEAAAAA%2Fad7ErJJAFH0S%2FEtYLnD%2FzGvCm0%3Dxcrv7RU1UCdBlQjq59xg0UEUr113FMURapS37c9prll3pfkkmD"
app_id = 22386877

# Username to make a request on behalf of the app
consumer_key = "KYD8pBfiM1hzYkzveTcDC2ztR"
# Password to make a request on behalf of the app:
consumer_secret = "bh6bZOu62DSVfNi2fhbWQAcrXMFwO8nZySWtYQW3IoF69cww82"

# token that represents the twitter account that owns the app
access_token = "2736768003-shFrt7F6HpKfpXgCmVOvvgE8cV1Sz76DYtlHB7K"
# token that represents the twitter account taht owns the app
token_secret = "ismP5fNqdO6gNxYphMcIGrbJs12IpKt0ROGXUl5yib8aD"

tweet_fields = 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,reply_settings,source,text,withheld'


# In[ ]:


rand_token = str(uuid4())

querystring = {"tweet.fields": tweet_fields}

headers = {
    "oauth_consumer_key" : consumer_key,
    "oauth_nonce" : rand_token,
    "access_token": access_token,
    "token_secret": token_secret
}


# In[ ]:


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = access_token
    return r


# In[ ]:


url = f"https://api.twitter.com/2/users/{app_id}/tweets"

response = requests.request("GET", url, params=querystring, auth=bearer_oauth)


# In[ ]:


for key in list(response.json()['data'][0].keys()):
    print(f'{key}: {response.json()["data"][0][key]}')
    print()


# In[ ]:


for tweet in response.json()['data']:
    print('id:', tweet['id'])
    print(tweet['text'])
    print()


# In[ ]:





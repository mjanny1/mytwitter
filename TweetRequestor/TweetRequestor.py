#!/usr/bin/env python3

import csv
import requests
import socket
import json
import numpy as np
import pandas as pd

bearer_token = "AAAAAAAAAAAAAAAAAAAAAL2YVQEAAAAA%2Fad7ErJJAFH0S%2FEtYLnD%2FzGvCm0%3Dxcrv7RU1UCdBlQjq59xg0UEUr113FMURapS37c9prll3pfkkmD"
standardHeader = "Bearer $BEARER_TOKEN"
UserIdRequest = "https://api.twitter.com/2/users/by/username/TwitterDev"
FollowingRequest= "https://api.twitter.com/2/users/:id/following"
FollowingListFile= "./FollowingTable.csv"

#HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
#PORT =  12346       # Port to listen on (non-privileged ports are > 1023)

print('Reading Following Table...')
df = pd.read_csv("../UserPreferenceDatabase/FollowingTable.csv") 
df1 = df['FollowingId']
   
print('Retrieving Tweets from Accounts Listed')
for key, value in df1.iteritems():
    print(value)

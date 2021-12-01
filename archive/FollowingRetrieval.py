#!/usr/bin/env python
# coding: utf-8

import socket
import requests
import json

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT =  12346       # Port to listen on (non-privileged ports are > 1023)

# fields used when pulling the user
users_fields = "id,name,username,verified"
users_results = 50


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
            data = conn.recv(1024)
            if not data:
                break

            target_user_id = str(data)
            target_user_id = target_user_id.replace('b\'', '').replace("\\n\'", '').replace('\'', '')

users_querystring = {"max_results": users_results, "user.fields":users_fields}

following_url = f"https://api.twitter.com/2/users/{target_user_id}/following"
following_users = requests.request("GET", following_url, params=users_querystring, auth=bearer_oauth).json()

following_user_dict = {following_user['id']: following_user for following_user in following_users['data']}
data_send = json.dumps({'id': target_user_id, 'following': following_user_dict})

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT+1))
    print("Connected!")
    s.send(data_send.encode())
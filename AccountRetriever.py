#!/usr/bin/env python3

import requests
import socket
import json

bearer_token = "AAAAAAAAAAAAAAAAAAAAAL2YVQEAAAAA%2Fad7ErJJAFH0S%2FEtYLnD%2FzGvCm0%3Dxcrv7RU1UCdBlQjq59xg0UEUr113FMURapS37c9prll3pfkkmD"
standardHeader = "Bearer $BEARER_TOKEN"
UserIdRequest = "https://api.twitter.com/2/users/by/username/TwitterDev"

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT =  12345       # Port to listen on (non-privileged ports are > 1023)

# Input Twitter Handle to retrieve that account's ID from Twitter APIs
def getUserID(username):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}

    print('Getting ID for username: ' + str(username))
    url = UserIdRequest.replace('TwitterDev', username)
    header = standardHeader.replace('$BEARER_TOKEN', bearer_token)
    response = requests.get(url, headers={"Authorization":header})
    print(response.json())
    return response.json()

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
            datastring = str(data)
            print (datastring)
            datastring = datastring.replace('b\'', '').replace("\\n\'", '').replace('\'', '')
            print (datastring)
            zero = getUserID(datastring)

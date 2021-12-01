#!/usr/bin/env python3
"""
Component Name: AccountRetriever

Component Purpose: This component receives the name of the new MyTwitter user's Twitter handle and retrieves a list of the accounts that person follows. It then saves the list of accounts to the Following Table in the User Preference Database
"""

import requests
import socket
import json

bearer_token = "AAAAAAAAAAAAAAAAAAAAAL2YVQEAAAAA%2Fad7ErJJAFH0S%2FEtYLnD%2FzGvCm0%3Dxcrv7RU1UCdBlQjq59xg0UEUr113FMURapS37c9prll3pfkkmD"
standardHeader = "Bearer $BEARER_TOKEN"
UserIdRequest = "https://api.twitter.com/2/users/by/username/TwitterDev"
FollowingRequest= "https://api.twitter.com/2/users/:id/following"
FollowingListFile= "./FollowingTable.csv"

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT =  12345       # Port to listen on (non-privileged ports are > 1023)

# Input Twitter Handle to retrieve that account's ID from Twitter APIs
def getUserID(username):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    print('Getting ID for username: ' + str(username))
    url = UserIdRequest.replace('TwitterDev', username)
    header = standardHeader.replace('$BEARER_TOKEN', bearer_token)
    response = requests.get(url, headers={"Authorization":header})
    #print(response.json())
    return response.json()

def getFollowingList(userId):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    print('Getting Following List for user: ' + str(userId))
    url = FollowingRequest.replace(':id', str(userId))
    header = standardHeader.replace('$BEARER_TOKEN', bearer_token)
    response = requests.get(url, headers={"Authorization":header})
    #print(response.json())
    return response.json()

def saveFollowingList(UserId, UserName, UserHandle, FollowingListDict):
    with open(FollowingListFile, "a") as followingTable:
        for f in range(len(followingListDict['data'])):
            print(followingListDict['data'][f]['id'])
            followingId     = followingListDict['data'][f]['id']
            followingName   = followingListDict['data'][f]['name']
            followingHandle = followingListDict['data'][f]['username']
            #Remove any commas for csv storage purposes
            followingName = followingName.replace(',', '')
            #Remove newlines for csv storage purposes
            followingName = followingName.replace('\n', '')
            followingTable.write(UserId          + "," +
                                 UserName        + "," +
                                 UserHandle      + "," + 
                                 followingId     + "," + 
                                 followingName   + "," + 
                                 followingHandle + "\n")
    return 0
    

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
            datastring = datastring.replace('b\'', '').replace("\\n\'", '').replace('\'', '')
            print ("Message Received: \"" + datastring + "\"")
            userIdDict = getUserID(datastring)
            print (userIdDict['data']['id'])

            userId     = userIdDict['data']['id']
            userName   = userIdDict['data']['name']
            userHandle = userIdDict['data']['username']

            followingListDict = getFollowingList(userId) 
            print ("User has " + str(len(followingListDict['data'])) + " followers")
            zero = saveFollowingList(userId, userName, userHandle, followingListDict)
            #print (followingListDict['data']['id[]'])
            
            #for s in range(len(students)):
            #if students[s]["name"] == to_find:
            #print("The age of {} is {}.".format(students[s]["name"], students[s]["age"]))

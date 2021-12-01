#!/usr/bin/env python3
"""
Test Tool Name: AccountSenderTool

Test Tool Purpose: This test tool is supposed to mimic the Twitter handle of a new MyTwitter user being sent to the AccountRetriever by the UI Controller.
"""

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT =  12345       # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print ("Connected!")
    username = input("Input Twitter Handle: ")
    s.send(username.encode())

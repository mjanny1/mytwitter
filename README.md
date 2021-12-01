# mytwitter

How to Run Prototype

Clone the repository found at: https://github.com/mjanny1/mytwitter 
Open a new terminal (call this Terminal 1) and navigate to mytwitter/Components/AccountRetriever
Run the python script: AccountRetriever.py
The terminal should print ‘Listening…’
Open a new terminal (call this Terminal 2) and navigate to mytwitter/Components/TestTools
Run the python script: AccountSenderTool.py
The terminal should print ‘Connected!’
The terminal should also provide a prompt to enter a Twitter Handle
Type: ‘VUCoachJWright’
(This is the Twitter Handle of Villanova basketball coach Jay Wright. We used this as an example but really any Twitter handle can be used)
On the other terminal, you should see a list of account IDs printed. These are the user IDs of accounts Jay Wright follows.
In Terminal 2, navigate to mytwitter/Components/UserPreferenceDatabase
View FollowingTable.csv and confirm that it is populated with the accounts Jay Wright follows.
In Terminal 1, navigate to mytwitter/Components/TweetRequestor
Run the python script: TweetRequestor.py
You should see the terminal start to fill with Tweets being requested.
Wait a few seconds for all the tweets to be pulled.
Navigate to mytwitter/Components/TweetDatabase
View the TweetTable.csv
You should see a list of tweets stored in a csv file. These are tweets that can be used to populate Jay Wright’s timeline.


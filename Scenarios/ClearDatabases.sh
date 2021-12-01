# Clearing User Preference Database
head -n 1 ../Components/UserPreferenceDatabase/FollowingTable.csv > ../Components/UserPreferenceDatabase/FollowingTable1.csv
mv ../Components/UserPreferenceDatabase/FollowingTable1.csv ../Components/UserPreferenceDatabase/FollowingTable.csv
# Clearing Tweet Database
head -n 1 ../Components/TweetDatabase/TweetTable.csv > ../Components/TweetDatabase/TweetTable1.csv
mv ../Components/TweetDatabase/TweetTable1.csv ../Components/TweetDatabase/TweetTable.csv

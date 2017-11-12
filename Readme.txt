We are using realtime search API, because free historical API data is only upto the duration of 15 days time, and realtime is unlimited.

When a tweet is made, it is quickly entered into the dictionary. It has no likes and retweets numbers instantly, as it is realtime .

If a tweet is retweeted however, we can go to the original tweet(dictionary) and update the likes and retweets number, because the by the time it is retweeted, it would have had updated feedbacks.


JSON output for a retweeted tweet

Text ="@RT kissore HPV is bad" id = 123120(Retweet link id) Screen name = "@retweeter" 

 Text = "HPV is bad" id = 1231231(Original Tweet link id) Screen name = "Tweeter"


JSON output for a original tweet 

id = 124123(tweet link) id_str = "124123" Text= "KISHORDON" Screen name ="mmakissore"

November 12 revision:

Streamed each tweet, converted into a dictionary and put each tweet_dictionary in a big dictionary with it's tweet link as Key.

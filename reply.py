# -*- coding: utf-8 -*-
#!/usr/bin/python

from twython import Twython

# Load twitter keys
keys_file = 'tw.keys'
with open(keys_file) as f:
    APP_KEY = f.readline().strip("\n")
    APP_SECRET = f.readline().strip("\n")
    OAUTH_TOKEN = f.readline().strip("\n")
    OAUTH_TOKEN_SECRET = f.readline().strip("\n")

# Create twitter instance
tw = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Get and read mentions texts and ids
mentions = tw.get_mentions_timeline()
for tweet in mentions:
	print(tweet['text'], tweet['id'])

# Reply to last mention
last_mention = mentions[0]
tweet_text = 'hey @' + last_mention['user']['screen_name']
print(tweet_text)
print(last_mention['id'])
tw.update_status(status=tweet_text, in_reply_to_status_id=last_mention['id'])

# EXERCISE:
# Retweet the tweet mentioning you tw.retweet(id = "TWEET_ID")

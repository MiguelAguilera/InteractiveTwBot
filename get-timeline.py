# -*- coding: utf-8 -*-
#!/usr/bin/python

from twython import Twython
from twython import TwythonError

# Load twitter keys
keys_file = 'tw.keys'
with open(keys_file) as f:
    APP_KEY = f.readline().strip("\n")
    APP_SECRET = f.readline().strip("\n")
    OAUTH_TOKEN = f.readline().strip("\n")
    OAUTH_TOKEN_SECRET = f.readline().strip("\n")

# Create twitter instance
tw = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
# More info:
# https://twython.readthedocs.io/en/latest/index.html

# Algorithm to get 1000 tweets from the timeline
tweet_texts = []
max_id = 10**18
while len(tweet_texts) < 1000:
	try:
		user_timeline = tw.get_user_timeline(
                    screen_name='realdonaldtrump',
                    include_rts=False,
                    count=200,
                    max_id=max_id)
		# More info:
		# https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline
		print(user_timeline)
	except TwythonError as e:
	   print(e)
	for tweet in user_timeline:
		print(tweet['text'])
		if tweet['id'] < max_id:
			max_id = tweet['id']
			print(max_id)
		tweet_texts += [tweet['text']]

# Write text into text file
with open('timeline.txt', 'w') as outfile:
	for tweet in tweet_texts:
		outfile.write(tweet+'\n')

# EXERCISE:
# Save only tweets with >= 15000 retweets
# Hint: check API documentation

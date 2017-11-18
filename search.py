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
# More info:
# https://twython.readthedocs.io/en/latest/index.html

# Define search query we want to look for in twitter
searchquery = '"ni machismo ni feminismo, igualdad" exclude:retweets'

# Get and read mentions texts and ids
search = tw.search(q=searchquery, count=20, result_type='recent')
for result in search["statuses"]:
	print(result['text'], result['id'])


# EXERCISE:
# Configure "sniper" bot, finding a specific sentence and sending a sad koala in response
# Hint: reuse code from post.py and reply.py scripts

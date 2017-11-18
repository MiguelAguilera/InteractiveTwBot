# -*- coding: utf-8 -*-
#!/usr/bin/python

from twython import Twython
import random

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

# Load random image and uplaod it to twitter
num = random.randint(0, 20 - 1)
imagefile = 'sad-cat/' + str(num) + '.jpg'
photo = open(imagefile, 'rb')
image_ids = tw.upload_media(media=photo)

# Write tweet text
tweet_text = 'Testing Etopia Bot' + str(num)

# Update status to twitter
# More info
# https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update
tw.update_status(status=tweet_text, media_ids=image_ids['media_id'])

# EXERCISE:
# Modify update text to mention another user

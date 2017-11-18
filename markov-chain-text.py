# -*- coding: utf-8 -*-
#!/usr/bin/python

import markovify

# Get raw text as string.
with open("last-question.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text, state_size=2)
# state_size determines lenght of markov chains

# Print three randomly-generated sentences of no more than 140 characters
for i in range(4):
    print('->', text_model.make_short_sentence(140))

# EXERCISE:
# Write random tweets form a model generated from a user's timeline
# Hint: reuse code from get-timeline.py and post.py

#!/usr/bin/env python
# -*- coding: latin-1 -*-
import oauth2

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key="Jw80fAXKjE652Xj81nWtc9WOv", secret="3Hrg6bGHsRpNQdXoSTADdFzSgo5aKSqEm86q29h7I0kWgEbp64")
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content

home_timeline = oauth_req( 'https://api.twitter.com/1.1/statuses/home_timeline.json', '1945205930-pkajbNI9qyPI9k0kyx0LepXon08PZf0MztCiSs0', '7HRseyzR2n9lf3BwgfqkLxWm3W9LCenxBYgZaozbyA1o9' )

f = open("twittertimeline.txt","w")
f.write(home_timeline)
f.close()

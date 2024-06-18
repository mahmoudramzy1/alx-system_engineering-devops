#!/usr/bin/python3
"""return number of subscribers of reddit"""

import requests

def number_of_subscribers(subreddit):
    """ function to get subscriber count"""
    subscribers = 0
    base_url = "https://www.reddit.com/r/"
    url = "{}{}/about.json".format(base_url, subreddit)
    res = requests.get(url, 
              headers = {"User-Agent": "My-User-Agent"},
              allow_redirects=False
              )
    if res.status_code == 200:
        data = res.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
    return subscribers

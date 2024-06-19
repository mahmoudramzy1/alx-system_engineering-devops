#!/usr/bin/python3
"""return titles of top ten posts"""

import requests


def top_ten(subreddit):
    """return titles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    params = {"limit": 10}
    res = requests.get(url, params=params, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        posts = data.get(data, {}).get(children, {})
        for post in posts:
                print(post.get('data').get('title'))
        else:
            print(None)


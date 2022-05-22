#!/usr/bin/python3
"""This script show the top 10"""

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/host.json?limit=10".format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    rq = requests.get(url, headers=headers)
    if (rq.status_code == 404):
        print("None")
    elif 'data' not in rq.json():
        print("None")
    else:
        rq = rq.json()
        for i in rq['data']['children']:
            print(post['data']['title'])

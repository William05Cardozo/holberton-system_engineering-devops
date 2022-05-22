#!/usr/bin/python3
"""This script queries the Reddit API and return of info"""

import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    rq = requests.get(url, headers=headers)
    if (rq.status_code == 302 or rq.status_code == 404):
        return 0
    rq = rq.json()
    if ('error' in rq):
        return 0
    elif ('subscribers' in rq['data']):
        return rq['data']['subscribers']
    else:
        return 0

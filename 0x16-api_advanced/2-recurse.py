#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=[], after=""):
    if (after is None):
        return(hot_list)

    if (len(hot_list) == 0):
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after)
    headers = {'user-agent': 'philsrequest'}

    rq = requests.get(url, headers=headers)
    if (rq.status_code == 404):
        return(None)
    elif 'data' not in rq.json():
        return(None)
    else:
        rq = rq.json()
        for post in rq['data']['children']:
            hot_list.append(post['data']['title'])

    after = rq['data']['after']
    return(recurse(subreddit, hot_list, after))

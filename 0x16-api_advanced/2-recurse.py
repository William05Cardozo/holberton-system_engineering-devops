#!/usr/bin/python3
"""
This script return a list containing the titles
Using a RecursiveFunction
"""

import requests


def recurse(subreddit, hot_list=[],):

    global after
    headers = {'User-Agent': 'my-app/0.0.1'}
    try:
        url = "https://www.reddit.com/r/{}.json".format(sudreddit)
        if after:
            url = "https://www.reddit.com/r/{}.json?after={}".format(after)
        gett = get(url, headers=headers, allow_redirects=False).json()
        for children in gett['data']['children']:
            hot_list.append(children.get('data').get('title'))
        after = get(url, headers=headers,
                    allow_redirects=False).json().get('data').get('after')
        if ater:
            return(recurse(sudreddit, hot_list))
        return(hot_list)
    except Exception:
        return(None)

#!/usr/bin/python3
"""
Function queries Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """ Queries Reddit API, returns number of subscribers """
    try:

        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        headers = {'User-Agent': 'MyApp/1.0'}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            subscriber_count = data["data"]["subscribers"]
            return (subscriber_count)
        else:
            return (0)
    except:
        return (0)

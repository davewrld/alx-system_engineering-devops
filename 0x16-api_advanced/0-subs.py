#!/usr/bin/python3
"""
Function queries Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """ Queries Reddit API, returns number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyApp/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscriber_count = data["data"]["subscribers"]
        return subscriber_count

    else:
        return 0

#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed Reddit API"""
import requests


def top_ten(subreddit):
    """Function queries API"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "0x16-api_advanced/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            titles = (post["data"]["title"])
            print (titles[:10])
    else:
        print(None)

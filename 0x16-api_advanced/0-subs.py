#!/usr/bin/python3
"""This Function is to query subscribers on a given Reddit subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    # Reddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    subscribers_count = response.json().get("data", {}).get("subscribers", 0)

    return subscribers_count

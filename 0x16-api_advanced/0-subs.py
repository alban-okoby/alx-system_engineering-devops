#!/usr/bin/python3
"""
Module: reddit_api.py
Description: A script to query the Reddit API and retrieve the number of
subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit

    Args:
        subreddit (str): The name of the subreddit

    Returns:
        int: The number of subscribers if the subreddit is valid, else 0
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyRedditScraper/1.0'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            subreddit_info = response.json()['data']
            return subreddit_info['subscribers']
        else:
            # print(f"Error: Status Code: {response.status_code}")
            return 0

    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0

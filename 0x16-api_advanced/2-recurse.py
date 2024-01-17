#!/usr/bin/python3
"""
Module: reddit_api.py
Description: A script to define a recsive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively retrieve the titles of all hot articles for a given subreddit

    Args:
        subreddit (str): The name of the subreddit
        hot_list (list): A list to store the titles of hot articles
        (default is None)
        after (str): The Reddit API parameter for pagination (default is None)

    Returns:
        list: A list containing the titles of hot articles
    """
    if hot_list is None:
        hot_list = []

    url = f'https://www.reddit.com/r/{sr}/hot.json?limit=100&after={after}'
    headers = {'User-Agent': 'MyRedditScraper/1.0'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            posts_data = response.json().get('data', {}).get('children', [])
            hot_list.extend([post['data']['title'] for post in posts_data])
            after = response.json().get('data', {}).get('after')

            if after:
                recurse(sr, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

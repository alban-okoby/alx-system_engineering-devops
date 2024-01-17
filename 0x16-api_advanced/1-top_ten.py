#!/usr/bin/python3
"""
Module: reddit_api.py
Description: A script to query the Reddit API and print the titles of
the first 10 hot posts for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit

    Args:
        subreddit (str): The name of the subreddit

    Returns:
        None
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    headers = {'User-Agent': 'MyRedditScraper/1.0'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            posts_data = response.json().get('data', {}).get('children', [])

            for index, post in enumerate(posts_data[:10], 1):
                title = post['data']['title']
                print(f"{index}. {title}")
        else:
            print(f"Error: Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {e}")

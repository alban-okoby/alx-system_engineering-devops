#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit"""
import requests


def count_words(subreddit, word_list, instances=None, after=None, count=0):
    """Prints counts of given words found in hot posts of a given subreddit

    Args:
        subreddit (str): The subreddit to search
        word_list (list): The list of words to search for in post titles
        instances (dict): Dictionary of words and their counts
        after (str): The parameter for the next page of the API results
        count (int): The parameter of results matched thus far
    """
    if instances is None:
        instances = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )

    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")

    for post in results.get("children"):
        title = post.get("data").get("title").lower().split()
        for word in word_list:
            instances[word] = (
                    instances.get(word, 0) + title.count(word.lower())
                    )

    if after is None:
        if not instances:
            print("")
            return

        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        for k, v in instances:
            print(f"{k}: {v}")
    else:
        count_words(subreddit, word_list, instances, after, count)

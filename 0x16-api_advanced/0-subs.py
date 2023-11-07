#!/usr/bin/python3
"""Module to get the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Gets number of subscribers by querying an API

    Args:
        subreddit: subredit to be searched

    Returns:
        Number of subscribers
    """
    user_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': user_agent
    }
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    dic = response.json()
    if 'data' not in dic:
        return 0
    if 'subscribers' not in dic.get('data'):
        return 0
    return dic['data']['subscribers']

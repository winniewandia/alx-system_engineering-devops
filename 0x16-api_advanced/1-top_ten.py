#!/usr/bin/python3
"""module to list the top ten hotposts for a given subreddit
"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddi

    Args:
        subreddit
    """
    user_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': user_agent
    }
    url = 'https://www.reddit.com/r/{}/hot.json?limit=9'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print('None')
        return
    dic = response.json()
    hot_posts = dic['data']['children']
    if len(hot_posts) == 0:
        print('None')
    else:
        for post in hot_posts:
            print(post['data']['title'])

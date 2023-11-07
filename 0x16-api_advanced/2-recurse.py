#!/usr/bin/python3
"""contains a recursive function that queries a reddit API

Returns:
    number of titles of all hot articles for a given subreddit
"""
import requests


# def recurse(subreddit, hot_list=None, after=None):
#     """recursive function that queries the Reddit API and returns a list
#     containing the titles of all hot articles for a given subreddit

#     Args:
#         subreddit
#         hot_list: Defaults to None.
#         after: Defaults to None.

#     Returns:
#        number of titles of all hot articles for a given subreddit
#     """
#     if hot_list is None:
#         hot_list = []

#     url = f"https://www.reddit.com/r/{subreddit}/hot.json"
#     params = {"after": after} if after else {}

#     response = requests.get(
#         url, headers={"User-Agent": "Mozilla/5.0"}, params=params)

#     if response.status_code == 200:
#         data = response.json()
#         posts = data.get("data", {}).get("children", [])

#         if posts:
#             for post in posts:
#                 hot_list.append(post["data"]["title"])

#             after = data["data"]["after"]
#             if after:
#                 hot_list = recurse(subreddit, hot_list=hot_list, after=after)

#         return hot_list
#     else:
#         return None

def add_title(hot_list, hot_posts):
    """ Adds item into a list """
    if len(hot_posts) == 0:
        return
    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_title(hot_list, hot_posts)


def recurse(subreddit, hot_list=[], after=None):
    """ Queries to Reddit API """
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(hot_list, hot_posts)
    after = dic['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)

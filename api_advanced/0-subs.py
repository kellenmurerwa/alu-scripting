#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and
returns the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditApp/0.0.1'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return 0
    
    try:
        data = response.json()
        return data['data']['subscribers']
    except (KeyError, ValueError):
        return 0

if __name__ == "__main__":
    print(number_of_subscribers('python')) 


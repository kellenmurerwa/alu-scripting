#!/usr/bin/python3
"""Return number of subscriber for a given subreddit. """

import requests


def number_of_subscribers(subreddit):
    """ Retrieves the number of subscribers for a given subreddit"""
   headers = { "User-Agent": "ALU-scripting API 0.1"}
    url = f"https://reddit.com/r/{subreddit}.json" 

    try:
        response = requests.get(url, headers=headers, timeout=30, allow_redirects=False)

    except requests.exceptions.Timeout:
        return "The request timed out"

    if response.status_code == 200:
        try:
            json_data = response.json()
            subscriber_number = json_data.get("data").get("children")[0].get("data").get("subreddit_subscribers")
            return subscriber_number
        except (AttributeError, KeyError):  
            return 0

    elif response.status_code == 404:
        return 0

    else:
        return 0  

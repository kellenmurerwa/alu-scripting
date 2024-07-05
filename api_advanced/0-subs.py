#!/usr/bin/python3
"""
This script retrieves the number of subscribers for a given subreddit using the Reddit API.

It makes a GET request to the subreddit's JSON endpoint and parses the response to extract the subscriber count. 
- A custom User-Agent header is set to identify the script.
- Timeouts and redirects are handled to prevent unexpected behavior.
- The function returns the number of subscribers, a timeout message, or 0 for other errors or invalid subreddits.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.

    Args:
        subreddit: The name of the subreddit to query.

    Returns:
        The number of subscribers (int) on success, "The request timed out" on timeout, or 0 for other errors or invalid subreddits.
    """

    headers = {"User-Agent": "ALU-scripting API 0.1"}
    url = f"https://www.reddit.com/r/{subreddit}.json"  # f-string for cleaner URL formatting

    try:
        response = requests.get(url, headers=headers, timeout=30, allow_redirects=False)

    except requests.exceptions.Timeout:
        return "The request timed out"

    if response.status_code == 200:
        try:
            json_data = response.json()
            subscriber_number = json_data.get("data").get("children")[0].get("data").get("subreddit_subscribers")
            return subscriber_number
        except (AttributeError, KeyError):  # Handle cases where data structure might be different
            return 0

    elif response.status_code == 404:
        return 0

    else:
        return 0  # Handle unexpected status codes


#!/usr/bin/python3
"""
1-top_ten module: prints the titles of the first 10 hot posts
for a given subreddit.
"""
import urllib.request
import urllib.error
import json


class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Prevents urllib from automatically following redirects."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit. Prints None if the
    subreddit is invalid.

    Args:
        subreddit (str): name of the subreddit to query.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "linux:alu.api.advanced:v1.0 (by /u/alu_student)"
    }
    request = urllib.request.Request(url, headers=headers)
    opener = urllib.request.build_opener(NoRedirectHandler)

    try:
        response = opener.open(request)
    except (urllib.error.HTTPError, urllib.error.URLError):
        print(None)
        return

    if response.status != 200:
        print(None)
        return

    try:
        data = json.loads(response.read().decode("utf-8"))
        posts = data["data"]["children"]
    except (KeyError, TypeError, ValueError):
        print(None)
        return

    if not posts:
        print(None)
        return

    for post in posts:
        print(post["data"]["title"])

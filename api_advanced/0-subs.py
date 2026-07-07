#!/usr/bin/python3
"""
0-subs module: queries the Reddit API for a subreddit's subscriber count.
"""
import urllib.request
import urllib.error
import json


class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Prevents urllib from automatically following redirects.

    Reddit sends invalid subreddits to a search-results page via a
    redirect, so we need to detect that redirect rather than follow it.
    """

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): name of the subreddit to query.

    Returns:
        int: number of subscribers, or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu.api.advanced:v1.0 (by /u/alu_student)"
    }
    request = urllib.request.Request(url, headers=headers)
    opener = urllib.request.build_opener(NoRedirectHandler)

    try:
        response = opener.open(request)
    except (urllib.error.HTTPError, urllib.error.URLError):
        return 0

    if response.status != 200:
        return 0

    try:
        data = json.loads(response.read().decode("utf-8"))
        return data["data"]["subscribers"]
    except (KeyError, TypeError, ValueError):
        return 0

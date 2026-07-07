
"""
3-count module: recursively counts keyword occurrences across the
titles of all hot posts in a subreddit, and prints a sorted count.
"""
import urllib.request
import urllib.error
import json


class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Prevents urllib from automatically following redirects."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def print_counts(counts):
    """
    Prints word counts sorted by count (descending), then
    alphabetically for ties. Words with a count of 0 are skipped.

    Args:
        counts (dict): mapping of lowercase word -> occurrence count.
    """
    items = [(word, count) for word, count in counts.items() if count > 0]
    items.sort(key=lambda pair: (-pair[1], pair[0]))
    for word, count in items:
        print("{}: {}".format(word, count))


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot
    articles for a subreddit, and prints a sorted count of the given
    keywords. Prints nothing if the subreddit is invalid or no
    keyword matches are found.

    Args:
        subreddit (str): name of the subreddit to query.
        word_list (list): keywords to search for (case-insensitive).
        after (str): pagination token, used internally by recursion.
        counts (dict): accumulator for word counts, used internally
            by the recursion.
    """
    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)

    headers = {
        "User-Agent": "linux:alu.api.advanced:v1.0 (by /u/alu_student)"
    }
    request = urllib.request.Request(url, headers=headers)
    opener = urllib.request.build_opener(NoRedirectHandler)

    try:
        response = opener.open(request)
    except (urllib.error.HTTPError, urllib.error.URLError):
        return print_counts(counts)

    if response.status != 200:
        return print_counts(counts)

    try:
        data = json.loads(response.read().decode("utf-8"))
        children = data["data"]["children"]
    except (KeyError, TypeError, ValueError):
        return print_counts(counts)

    multiplier = {}
    for word in word_list:
        key = word.lower()
        multiplier[key] = multiplier.get(key, 0) + 1

    for post in children:
        title = post["data"]["title"]
        for token in title.split():
            clean = token.lower()
            if clean in multiplier:
                counts[clean] = counts.get(clean, 0) + multiplier[clean]

    next_after = data["data"].get("after")
    if next_after:
        return count_words(subreddit, word_list, next_after, counts)

    return print_counts(counts)

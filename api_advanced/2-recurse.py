#!/usr/bin/python3
"""
2-recurse module: recursively collects all hot post titles for a
given subreddit, following Reddit's pagination.
"""
import urllib.request
import urllib.error
import json


class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Prevents urllib from automatically following redirects."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of the
    titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): name of the subreddit to query.
        hot_list (list): accumulator for post titles (do not pass
            manually; used internally by the recursion).
        after (str): pagination token used internally by the
            recursion.

    Returns:
        list: titles of every hot post in


cat > 2-recurse.py << 'EOF'
#!/usr/bin/python3
"""
2-recurse module: recursively collects all hot post titles for a
given subreddit, following Reddit's pagination.
"""
import urllib.request
import urllib.error
import json


class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Prevents urllib from automatically following redirects."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of the
    titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): name of the subreddit to query.
        hot_list (list): accumulator for post titles (do not pass
            manually; used internally by the recursion).
        after (str): pagination token used internally by the
            recursion.

    Returns:
        list: titles of every hot post in




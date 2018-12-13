"""
Embedded tweet plugin for Pelican
=================================

This plugin allows you to embed Twitter tweets into your articles.
And also provides a link for Twitter username.

    i.e.

        @username

        will be replaced by a link to Twitter username page.

        @username/status/tweetid

        will be replaced by a `Embedded-tweet`_ API.

.. _Embedded-tweet: https://developer.twitter.com/en/docs/twitter-for-websites/embedded-tweets/overview.html

"""

from pelican import signals
import re


def embed_tweet(instance):
    if not instance._content:
        return

    instance._content = re.sub(
        r'(^|[^@\w])@(\w{1,15})(\b[^/])',
        '\\1<a href="https://twitter.com/\\2">@\\2</a>\\3',
        re.sub(
            r'(^|[^@\w])@(\w{1,15})/status/(\d+)\b',
            '\\1<blockquote class="twitter-tweet" align="center"><a href="https://twitter.com/\\2/status/\\3">Tweet of \\2/\\3</a></blockquote>',
            instance._content
        )
    ) + '<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>'


def register():
    signals.content_object_init.connect(embed_tweet)

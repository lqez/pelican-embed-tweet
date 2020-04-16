pelican-embed-tweet
===================

Embedding tweets into your Pelican blog posts.


How to use this?
----------------

 1. Download `embed_tweet.py`
 1. Copy it wherever or just into `pelican/plugins/`
 1. Push back `embed_tweet` into plugin list of settings.
    - `PLUGINS = ['pelican.plugins.embed_tweet']`

 1. That's all!


Conversion
----------

 1. `t@username` will be replaced by `https://twitter.com/username`
 1. `t@username/status/tweetid` will be replaced by `Embedded-tweet`
    - See: <https://dev.twitter.com/docs/embedded-tweets>
    - Example: <http://lqez.github.io/blog/gittipcom-and-forkorea.html>


License
-------

Distributed under MIT license.


AUTHOR
------
Park Hyunwoo / [@lqez](https://twitter.com/lqez)

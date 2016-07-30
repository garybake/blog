#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gary Bake'
SITENAME = u'This and That'
SITEURL = '' 
# SITEURL = 'http://garybake.com'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Home', '/'),)  # TODO Opens in a new window???

DEFAULT_PAGINATION = 10

STATIC_PATHS = ["images"]

STATIC_PATHS = [
    'images', 
    'extra/robots.txt', 
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

THEME = '/home/gary/Devel/blog/themes/Flex'

GITHUB_URL = 'https://github.com/garybake'
TWITTER_USERNAME = 'MrGaryBake'

SOCIAL = (('twitter', 'http://twitter.com/MrGaryBake'),
          ('facebook', 'https://www.facebook.com/garybake'),
          ('stack-overflow', 'http://stackoverflow.com/users/1205730/garybake'),
          ('linkedin', 'https://www.linkedin.com/in/garybakeuk'),
          ('github', 'http://github.com/garybake'),
          )

SITELOGO = '/images/face.jpg'

GOOGLE_ANALYTICS = "UA-15291213-1"

DISQUS_SITENAME = "garybake"

PYGMENTS_STYLE = "monokai"
AUTHOR = 'Gary Bake'
SITENAME = 'This and That'
SITEURL = '' 
SITEDESCRIPTION = 'Programming, Machine learning and Electronics chit chat'

PATH = 'content'

TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Home', '/'),)  # TODO Opens in a new window???

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

THEME = 'Flex'

GITHUB_URL = 'https://github.com/garybake'
TWITTER_USERNAME = 'MrGaryBake'

SOCIAL = (('twitter', 'http://twitter.com/MrGaryBake'),
          ('facebook', 'https://www.facebook.com/garybake'),
          ('stack-overflow', 'http://stackoverflow.com/users/1205730/garybake'),
          ('linkedin', 'https://www.linkedin.com/in/garybakeuk'),
          ('github', 'http://github.com/garybake'),
          )

SITELOGO = '/images/face.jpg'
SITETITLE = 'My face'

PYGMENTS_STYLE = "monokai"

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "monthly",
        "pages": "monthly"
    }
}
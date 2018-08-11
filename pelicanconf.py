''' Main settings python file'''
# !/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hussain AlSalem'
SITENAME = 'geoHussain'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs', 'extra']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
HIDE_SIDEBAR = False
SOCIAL = (('github', 'http://github.com/geohussain'),
          ('bitbucket', 'https://bitbucket.org/geohussain/'),
          )
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
RECENT_POST_COUNT = 4
DISPLAY_TAGS_ON_SIDEBAR = True
TAGS_URL = 'tags.html'
TAG_CLOUD_MAX_ITEMS = 0


DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
THEME = 'themes/pelican-themes/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['plugins/pelican-plugins']
PLUGINS = ['i18n_subsites', 'subcategory', 'tag_cloud', 'pelican-bibtex',
           'pelican-ipynb.markup']
IGNORE_FILES = ['.ipynb_checkpoints']
MARKUP = ('md', 'ipynb')
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.tables': {},
    }
}
I18N_TEMPLATES_LANG = 'en'
BOOTSTRAP_THEME = 'cosmo'
TYPOGRIFY = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
# SHOW_ARTICLE_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
IPYNB_IGNORE_CSS = False

MENUITEMS = (
    ('Blog', '/category/Blog.html'),
    ('Python Notebooks', '/pages/python-notebooks.html'),
    ('Publications', '/publications.html'),
    ('CV', '/pages/cv.html'),
)
PYGMENTS_STYLE = 'monokai'

ABOUT_ME = 'I\'m a geophysicist and programmer with love to high ' + \
    'performance computing (HPC).'
AVATAR = 'images/profile.jpg'

PUBLICATIONS_SRC = 'content/example.bib'
CUSTOM_CSS = 'static/css/custom.css'
DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives',
                    'publications', 'tags']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
}
PADDED_SINGLE_COLUMN_STYLE = False

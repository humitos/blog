# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
import os

##############################################
# Configuration
##############################################


# Data about this site
BLOG_AUTHOR = "Manuel Kaufmann"
BLOG_TITLE = "Humitos"
# This is the main URL for your site. It will be used
# in a prominent link
SITE_URL = "http://elblogdehumitos.com.ar/"
# This is the URL where nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = "http://nikola.ralsina.com.ar"
BLOG_EMAIL = "humitos@gmail.com"
BLOG_DESCRIPTION = "el blog de Manuel Kaufmann -- " \
                   "comunicando mi vida a la sociedad"

# Nikola is multilingual!
#
# Currently supported languages are:
#   English -> en
#   Greek -> gr
#   German -> de
#   French -> fr
#   Polish -> pl
#   Russian -> ru
#   Spanish -> es
#   Italian -> it
#   Simplified Chinese -> zh-cn
#
# If you want to use Nikola with a non-supported language you have to provide
# a module containing the necessary translations
# (p.e. look at the modules at: ./nikola/data/themes/default/messages/fr.py).
# If a specific post is not translated to a language, then the version
# in the default language will be shown instead.

# What is the default language?
DEFAULT_LANG = "es"

# What other languages do you have?
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "es": "./es",
    # 'en': './en',
}

TRANSLATIONS_PATTERN = '{path}.{lang}.{ext}'

# Links for the sidebar / navigation bar.
# You should provide a key-value pair for each used language.
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ('http://argentinaenpython.com.ar/', 'Argentina en Python'),
        ('/pages/quien-escribe/', '¿Quién escribe?'),
        # ('/pages/modulos-python/', 'Módulos Python'),
        ('/random/', 'Random'),
        (
            (
                ('http://pois.elblogdehumitos.com.ar/', 'Puntos de Interés'),
                ('http://elblogdehumitos.com.ar/osm/', 'Tu negocio en OSM'),
            ),
            'OpenStreetMap',
        ),
        (
            (
                ('http://tutorial.python.org.ar/', 'El Tutorial de Python'),
                ('/pages/traducciones/', 'Traducciones'),
                ('/pages/apoyo/', 'Apoyo'),
                ('/pages/repositorio/', 'Repositorio'),
                ('/pages/frases/', 'Frases'),
                # ('/pages/expresiones-regionales/', 'Expresiones Regionales'),
            ),
            'Extras',
        ),
        (
            (
                ('/categories/index.html', 'Etiquetas'),
                ('/archive.html', 'Archivo Anual'),
                ('http://humitos.wordpress.com', 'Viejo Blog en Wordpress'),
                ('http://feeds.feedburner.com/humitos', 'RSS'),
            ),
            'Historial',
        ),
        # ('/rss.xml', 'RSS'),
    ),
}


##############################################
# Below this point, everything is optional
##############################################


# POSTS and PAGES contains (wildcard, destination, template) tuples.
#
# The wildcard is used to generate a list of reSt source files
# (whatever/thing.txt).
#
# That fragment must have an associated metadata file (whatever/thing.meta),
# and opcionally translated files (example for spanish, with code "es"):
#     whatever/thing.txt.es and whatever/thing.meta.es
#
# From those files, a set of HTML fragment files will be generated:
# cache/whatever/thing.html (and maybe cache/whatever/thing.html.es)
#
# These files are combinated with the template to produce rendered
# pages, which will be placed at
# output / TRANSLATIONS[lang] / destination / pagename.html
#
# where "pagename" is specified in the metadata file.
#
# The difference between POSTS and PAGES is that POSTS are added
# to feeds and are considered part of a blog, while PAGES are
# just independent HTML pages.

POSTS = (
    ("posts/nikola/*.rst", "posts", "post.tmpl"),
    # ("posts/wordpress/*.wp", "posts/wordpress", "post.tmpl"),
    ("posts/wordpress/migrated/*.rst", "posts/wordpress", "post.tmpl"),
)

PAGES = (
    ("pages/*.rst", "pages", "story.tmpl"),
)

# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of "source" "relative destination".
# Default is:
# FILES_FOLDERS = {'files': '' }
# Which means copy 'files' into 'output'

# A mapping of languages to file-extensions that represent that language.
# Feel free to add or delete extensions to any list, but don't add any new
# compilers unless you write the interface for it yourself.
#
# 'rest' is reStructuredText
# 'markdown' is MarkDown
# 'html' assumes the file is html and just copies it
COMPILERS = {
    "rest": ('.txt', '.rst'),
    "markdown": ('.md', '.mdown', '.markdown'),
    "textile": ('.textile',),
    "txt2tags": ('.t2t',),
    "bbcode": ('.bb',),
    "wiki": ('.wiki',),
    "ipynb": ('.ipynb',),
    "html": ('.html', '.htm')
}

# Create by default posts in one file format?
# Set to False for two-file posts, with separate metadata.
# ONE_FILE_POSTS = True

# If this is set to True, then posts that are not translated to a language
# LANG will not be visible at all in the pages in that language.
# If set to False, the DEFAULT_LANG version will be displayed for
# untranslated posts.
SHOW_UNTRANSLATED_POSTS = False

# Nikola supports logo display.  If you have one, you can put the URL here.
# Final output is <img src="LOGO_URL" id="logo" alt="BLOG_TITLE">.
# The URL may be relative to the site root.
LOGO_URL = '/logo.png'

# Paths for different autogenerated bits. These are combined with the
# translation paths.

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag.xml (RSS feed for a tag)
# TAG_PATH = "categories"

# If TAG_PAGES_ARE_INDEXES is set to True, each tag's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# TAG_PAGES_ARE_INDEXES = True

# Only include tags on the tag list/overview page if there are at least
# TAGLIST_MINIMUM_POSTS number of posts or more with every tag. Every tag
# page is still generated, linked from posts, and included in the sitemap.
# However, more obscure tags can be hidden from the tag index page.
# TAGLIST_MINIMUM_POSTS = 1

# Final location is output / TRANSLATION[lang] / INDEX_PATH / index-*.html
# INDEX_PATH = ""

# Create per-month archives instead of per-year
# CREATE_MONTHLY_ARCHIVE = False
# Create one large archive instead of per-year
# CREATE_SINGLE_ARCHIVE = False
# Create year, month, and day archives each with a (long) list of posts
# (overrides both CREATE_MONTHLY_ARCHIVE and CREATE_SINGLE_ARCHIVE)
# CREATE_FULL_ARCHIVES = False
# If monthly archives or full archives are created, adds also one archive per day
# CREATE_DAILY_ARCHIVE = False

# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / ARCHIVE_FILENAME
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / DAY / index.html
# ARCHIVE_PATH = ""
# ARCHIVE_FILENAME = "archive.html"

# If ARCHIVES_ARE_INDEXES is set to True, each archive page which contains a list
# of posts will contain the posts themselves. If set to False, it will be just a
# list of links.
# ARCHIVES_ARE_INDEXES = False

# URLs to other posts/pages can take 3 forms:
# rel_path: a relative URL to the current page/post (default)
# full_path: a URL with the full path from the root
# absolute: a complete URL (that includes the SITE_URL)
# URL_TYPE = 'rel_path'

# Final location for the blog main RSS feed is:
# output / TRANSLATION[lang] / RSS_PATH / rss.xml
# RSS_PATH = ""

# Number of posts in RSS feeds
# FEED_LENGTH = 10

# Slug the Tag URL easier for users to type, special characters are
# often removed or replaced as well.
SLUG_TAG_PATH = True

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []
REDIRECTIONS = [
    ('pages/donaciones/index.html', '/pages/argentina-en-python/donaciones/'),
    ('pages/donde-esta-humitos/index.html', '/pages/argentina-en-python/donde-esta-humitos/'),
    ('pages/argentina-en-python/index.html', 'http://argentinaenpython.com.ar/'),
    ('pages/argentina-en-python-en/index.html', 'http://argentinaenpython.com.ar/en/'),
    ('pages/argentina-en-python/donde-esta-humitos/index.html', 'http://argentinaenpython.com.ar/donde-esta-humitos/'),
    ('pages/argentina-en-python/track-teen-scipy-la-2015/index.html', 'http://argentinaenpython.com.ar/track-teen-scipy-la-2015/'),
    ('pages/argentina-en-python/python-for-ladies/index.html', 'http://argentinaenpython.com.ar/python-for-ladies/'),
    ('pages/argentina-en-python/eventos/index.html', 'http://argentinaenpython.com.ar/eventos/'),
    ('pages/argentina-en-python/remeras/index.html', 'http://argentinaenpython.com.ar/remeras/'),
    ('pages/argentina-en-python/donaciones/index.html', 'http://argentinaenpython.com.ar/donaciones/'),
    ('pages/argentina-en-python/donaciones/medios/index.html', 'http://argentinaenpython.com.ar/donaciones/medios/'),
    ('pages/argentina-en-python/donaciones/misiones/index.html', 'http://argentinaenpython.com.ar/donaciones/misiones/'),
    ('pages/argentina-en-python/donaciones/colaboradores/index.html', 'http://argentinaenpython.com.ar/donaciones/colaboradores/'),
    ('pages/argentina-en-python/donaciones/gracias/index.html', 'http://argentinaenpython.com.ar/donaciones/gracias/'),
]

# Commands to execute to deploy. Can be anything, for example,
# you may use rsync:
# "rsync -rav output/* joe@my.site:/srv/www/site"
# And then do a backup, or ping pingomatic.
# To do manual deployment, set it to []
# DEPLOY_COMMANDS = []
from local_conf import DEPLOY_COMMANDS

# For user.github.io OR organization.github.io pages, the DEPLOY branch
# MUST be 'master', and 'gh-pages' for other repositories.
# GITHUB_SOURCE_BRANCH = 'master'
# GITHUB_DEPLOY_BRANCH = 'gh-pages'

# The name of the remote where you wish to push to, using github_deploy.
# GITHUB_REMOTE_NAME = 'origin'


# Where the output site should be located
# If you don't use an absolute path, it will be considered as relative
# to the location of conf.py
# OUTPUT_FOLDER = 'output'

# where the "cache" of partial generated content should be located
# default: 'cache'
# CACHE_FOLDER = 'cache'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, there are no filters.

def convert_images(filename):
    EXCLUDE_IMAGES = (
        'assets',
    )
    for exclude in EXCLUDE_IMAGES:
        if exclude in filename:
            continue

    name, ext = os.path.splitext(filename)
    to_filename = name + '.thumbnail' + ext
    command = 'convert {from_filename} -thumbnail 580 {to_filename}'\
            .format(from_filename=filename,
                    to_filename=to_filename)
    os.system(command)

FILTERS = {
    # ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
    ".jpg": [convert_images],
    ".jpeg": [convert_images],
    ".png": [convert_images],
}


# Expert setting! Create a gzipped copy of each generated file. Cheap server-
# side optimization for very high traffic sites or low memory servers.
# GZIP_FILES = False
# File extensions that will be compressed
# GZIP_EXTENSIONS = ('.txt', '.htm', '.html', '.css', '.js', '.json', '.xml')
# Use an external gzip command? None means no.
# Example: GZIP_COMMAND = "pigz -k {filename}"
# GZIP_COMMAND = None
# Make sure the server does not return a "Accept-Ranges: bytes" header for
# files compressed by this option! OR make sure that a ranged request does not
# return partial content of another representation for these resources. Do not
# use this feature if you do not understand what this means.

# Compiler to process LESS files.
# LESS_COMPILER = 'lessc'

# A list of options to pass to the LESS compiler.
# Final command is: LESS_COMPILER LESS_OPTIONS file.less
# LESS_OPTIONS = []

# Compiler to process Sass files.
# SASS_COMPILER = 'sass'

# A list of options to pass to the Sass compiler.
# Final command is: SASS_COMPILER SASS_OPTIONS file.s(a|c)ss
# SASS_OPTIONS = []

# #############################################################################
# Image Gallery Options
# #############################################################################

# Galleries are folders in galleries/
# Final location of galleries will be output / GALLERY_PATH / gallery_name
GALLERY_FOLDERS = {u'galleries': u'galleries'}
THUMBNAIL_SIZE = 180
MAX_IMAGE_SIZE = 1280
USE_FILENAME_AS_TITLE = False
GALLERY_SORT_BY_DATE = True
EXTRA_IMAGE_EXTENSIONS = []

# If set to False, it will sort by filename instead. Defaults to True
# GALLERY_SORT_BY_DATE = True
#
# Folders containing images to be used in normal posts or
# pages. Images will be scaled down according to THUMBNAIL_SIZE and
# MAX_IMAGE_SIZE options, but will have to be referenced manually to
# be visible on the site. The format is a dictionary of {source:
# relative destination}.
#
IMAGE_FOLDERS = {'images': ''}

# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################

# Data about post-per-page indexes
# INDEXES_TITLE = ""  # If this is empty, the default is BLOG_TITLE
# INDEXES_PAGES = ""  # If this is empty, the default is 'old posts page %d'
# translated

# Name of the theme to use.
# THEME = 'site'
THEME = 'elblogdehumitos'

# Data about post-per-page indexes.
# INDEXES_PAGES defaults to 'old posts, page %d' or 'page %d' (translated),
# depending on the value of INDEXES_PAGES_MAIN.
# INDEXES_TITLE = ""         # If this is empty, defaults to BLOG_TITLE
# INDEXES_PAGES = ""         # If this is empty, defaults to '[old posts,] page %d' (see above)
# INDEXES_PAGES_MAIN = False # If True, INDEXES_PAGES is also displayed on
#                            # the main (the newest) index page (index.html)

# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored.
# Can be any of autumn borland bw colorful default emacs friendly fruity manni
# monokai murphy native pastie perldoc rrt tango trac vim vs
# CODE_COLOR_SCHEME = default

# If you use 'site-reveal' theme you can select several subthemes
# THEME_REVEAL_CONFIG_SUBTHEME = 'sky'
# You can also use: beige/serif/simple/night/default

# Again, if you use 'site-reveal' theme you can select several transitions
# between the slides
# THEME_REVEAL_CONFIG_TRANSITION = 'cube'
# You can also use: page/concave/linear/none/default

# date format used to display post dates.
# (str used by datetime.datetime.strftime)
DATE_FORMAT = '%d-%m-%Y %H:%M'

# Date format used to display post dates, if local dates are used.
# (str used by moment.js)
JS_DATE_FORMAT = DATE_FORMAT

# Date fanciness.
#
# 0 = using DATE_FORMAT and TIMEZONE
# 1 = using JS_DATE_FORMAT and local user time (via moment.js)
# 2 = using a string like “2 days ago”
#
# Your theme must support it, bootstrap and bootstrap3 already do.
DATE_FANCINESS = 2

# One or more folders containing listings to be processed and stored into
# the output. The format is a dictionary of {source: relative destination}.
# Default is:
# LISTINGS_FOLDERS = {'listings': 'listings'}
# Which means process listings from 'listings' into 'output/listings'

# If you want to hide the title of your website (for example, if your logo
# already contains the text), set this to False.
SHOW_BLOG_TITLE = True

# Writes tag cloud data in form of tag_cloud_data.json.
# Warning: this option will change its default value to False in v8!
WRITE_TAG_CLOUD = True

# FAVICONS contains (name, file, size) tuples.
# Used for create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
# For creating favicons, take a look at:
# http://www.netmagazine.com/features/create-perfect-favicon
FAVICONS = {
    ("icon", "/favicon.ico", "16x16"),
    ("icon", "/favicon_128x128.png", "128x128"),
}

# HTML fragments with the Read more... links.
# The following tags exist and are replaced for you:
# {link}                        A link to the full post page.
# {read_more}                   The string “Read more” in the current language.
# {reading_time}                An estimate of how long it will take to read the post.
# {remaining_reading_time}      An estimate of how long it will take to read the post, sans the teaser.
# {min_remaining_read}          The string “{remaining_reading_time} min remaining to read” in the current language.
# {paragraph_count}             The amount of paragraphs in the post.
# {remaining_paragraph_count}   The amount of paragraphs in the post, sans the teaser.
# {{                            A literal { (U+007B LEFT CURLY BRACKET)
# }}                            A literal } (U+007D RIGHT CURLY BRACKET)

INDEX_TEASERS = True
# 'Read more...' for the index page, if INDEX_TEASERS is True (translatable)
# INDEX_READ_MORE_LINK = 'Seguir leyendo...'
# 'Read more...' for the RSS_FEED, if RSS_TEASERS is True (translatable)
INDEX_READ_MORE_LINK = RSS_READ_MORE_LINK = '''
<ul class="pager">
  <li class="previous">
    <a href="{link}">Seguir leyendo...</a>
  </li>
</ul>
'''

RSS_TEASERS = False
# Append a URL query to the RSS_READ_MORE_LINK and the //rss/item/link in
# RSS feeds. Minimum example for Piwik "pk_campaign=rss" and Google Analytics
# "utm_source=rss&utm_medium=rss&utm_campaign=rss". Advanced option used for
# traffic source tracking.
RSS_LINKS_APPEND_QUERY = False

# A HTML fragment describing the license, for the sidebar. Default is "".
# I recommend using the Creative Commons' wizard:
# http://creativecommons.org/choose/
LICENSE = """
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
  <img alt="Licencia Creative Commons" style="border-width:0" src="/cc_by-sa_88x31.png" />
</a>"""



# A small copyright notice for the page footer (in HTML).
# (translatable)
CONTENT_FOOTER = '&copy; 2007-{date} <a href="mailto:{email}">{author}</a> - Powered by <a href="http://getnikola.com">Nikola</a>' + \
    '<br/>El contenido de este blog está bajo la licencia Creative Commons,' + \
    '<br/>la misma está disponible completa <a target="_blank" href="http://creativecommons.org/licenses/by-sa/4.0/">aquí.</a>' + \
    '<br/>{license}'

# Things that will be passed to CONTENT_FOOTER.format().  This is done
# for translatability, as dicts are not formattable.  Nikola will
# intelligently format the setting properly.
# The setting takes a dict. The keys are languages. The values are
# tuples of tuples of positional arguments and dicts of keyword arguments
# to format().  For example, {'en': (('Hello'), {'target': 'World'})}
# results in CONTENT_FOOTER['en'].format('Hello', target='World').
# WARNING: If you do not use multiple languages with CONTENT_FOOTER, this
#          still needs to be a dict of this format.  (it can be empty if you
#          do not need formatting)
# (translatable)
CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE
        }
    )
}

# To use comments, you can choose between different third party comment
# systems, one of "disqus", "livefyre", "intensedebate", "moot",
# "googleplus" or "facebook"
COMMENT_SYSTEM = "disqus"
# And you also need to add your COMMENT_SYSTEM_ID which
# depends on what comment system you use. The default is
# "nikolademo" which is a test account for Disqus. More information
# is in the manual.
COMMENT_SYSTEM_ID = "humitos"

# Create index.html for story folders?
# STORY_INDEX = False
# Enable comments on story pages?
COMMENTS_IN_STORIES = True
# Enable comments on picture gallery pages?
# COMMENTS_IN_GALLERIES = False

# Enable annotations using annotateit.org?
# If set to False, you can still enable them for individual posts and pages
# setting the "annotations" metadata.
# If set to True, you can disable them for individual posts and pages using
# the "noannotations" metadata.
# ANNOTATIONS = False

# Create index.html for page (story) folders?
# WARNING: if a page would conflict with the index file (usually
#          caused by setting slug to `index`), the STORY_INDEX
#          will not be generated for that directory.
# STORY_INDEX = False
# Enable comments on story pages?
# COMMENTS_IN_STORIES = False
# Enable comments on picture gallery pages?
# COMMENTS_IN_GALLERIES = False

# What file should be used for directory indexes?
# Defaults to index.html
# Common other alternatives: default.html for IIS, index.php
INDEX_FILE = "index.html"

# If a link ends in /index.html,  drop the index.html part.
# http://mysite/foo/bar/index.html => http://mysite/foo/bar/
# (Uses the INDEX_FILE setting, so if that is, say, default.html,
# it will instead /foo/default.html => /foo)
# (Note: This was briefly STRIP_INDEX_HTML in v 5.4.3 and 5.4.4)
# Default = False
STRIP_INDEXES = True

# Should the sitemap list directories which only include other directories
# and no files.
# Default to True
# If this is False
# e.g. /2012 includes only /01, /02, /03, /04, ...: don't add it to the sitemap
# if /2012 includes any files (including index.html)... add it to the sitemap
# SITEMAP_INCLUDE_FILELESS_DIRS = True

# List of files relative to the server root (!) that will be asked to be excluded
# from indexing and other robotic spidering. * is supported. Will only be effective
# if SITE_URL points to server root. The list is used to exclude resources from
# /robots.txt and /sitemap.xml, and to inform search engines about /sitemapindex.xml.
ROBOTS_EXCLUSIONS = ["/archive.html", "/category/*.html"]

# Instead of putting files in <slug>.html, put them in
# <slug>/index.html. Also enables STRIP_INDEXES
# This can be disabled on a per-page/post basis by adding
#    .. pretty_url: False
# to the metadata
PRETTY_URLS = True

# If True, publish future dated posts right away instead of scheduling them.
# Defaults to False.
# FUTURE_IS_NOW = False

# If True, future dated posts are allowed in deployed output
# Only the individual posts are published/deployed; not in indexes/sitemap
# Generally, you want FUTURE_IS_NOW and DEPLOY_FUTURE to be the same value.
DEPLOY_FUTURE = False
# If False, draft posts will not be deployed
DEPLOY_DRAFTS = False

# Allows scheduling of posts using the rule specified here (new_post -s)
# Specify an iCal Recurrence Rule: http://www.kanzaki.com/docs/ical/rrule.html
# SCHEDULE_RULE = ''
# If True, use the scheduling rule to all posts by default
# SCHEDULE_ALL = False

# Do you want a add a Mathjax config file?
# MATHJAX_CONFIG = ""

# If you are using the compile-ipynb plugin, just add this one:
# MATHJAX_CONFIG = """
# <script type="text/x-mathjax-config">
# MathJax.Hub.Config({
#     tex2jax: {
#         inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
#         displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ],
#         processEscapes: true
#     },
#     displayAlign: 'left', // Change this to 'center' to center equations.
#     "HTML-CSS": {
#         styles: {'.MathJax_Display': {"margin": 0}}
#     }
# });
# </script>
# """

# Do you want to customize the nbconversion of your IPython notebook?
# IPYNB_CONFIG = {}
# With the following example configuration you can use a custom jinja template
# called `toggle.tpl` which has to be located in your site/blog main folder:
# IPYNB_CONFIG = {'Exporter':{'template_file': 'toggle'}}

# What Markdown extensions to enable?
# You will also get gist, nikola and podcast because those are
# done in the code, hope you don't mind ;-)
# Note: most Nikola-specific extensions are done via the Nikola plugin system,
#       with the MarkdownExtension class and should not be added here.
# MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite']

# Extra options to pass to the pandoc comand.
# by default, it's empty, is a list of strings, for example
# ['-F', 'pandoc-citeproc', '--bibliography=/Users/foo/references.bib']
# PANDOC_OPTIONS = []

# Social buttons. This is sample code for AddThis (which was the default for a
# long time). Insert anything you want here, or even make it empty.
SOCIAL_BUTTONS_CODE = ""

# Show link to source for the posts?
SHOW_SOURCELINK = True

# Modify the number of Post per Index Page
# Defaults to 10
INDEX_DISPLAY_POST_COUNT = 4

# By default, Nikola generates RSS files for the website and for tags, and
# links to it.  Set this to False to disable everything RSS-related.
GENERATE_RSS = True

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a FeedBurner feed or something else.
# RSS_LINK = None

# Show only teasers in the RSS feed? Default to True
# RSS_TEASERS = True

# Strip HTML in the RSS feed? Default to False
# RSS_PLAIN = False

# A search form to search this site, for the sidebar. You can use a Google
# custom search (http://www.google.com/cse/)
# Or a DuckDuckGo search: https://duckduckgo.com/search_box.html
# Default is no search form.
# (translatable)
# SEARCH_FORM = ""
#
# This search form works for any site and looks good in the "site" theme where
# it appears on the navigation bar:
#
# SEARCH_FORM = """
# <!-- Custom search -->
# <form method="get" id="search" action="//duckduckgo.com/"
#  class="navbar-form pull-left">
# <input type="hidden" name="sites" value="%s"/>
# <input type="hidden" name="k8" value="#444444"/>
# <input type="hidden" name="k9" value="#D51920"/>
# <input type="hidden" name="kt" value="h"/>
# <input type="text" name="q" maxlength="255"
#  placeholder="Search&hellip;" class="span2" style="margin-top: 4px;"/>
# <input type="submit" value="DuckDuckGo Search" style="visibility: hidden;" />
# </form>
# <!-- End of custom search -->
# """ % SITE_URL
#
# If you prefer a Google search form, here's an example that should just work:
# SEARCH_FORM = """
# <!-- Custom search with Google-->
# <form id="search" action="//www.google.com/search" method="get" class="navbar-form pull-left">
# <input type="hidden" name="q" value="site:%s" />
# <input type="text" name="q" maxlength="255" results="0" placeholder="Search"/>
# </form>
# <!-- End of custom search -->
#""" % SITE_URL

# Also, there is a local search plugin you can use, based on Tipue, but it requires setting several
# options:

# SEARCH_FORM = """
# <span class="navbar-form pull-left">
# <input type="text" id="tipue_search_input">
# </span>"""
#
# ANALYTICS = """
# <script type="text/javascript" src="/assets/js/tipuesearch_set.js"></script>
# <script type="text/javascript" src="/assets/js/tipuesearch.js"></script>
# <script type="text/javascript">
# $(document).ready(function() {
    # $('#tipue_search_input').tipuesearch({
        # 'mode': 'json',
        # 'contentLocation': '/assets/js/tipuesearch_content.json',
        # 'showUrl': false
    # });
# });
# </script>
# """

# Use content distribution networks for jquery and twitter-bootstrap css and js
# If this is True, jquery is served from the Google CDN and twitter-bootstrap
# is served from the NetDNA CDN
# Set this to False if you want to host your site without requiring access to
# external resources.
# USE_CDN = False

# Extra things you want in the pages HEAD tag. This will be added right
# before </head>
# (translatable)
# EXTRA_HEAD_DATA = ""
# Google Analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
BODY_END = """
<!-- Piwik -->
<script type="text/javascript">
  var _paq = _paq || [];
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u="//elblogdehumitos.com.ar/piwik/";
    _paq.push(['setTrackerUrl', u+'piwik.php']);
    _paq.push(['setSiteId', 1]);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript'; g.async=true; g.defer=true; g.src=u+'piwik.js'; s.parentNode.insertBefore(g,s);
  })();
</script>
<noscript><p><img src="//elblogdehumitos.com.ar/piwik/piwik.php?idsite=1" style="border:0;" alt="" /></p></noscript>
<!-- End Piwik Code -->
"""

# The possibility to extract metadata from the filename by using a
# regular expression.
# To make it work you need to name parts of your regular expression.
# The following names will be used to extract metadata:
# - title
# - slug
# - date
# - tags
# - link
# - description
#
# An example re is the following:
# '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)-(?P<title>.*)\.md'
# FILE_METADATA_REGEXP = None

# If you hate "Filenames with Capital Letters and Spaces.md", you should
# set this to true.
UNSLUGIFY_TITLES = True

# Additional metadata that is added to a post when creating a new_post
# ADDITIONAL_METADATA = {}

# Nikola supports Open Graph Protocol data for enhancing link sharing and
# discoverability of your site on Facebook, Google+, and other services.
# Open Graph is enabled by default.
# USE_OPEN_GRAPH = True

# Nikola supports Twitter Card summaries, but they are disabled by default.
# They make it possible for you to attach media to Tweets that link
# to your content.
#
# IMPORTANT:
# Please note, that you need to opt-in for using Twitter Cards!
# To do this please visit https://cards-dev.twitter.com/validator
#
# Uncomment and modify to following lines to match your accounts.
# Images displayed come from the `previewimage` meta tag.
# You can specify the card type by using the `card` parameter in TWITTER_CARD.
# TWITTER_CARD = {
#     # 'use_twitter_cards': True,  # enable Twitter Cards
#     # 'card': 'summary',          # Card type, you can also use 'summary_large_image',
#                                   # see https://dev.twitter.com/cards/types
#     # 'site': '@website',         # twitter nick for the website
#     # 'creator': '@username',     # Username for the content creator / author.
# }


# Post's dates are considered in UTC by default, if you want to use
# another time zone, please set TIMEZONE to match. Check the available
# list from Wikipedia:
# http://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# (eg. 'Europe/Zurich')
# Also, if you want to use a different time zone in some of your posts,
# you can use the ISO 8601/RFC 3339 format (ex. 2012-03-30T23:00:00+02:00)
TIMEZONE = 'America/Argentina/Buenos_Aires'

# If webassets is installed, bundle JS and CSS to make site loading faster
# USE_BUNDLES = True

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["render_galleries"]

# Add the absolute paths to directories containing plugins to use them.
# For example, the `plugins` directory of your clone of the Nikola plugins
# repository.
# EXTRA_PLUGINS_DIRS = []

# List of regular expressions, links matching them will always be considered
# valid by "nikola check -l"
# LINK_CHECK_WHITELIST = []

# If set to True, enable optional hyphenation in your posts (requires pyphen)
# HYPHENATE = False

# The <hN> tags in HTML generated by certain compilers (reST/Markdown)
# will be demoted by that much (1 → h1 will become h2 and so on)
# This was a hidden feature of the Markdown and reST compilers in the
# past.  Useful especially if your post titles are in <h1> tags too, for
# example.
# (defaults to 1.)
# DEMOTE_HEADERS = 1

# If you don’t like slugified file names ([a-z0-9] and a literal dash),
# and would prefer to use all the characters your file system allows.
# USE WITH CARE!  This is also not guaranteed to be perfect, and may
# sometimes crash Nikola, your web server, or eat your cat.
# USE_SLUGIFY = True

# You can configure the logging handlers installed as plugins or change the
# log level of the default stderr handler.
# WARNING: The stderr handler allows only the loglevels of 'INFO' and 'DEBUG'.
#          This is done for safety reasons, as blocking out anything other
#          than 'DEBUG' may hide important information and break the user
#          experience!

LOGGING_HANDLERS = {
    'stderr': {'loglevel': 'INFO', 'bubble': True},
    # 'smtp': {
    #     'from_addr': 'test-errors@example.com',
    #     'recipients': ('test@example.com'),
    #     'credentials':('testusername', 'password'),
    #     'server_addr': ('127.0.0.1', 25),
    #     'secure': (),
    #     'level': 'DEBUG',
    #     'bubble': True
    # }
}

# Templates will use those filters, along with the defaults.
# Consult your engine's documentation on filters if you need help defining
# those.
# TEMPLATE_FILTERS = {}

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.

GLOBAL_CONTEXT = {
    'has_custom_css': True,
}

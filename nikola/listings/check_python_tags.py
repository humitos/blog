# This script checks if there is a newer tag than the specified in CURRENT_TAG

import conf
import smtplib
import feedparser
from email.mime.text import MIMEText

TAGS_URL = 'http://hg.python.org/cpython/tags'
CURRENT_TAG = 'v3.4.0a2'
ATOM_URL = 'http://hg.python.org/cpython/atom-tags'

rss = feedparser.parse(ATOM_URL)
tag = rss['entries'][0].title

if tag != CURRENT_TAG:
    # Send an email to my account
    text = 'Please go to {} to check it out.'.format(TAGS_URL)
    msg = MIMEText(text)
    msg['From'] = conf.FROMADDR
    msg['To'] = conf.TOADDRS
    subject = '[Python HG] There is a new tag: {tag}'.format(tag=tag)
    msg['Subject'] = subject

    # Credentials
    username = conf.USERNAME
    password = conf.PASSWORD

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.send_message(msg)
    server.quit()

#!/usr/bin/python
import sys
import hashlib
import time

try:
    from urllib.parse import urlsplit
except ImportError:
    from urlparse import urlsplit


def sign_url(url, password, expires=None):
    if expires is None:
        expires = int(time.time()) + (60 * 60 * 12)
    parts = urlsplit(url)
    if parts.query:
        sign = "%s?%s&expires=%s&pass=%s" % (
            parts.path, parts.query, expires, password)
        new = "%s://%s%s?%s&expires=%s&token=" % (
            parts.scheme, parts.netloc, parts.path, parts.query, expires)
    else:
        sign = "%s?expires=%s&pass=%s" % (parts.path, expires, password)
        new = "%s://%s%s?expires=%s&token=" % (
            parts.scheme, parts.netloc, parts.path, expires)
    md5instance = hashlib.md5()
    md5instance.update(sign.encode("ascii"))
    token = md5instance.hexdigest()
    return "%s%s" % (new, token)


expires = int(time.time()) + (60 * 60 * 12)
password = 'xa5aileeph6nah5ooQu'

for url in sys.argv[1:]:
    print sign_url(url, password, expires)

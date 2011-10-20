#!/usr/bin/env python
#
# (C) Copyright 2008-2011 White Magnet Software Private Limited
#
# For more information check http://cachevideos.com/
#

__author__ = """Kulbir Saini <saini@saini.co.in>"""
__docformat__ = 'plaintext'

import re

def check_slutload_video(host, path, query, url):
    matched, website_id, video_id, format, search, queue = True, 'slutload', None, '', True, True

    if re.compile('\.slutload-media\.com').search(host) and re.compile('(.*)\/[a-zA-Z0-9_-]+\.flv').search(path) and path.find('.flv') > -1:
        try:
            video_id = path.strip('/').split('/')[-1]
        except Exception, e:
            pass
    else:
        matched = False

    return (matched, website_id, video_id, format, search, queue)


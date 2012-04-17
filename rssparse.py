import site, re
site.addsitedir('./thirdparty')

from requests import request
from feedparser import parse

__author__ = 'trey'

SEASON_RE = re.compile(r'S(?P<season>[0-9]{2,3})E(?P<episode>[0-9]{2,3})', re.IGNORECASE)
SEASON_ALT_RE = re.compile(r'(?P<season>[0-9]{1,2})x(?P<episode>[0-9]{2,3})')
RESOLUTION_RE = re.compile(r'(?P<resolution>(480|720|1080)p)')

def get_feed(url):
    return parse(request('GET', url).raw)

def print_feed(feed):
    for entry in feed.entries:
        season, episode, resolution, inhd = 0, 0, 0, False
        season_info = SEASON_RE.search(entry.title)
        resolution = RESOLUTION_RE.search(entry.title)

        if resolution:
            resolution = resolution.groups()

        if not season_info:
            season_info = SEASON_ALT_RE.search(entry.title)

        if season_info:
            season, episode = season_info.groups()

        if entry.title.find('HDTV'):
            inhd=True

        print "%s (%s) %s/%s - %s" % (inhd, resolution, season, episode, entry.title)

if __name__ == '__main__':
    feed = get_feed('http://static.demonoid.me/rss/3.193.xml') #TV feed
    print_feed(feed)
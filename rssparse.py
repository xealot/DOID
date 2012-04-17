import site, re
site.addsitedir('./thirdparty')

from requests import request
from feedparser import parse

__author__ = 'trey'

SEASON_RE = re.compile(r'S(?P<season>[0-9]{2,3})E(?P<episode>[0-9]{2,3})', re.IGNORECASE)


def get_feed(url):
    return parse(request('GET', url).raw)

def print_feed(feed):
    for entry in feed.entries:
        season, episode = 0, 0
        season_info = SEASON_RE.search(entry.title)
        from pprint import pprint
        if season_info:
            pprint(season_info.groupdict())
        print "%s/%s - %s" % (season, episode, entry.title)

if __name__ == '__main__':
    feed = get_feed('http://static.demonoid.me/rss/3.193.xml') #TV feed
    print_feed(feed)
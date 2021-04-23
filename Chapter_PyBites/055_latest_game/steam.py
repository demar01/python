"""
Bite 55. Get the latest game releases from Steam's RSS feed
"""

from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"
#<class 'str'>

#1) easy way to do this. Parses Steam's RSS feed and prints output to screen
feed = feedparser.parse(FEED_URL)
type(feed) #<class 'feedparser.util.FeedParserDict'>
type(feed.entries) #list 
for entry in feed.entries:
    print(entry.title + entry.link)

#2) we can instead return a list of Game named tuples

Game = namedtuple('Game', 'title link')
def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    feed = feedparser.parse(FEED_URL)
    return [Game(entry.title, entry.link) for entry in feed.entries]
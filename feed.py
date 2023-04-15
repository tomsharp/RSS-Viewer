import ssl 
from typing import List

import feedparser

def get_feed(rss_url: str) -> feedparser.util.FeedParserDict:
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
    feed = feedparser.parse(rss_url)
    if len(feed.entries) == 0:
        raise ValueError(f"Could not retrieve any entries for feed. feedparser returned: {feed}")
    return feed

def _split_google_rss_entry(entry: str) -> str:
  return entry.link.split("&url=")[1].split("&ct=")[0]

def get_links_from_feed(rss_url: str) -> List[str]:
    feed = get_feed(rss_url)
    return [_split_google_rss_entry(entry) for entry in feed.entries]

import feedparser

d = feedparser.parse("http://www.theverge.com/rss/index.xml")
print d.feed.title
print d.entries[0].title
print d.entries[0].published
print d.entries[0].link
print d.entries[0].description

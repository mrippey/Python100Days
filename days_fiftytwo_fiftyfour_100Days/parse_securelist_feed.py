#This script reads from a static XML file, as opposed to reaching out and pulling down the feed from the internet

import feedparser 
import webbrowser

FEED_FILE = 'securelistfeed.xml'

feed = feedparser.parse(FEED_FILE)

print('\t\tSecurelist RSS Feed Parser')
print()
print("Available Categories: APT reports, Malware descriptions, \
Publications, Malware reports" )

def get_rss_feed_info():
    value = str(input('Enter one of the above categories for recent articles: '))
    print()
    for idx, entry in enumerate(feed.entries, start=1):
        if value in entry.category:
            send_mess = f"{idx:<2}  {entry.published} {entry.title} {entry.link}"
            view_summ = entry.description
            print(send_mess)
    
    view_in_browser = int(input("Pick the corresponding number to open a new browser \
page and view the article: "))
    print()
    print(f"Article {view_in_browser} was selected")
    print()
    prep_article_to_open = feed.entries[int(view_in_browser)-1]
    print(f"Now opening: {prep_article_to_open.link}")
    webbrowser.open(prep_article_to_open.link, new=2)
  
 get_rss_feed_info()
    
    
 TODO: Add functionality to view the description of the selected article instead of opening in a broswer, maybe create Flask App of script

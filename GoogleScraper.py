import urllib2
import sys
from google import google
from bs4 import BeautifulSoup

num_page = 1
url = ""
for args in sys.argv[1:]:
    url += args
    url += " "
url += "lyrics"
search_results = google.search(url, num_page)
for result in search_results:
    if "songtexte.com" in result.link:
        if len(search_results) > 0:
            page = urllib2.urlopen(result.link)
            soup = BeautifulSoup(page.read(), 'html.parser')
            print(soup.find(id="lyrics").get_text())
            exit()

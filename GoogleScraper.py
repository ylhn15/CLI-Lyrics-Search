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
#for result in search_results:
#    print(result.link)
if len(search_results) > 0:
    first_url = search_results[0].link
    page = urllib2.urlopen(first_url)
#    print(page.read())
    soup = BeautifulSoup(page.read(), 'html.parser')
#    print(soup.prettify())
    #print(soup.get_text())
    print(soup.find(id="lyrics").get_text())
#    for div in soup.find_all('div'):
        #print(div.get('lyrics'))

from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
import re

# grab URL, parse links
a_tags = SoupStrainer('a')  # prefilter

# testing data to prevent ban from live site while running tests
# url = open('html.html', 'r')
# soup = BeautifulSoup(url, 'html.parser', parse_only=a_tags)

# live data
url = 'https://pinboard.in/popular'
soup = BeautifulSoup(urlopen(url), 'html.parser', parse_only=a_tags)

# filter all but twitter.com links
# pop_tweets = soup.find_all(href=re.compile('//twitter.com/'), class_='url_display')  # for test file
pop_tweets = soup.find_all(href=re.compile('//twitter.com/'))  # for live site

# format links to HTML page
pop_clean = '<html>\n<body>\n<ul>\n'
for x in pop_tweets:
    del x['class']
    pop_clean += '<li> %s </li>' % (x)
pop_clean += '</ul>\n</body>\n</html>'

soup_clean = BeautifulSoup(pop_clean, 'html.parser')
soup_clean_pretty = soup_clean.prettify()

# write to file
f = open('output.html', 'w')
f.write(soup_clean_pretty)
# print(soup_clean_pretty)
f.close()


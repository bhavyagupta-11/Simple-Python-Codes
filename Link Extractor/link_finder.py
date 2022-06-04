from html.parser import HTMLParser #html.parser is uded to deal with the html of a particular page
from urllib import parse
from urllib.request import urlopen
from main import *

class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag=='a':
            for(attribute,value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url,value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self,message):
        pass


#from bs4 import BeautifulSoup
#from urllib.request import Request, urlopen
#import re

#req = Request("http://slashdot.org")
#html_page = urlopen(req)

#soup = BeautifulSoup(html_page, "lxml")

#links = []
#for link in soup.findAll('a'):
#    links.append(link.get('href'))

#print(links)

import requests 
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


class ScrapeArticles(object):

    def __init__(self):
        
        self.base_url = "https://fireeye.com/blog"


    def get_recent_articles(self):
        try:
            
            response = requests.get(self.base_url)
            response.raise_for_status()
        
        except HTTPError as http_err:
            print(f'Error Found During Processing: {http_err}')
        
        soup = BeautifulSoup(response.text, 'html.parser')
        feye_links = soup.find_all('div', {'class': 'c05 c05v0 row-count-2'})[0]

        print('Most recent articles: \n')
        
        for tag in feye_links.find_all("a"):
            url = tag.get('href')

            print(url)


    def get_all_articles(self):
      try:
        
        response = requests.get(self.base_url)
        response.raise_for_status()
       
      except HTTPError as http_err:
          print(f'Error Found During Processing: {http_err}')
       
      soup = BeautifulSoup(response.text, 'html.parser')
       all_feye_links = soup.find_all('div', {'class': 'c05 c05v0 row-count-2'})[1]
       print('FireEye Stories: ')
       
        for tag in all_feye_links.find_all("a"):
           url = tag.get('href')
      
           print(url)

test1 = ScrapeArticles()
test1.get_recent_articles()
test1.get_all_articles()


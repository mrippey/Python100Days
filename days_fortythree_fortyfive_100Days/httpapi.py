import requests 
import pprint
from dataclasses import dataclass 
from typing import List 

@dataclass
class SearchParams:  
    category: str 
    id: int 
    url: str
    title: str
    description: str 
   
search_data = []


def talk_python_search_terms(srch_term: str) -> List[SearchParams]:
    url = f'http://search.talkpython.fm/api/search?q={srch_term}'

    resp = requests.get(url)
    resp.raise_for_status()

    results = resp.json()

    for x in results.get('results'):
        search_data.append(SearchParams(**x))
    
    # Suppress output to top three results, due to some large results returned
    return search_data[:3] 

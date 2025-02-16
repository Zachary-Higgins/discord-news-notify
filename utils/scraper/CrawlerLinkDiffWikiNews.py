import pandas as pd
import os
from .CrawlerLinkDiff import CrawlerLinkDiff

class CrawlerLinkDiffWikiNews(CrawlerLinkDiff):
   
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      
   @staticmethod
   def extract_links(soup):
      links = []
      texts = []
      
      for e in soup.select("div.current-events-main.vevent li"):
         for li in e.find_all("li"):
            texts.append(li.get_text(strip=True).replace("\n",""))
            links.append(li.find("a", {"class": "external text"}).get("href"))
      return links, texts
      
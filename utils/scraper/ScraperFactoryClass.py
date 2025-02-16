import requests
import os
import json
from weasyprint import HTML
from pathlib import Path
from bs4 import BeautifulSoup, Comment

class ScraperFactoryClass():
   
   default_css = """
      @page {
         /* A4(210mm 297mm) * 1.5  */
         size: 400mm 2000mm;
      }
   """
   
   def __init__(self, url, parser="html.parser"):
      response = requests.get(url)
      self.parser = parser
      self.soup = BeautifulSoup(response.text, self.parser)
      self._remove_scripts()
      
   def do_run(self):
      raise Exception("Must be called from derived class (not super).")
      
   def extract_between_comments(self, start_comment, end_comment, raw=False) -> BeautifulSoup:
      comments = self.soup.find_all(string=lambda x: isinstance(x, Comment))
      start_index = None
      end_index = None
      for i, comment in enumerate(comments):
         if start_comment.replace(' ','') in comment.replace(' ',''):
            start_index = i
         if end_comment.replace(' ','') in comment.replace(' ',''):
            end_index = i
            
      if start_index is not None and end_index is not None:
         content = []
         next_element = comments[start_index].next_sibling
         while next_element and next_element != comments[end_index]:
            content.append(str(next_element))
            next_element = next_element.next_sibling
         extracted_html = "".join(content).strip()
      
      if raw:
         return extracted_html
      return self.convert_html_to_soup(extracted_html)
   
   
   def export_to_pdf(self, file_name=None, css=None):
      file_name = getattr(self, "file_name", self.__class__.__name__)
      if css is None:
         css = self.default_css
      file_dir = os.path.join(os.getcwd(), 'buffer')
      file_path = os.path.join(file_dir, f"{file_name}.pdf")
      HTML(string=str(self.soup)).write_pdf(file_path, stylesheets=[
         f"data:text/css;charset=utf-8,{css}"
      ])
      return file_path
   
   def _remove_scripts(self):
      for script in self.soup.find_all("script"):
         script.decompose()
   
   @staticmethod
   def convert_html_to_soup(html_string, parser="html.parser"):
      return BeautifulSoup(html_string, parser)
   
   @staticmethod
   def extract_links(soup):
      links = []
      texts = []
      for a_tag in soup.find_all("a"):
         links.append(a_tag.get("href"))
         texts.append(a_tag.get_text(strip=True))
      return links, texts
   
   @staticmethod   
   def save_last_run(file_name, data):
      file_dir = os.path.join(os.getcwd(), 'buffer')
      file_path = os.path.join(file_dir, file_name)
      Path(file_dir).mkdir(parents=True, exist_ok=True)
      with open(file_path, "w") as f:
         json.dump(data, f, indent=4)
      return file_path
         
   @staticmethod   
   def load_last_run(file_name):
      file_path = os.path.join(os.getcwd(), 'buffer', file_name)
      with open(file_path, "r") as f:
         return json.loads(f.read())
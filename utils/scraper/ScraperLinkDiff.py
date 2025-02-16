import pandas as pd
import os
from io import StringIO
from .ScraperFactoryClass import ScraperFactoryClass

class ScraperLinkDiff(ScraperFactoryClass):
   
   def __init__(self, file_name, *args, **kwargs):
      super().__init__(*args, **kwargs)
      
      for key, value in kwargs.items():
         setattr(self, key, value)
      file_name = self.__class__.__name__ if file_name is None else file_name
      self.buffer_filename = os.path.join(os.getcwd(), 'buffer', f"{file_name}.json")
   
   def do_run(self):
      links, texts = self.extract_links(self.soup)
      new_run_df = pd.DataFrame({"URL": links, "Link Text": texts}).sort_values("Link Text")
      
      if os.path.exists(self.buffer_filename):
         last_run_data = self.load_last_run(self.buffer_filename)
         last_run_df = pd.read_json(StringIO(last_run_data)) #Supress Pandas Warning
         df_merged = pd.merge(new_run_df, last_run_df, how='outer', indicator=True)
         df_only_new_df = df_merged[df_merged['_merge'] == 'left_only'].drop(columns=['_merge'])
         _ = self.save_last_run(self.buffer_filename, new_run_df.to_json())
         return df_only_new_df
      else:
         self.save_last_run(self.buffer_filename, new_run_df.to_json())
         return pd.DataFrame({})
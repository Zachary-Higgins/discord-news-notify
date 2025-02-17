import os
import requests
from datetime import datetime

class DiscordWebHook():
   
   def __init__(self, webhook_key, **kwargs):         
      for key, value in kwargs.items():
         setattr(self, key, value)
      if webhook_key is None:
         self.webhook_url = getattr(self, "webhook_url", None)
      else:
         self.webhook_url = os.environ.get(webhook_key, None)
      assert self.webhook_url is not None, "Something went terribly wrong."
   
   def do_health_checkin(self, payload):
      payload['embeds'][0]['title'] = "Health Check"
      payload['embeds'][0]['url'] = ""
      payload['embeds'][0]['description'] = f"Health check-in... The time is {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"
      _ = requests.post(self.webhook_url, json=payload)
      
   def do_push_notification(self, payload):
      return requests.post(self.webhook_url, json=payload)
      
   def do_push_file_notification(self, file_name):
      with open(file_name, "rb") as f:
         requests.post(self.webhook_url, files={"file":f})
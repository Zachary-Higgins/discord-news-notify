from utils.scraper.ScraperLinkDiff import ScraperLinkDiff
from utils.notification.DiscordWebhook import DiscordWebHook
from utils.logger.richlogger import log, countdown
import sys
import os

def do_loop(webhook_url=None):
  
  i = 0
  
  while True:
    
    scraper = ScraperLinkDiff("DrudgeReportMon", url="http://drudgereport.com")
    if webhook_url is None:
      notification = DiscordWebHook(webhook_key="drudge_webhook")
    else:
      notification = DiscordWebHook(None, webhook_url=webhook_url)
    
    if i % 36 == 0:
      notification.do_health_checkin()
    
    new_df = scraper.do_run()

    if len(new_df) > 0:
      
      embed = {
        "author": {
          "name": "Drudge Scraper Bot",
        },
        "title": "New Links Hit The Drudge",
        "url": "http://drudgereport.com",
        "description": "New links have been detected @ [hyperlink](http://drudgereport.com)",
        "color": 15258703,
        "fields": [
          {
              "name": row['Link Text'],
              "value": row['URL']
          } for index, row in new_df.iterrows()
        ]
      }
      
      notification.do_push_notification(embed=embed)
      export_file = scraper.export_to_pdf()
      notification.do_push_file_notification(export_file)
        
    else:
      log.info("Dataframe results were empty. Skipping.")
    
    i = i+1
    
    countdown(300)
    
if __name__ == '__main__':
  log.info("Initializing DrudgeMon")
  if len(sys.argv) < 2:
    webhook_url = os.environ.get("drudge_webhook", None)
    if webhook_url is None:
      log.critical("Webhook URL not found.")
      raise Exception("Must provide the webhook URL.")
  else:
    webhook_url = sys.argv[1]
  log.info("Webhook URL set. Running loop...")
  do_loop(webhook_url)
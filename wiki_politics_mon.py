from utils.scraper.CrawlerLinkDiffWikiNews import CrawlerLinkDiffWikiNews
from utils.notification.DiscordWebhook import DiscordWebHook
from utils.logger.richlogger import log, countdown
import sys
import os


def do_loop(webhook_url=None):
  
  i = 0
  
  while True:
    
    crawler = CrawlerLinkDiffWikiNews("WikiPoliticsMon", url="https://en.wikipedia.org/wiki/Portal:Current_events")
    if webhook_url is None:
      notification = DiscordWebHook(webhook_key="wikipolitics_webhook")
    else:
      notification = DiscordWebHook(None, webhook_url=webhook_url)
    
    if i % 36 == 0:
      notification.do_health_checkin()
    
    new_df = crawler.do_run()

    if len(new_df) > 0:
      
      embed = {
        "author": {
          "name": "Wiki Politics Crawler Bot",
        },
        "title": "New Links Hit Wiki Politics",
        "url": "https://en.wikipedia.org/wiki/Portal:Current_events",
        "description": "New links have been detected @ [hyperlink](https://en.wikipedia.org/wiki/Portal:Current_events)",
        "color": 15258703,
        "fields": [
          {
              "name": row['Link Text'],
              "value": row['URL']
          } for index, row in new_df.iterrows()
        ]
      }
      
      notification.do_push_notification(embed=embed)
      export_file = crawler.export_to_pdf()
      notification.do_push_file_notification(export_file)
        
    else:
      log.info("Dataframe results were empty. Skipping.")
    
    i = i+1
    
    countdown(300)
    
if __name__ == '__main__':
  log.info("Initializing WikiPoliticsMon")
  if len(sys.argv) < 2:
    webhook_url = os.environ.get("drudge_webhook", None)
    if webhook_url is None:
      log.critical("Webhook URL not found.")
      raise Exception("Must provide the webhook URL.")
  else:
    webhook_url = sys.argv[1]
  log.info("Webhook URL set. Running loop...")
  do_loop(webhook_url)
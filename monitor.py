from utils.notification.DiscordWebhook import DiscordWebHook
from utils.logger.richlogger import log, countdown
from configs import configs
import os
import sys


def get_webhook_url(config):
	webhook_url = os.environ.get(config['webhook_env_key'], None)
	assert webhook_url is not None, f"Environment parameter not set. Webhook as arg not implemented yet. Please set {config['webhook_env_key']}."
	return webhook_url


def do_healthcheck(config):
   log.info("Sending health check.")
   webhook_url = get_webhook_url(config)
   notification_hc = config['notification_config'].copy()
   notification = DiscordWebHook(None, webhook_url=webhook_url)
   notification.do_health_checkin(notification_hc)
   log.info("Health check complete.")


def do_run(config):
   log.info("Starting loop.")
   monitor_class = config['monitor_class']
   monitor_name = config['monitor_name']
   monitor_url = config['monitor_url']
   webhook_url = get_webhook_url(config)
   scraper = monitor_class(monitor_name, monitor_url)
   notification = DiscordWebHook(None, webhook_url=webhook_url)
   payload = config['notification_config'].copy()
   
   new_df = scraper.do_run()
   
   if len(new_df) > 0:
      fields = [
			{
				"name": row['Link Text'],
				"value": row['URL']
			} for index, row in new_df.iterrows()
		]
      
      payload['embeds'][0]['fields'] = fields
      
      notification.do_push_notification(payload)
      export_file = scraper.export_to_pdf()
      notification.do_push_file_notification(export_file)
      log.info("New links detected. Sending notification.")
   
   else:
      log.warning("Dataframe results were empty. Skipping.")
      
   log.info("Loop complete.")
			

def do_loop(key):
	i = 0
	config = configs[key]
	log.info("Configuration loaded.")
		
	while True:
		
		loop_healthcheck = config['loop_healthcheck']
		if i % loop_healthcheck == 0:
			do_healthcheck(config)
		
		do_run(config)
		
		i = i+1
  
		countdown(config['loop_delay'])
  
  
if __name__ == '__main__':
   keys = [x for x in configs.keys()]
   if len(sys.argv) < 2:
      key = input(f"Please provide one of: {", ".join(keys)} » ")
   else:
      key = sys.argv[1]
   do_loop(key)
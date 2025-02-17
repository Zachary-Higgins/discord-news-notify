from utils.scraper.ScraperLinkDiff import ScraperLinkDiff
from utils.scraper.ScraperLinkDiffWikiNews import ScraperLinkDiffWikiNews

configs = {
	"Drudge": {
		"monitor_name": "Drudge Report Monitor",
		"monitor_url": "http://drudgereport.com",
		"monitor_class": ScraperLinkDiff,
		"loop_delay": 300,
		"loop_healthcheck": 36,
		"webhook_env_key": "drudge_webhook",
		"notification_config": {
				"username": "Captain Hook",
				"avatar_url": "",
				"content": "",
				"embeds": [
					{
						"author": {
							"name": "Drudge Scraper Bot",
						},
						"title": "New Links Hit The Drudge",
						"url": "http://drudgereport.com",
						"description": "New links have been detected @ [hyperlink](http://drudgereport.com)",
						"color": 15258703,
						"fields": []
					}
				]
		}      
	},
	"WikiCurrentEvents": {
		"monitor_name": "Wiki Current Events",
		"monitor_url": "https://en.wikipedia.org/wiki/Portal:Current_events",
		"monitor_class": ScraperLinkDiffWikiNews,
		"loop_delay": 300,
		"loop_healthcheck": 36,
		"webhook_env_key": "wikipolitics_webhook",
		"notification_config": {
				"username": "Captain Hook",
				"avatar_url": "",
				"content": "",
				"embeds": [
					{
						"author": {
							"name": "Wikipedia Current Events Scraper Bot",
						},
						"title": "New Links Hit Wikipedia Current Events",
						"url": "https://en.wikipedia.org/wiki/Portal:Current_events",
						"description": "New links have been detected @ [hyperlink](https://en.wikipedia.org/wiki/Portal:Current_events)",
						"color": 15258703,
						"fields": []
					}
				]
		}        
	}
}

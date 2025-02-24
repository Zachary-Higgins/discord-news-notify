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
            "avatar_url": "https://styles.redditmedia.com/t5_2qmol/styles/communityIcon_tabjv9ahw3m71.jpg?format=pjpg&s=f32278b9b079eb822b28ecaa29707e99ebfb4878",
            "content": "",
            "embeds": [
               {
                  "author": {
                     "name": "Drudge Scraper Bot",
                  },
                  "title": "New Links Hit The Drudge",
                  "url": "http://drudgereport.com",
                  "description": "New links have been detected @ [DrudgeReport](http://drudgereport.com)",
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
            "avatar_url": "https://styles.redditmedia.com/t5_2qmol/styles/communityIcon_tabjv9ahw3m71.jpg?format=pjpg&s=f32278b9b079eb822b28ecaa29707e99ebfb4878",
            "content": "",
            "embeds": [
               {
                  "author": {
                     "name": "Wikipedia Current Events Scraper Bot",
                  },
                  "title": "New Links Hit Wikipedia Current Events",
                  "url": "https://en.wikipedia.org/wiki/Portal:Current_events",
                  "description": "New links have been detected @ [Wikipedia, Current Events](https://en.wikipedia.org/wiki/Portal:Current_events)",
                  "color": 15258703,
                  "fields": []
               }
            ]
      }        
   }
}

## Introduction
This is a web crawler/scraper project designed to monitor news aggregators for updates. These monitors run in an infinite loop (with intervals of 5 minutes or more, being respectful of our sources). On each iteration, the monitors compare the current results to the previous run. If new results (links or headlines) are found, they will send a Discord notification to the configured webhook.

_I am not affiliated with any news agency or media company. As always, the news can be biased, as can the headlines that aggregators choose to display. This information is simply meant to signal that an event is occurring which may be of interest to the reader._

## Contributions
This is a project I created to test whether it could be a viable way to monitor news aggregation websites. I am unsure whether anyone will find it useful, but if you do, please feel free to contribute in any way you see fit. PRs and issues are welcome!

## Install (Dependencies):
- Install Weazy Print: https://github.com/Kozea/WeasyPrint/releases
- MYSYS2 https://www.msys2.org/#installation
- CMD > `pacman -S mingw-w64-x86_64-pango`

## Requirements
- Python 3.9 (or higher)
- `pip install -r requirements.txt`


## Usage
- Refer to the following link for creating a discord webhook: https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks
- There are currently 2 crawlers setup (more if I didn't update the readme yet.)
- #### Webhooks as Command Line Parameters
   - drudge_mon -> `python ./drudge_mon.py "<insert webhook URL>"`
   - wiki_politics_mon -> `python ./wiki_politics_mon.py "<insert webhook URL>"`
- #### Webhooks as Environment Parameters
   - Webhook must exist as a environment param (useful for docker installations). This isn't fully fleshed out so plan on reading some python to determine the appropriate environment variable names (for now).
   - You can start with the drudge_mon.py or wiki_politics_mon.py.
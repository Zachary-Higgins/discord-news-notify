import requests
import os
import json
from weasyprint import HTML
from pathlib import Path
from bs4 import BeautifulSoup, Comment


html = """<div role="region" aria-label="February 16" id="2025_February_16" class="current-events-main vevent">
	<div class="current-events-heading plainlinks">
		<div class="current-events-title" role="heading">
			<span class="summary">February&#160;16,&#160;2025<span style="display:none">&#160;(<span class="bday dtstart published updated itvstart">2025-02-16</span>)</span> (Sunday)</span>
		</div>
		<ul class="current-events-navbar editlink noprint">
			<li>
				<a class="external text" href="https://en.wikipedia.org/w/index.php?title=Portal:Current_events/2025_February_16&amp;action=edit&amp;editintro=Portal:Current_events/Edit_instructions">edit</a>
			</li>
			<li>
				<a class="external text" href="https://en.wikipedia.org/w/index.php?title=Portal:Current_events/2025_February_16&amp;action=history">history</a>
			</li>
			<li>
				<a class="external text" href="https://en.wikipedia.org/w/index.php?title=Portal:Current_events/2025_February_16&amp;action=watch">watch</a>
			</li>
		</ul>
	</div>
	<div class="current-events-content description">
		<p>
			<b>Armed conflicts and attacks</b>
		</p>
		<ul>
			<li>
				<a href="/wiki/Kivu_conflict" title="Kivu conflict">Kivu conflict</a>
				<ul>
					<li>
						<a href="/wiki/M23_campaign_(2022%E2%80%93present)" title="M23 campaign (2022–present)">M23 campaign</a>
						<ul>
							<li>
								<a href="/wiki/2025_Bukavu_offensive" title="2025 Bukavu offensive">2025 Bukavu offensive</a>
								<ul>
									<li>Local officials and residents report that <a href="/wiki/Rwanda" title="Rwanda">Rwanda</a>-backed <a href="/wiki/March_23_Movement" title="March 23 Movement">M23 forces</a> have taken over the center of <a href="/wiki/Bukavu" title="Bukavu">Bukavu</a>, the capital of <a href="/wiki/South_Kivu" title="South Kivu">South Kivu</a> in eastern <a href="/wiki/Democratic_Republic_of_the_Congo" title="Democratic Republic of the Congo">DR Congo</a>. <a rel="nofollow" class="external text" href="https://www.aljazeera.com/news/2025/2/16/dr-congos-m23-rebels-enter-centre-of-strategic-city-bukavu-report">(Al Jazeera)</a>
									</li>
									<li>The <a href="/wiki/Government_of_the_Democratic_Republic_of_the_Congo" title="Government of the Democratic Republic of the Congo">Government of the Democratic Republic of the Congo</a> acknowledges the fall of Bukavu to M23 rebels, and urges its roughly two million residents to <a href="/wiki/Shelter-in-place" title="Shelter-in-place">shelter in place</a>. <a rel="nofollow" class="external text" href="https://www.bbc.com/news/articles/c0rqr8q5v52o">(BBC News)</a>
									</li>
								</ul>
							</li>
						</ul>
					</li>
				</ul>
			</li>
			<li>
				<a href="/wiki/Russian_invasion_of_Ukraine" title="Russian invasion of Ukraine">Russian invasion of Ukraine</a>
				<ul>
					<li>
						<a href="/wiki/Mykolaiv_strikes_(2022%E2%80%93present)" title="Mykolaiv strikes (2022–present)">Mykolaiv strikes</a>, <a href="/wiki/Russian_strikes_against_Ukrainian_infrastructure_(2022%E2%80%93present)" title="Russian strikes against Ukrainian infrastructure (2022–present)">Russian strikes against Ukrainian infrastructure</a>
						<ul>
							<li>
								<a href="/wiki/Russia" title="Russia">Russia</a> launches <a href="/wiki/Drone_strike" class="mw-redirect" title="Drone strike">drone strikes</a> across <a href="/wiki/Ukraine" title="Ukraine">Ukraine</a>, injuring at least one person and damaging a <a href="/wiki/Thermal_power_station" title="Thermal power station">thermal power station</a> in <a href="/wiki/Mykolaiv" title="Mykolaiv">Mykolaiv</a>, leaving 46,000 people without heat. Ukraine says that it shot down 95 of 143 drones while disrupting 46 others by <a href="/wiki/Electronic_countermeasure" title="Electronic countermeasure">electronic countermeasures</a>. <a rel="nofollow" class="external text" href="https://www.reuters.com/world/europe/russian-overnight-attacks-injure-one-damage-infrastructure-houses-ukraine-2025-02-16/">(Reuters)</a>
							</li>
						</ul>
					</li>
				</ul>
			</li>
		</ul>
		<p>
			<b>International relations</b>
		</p>
		<ul>
			<li>
				<a href="/wiki/Russia%E2%80%93United_States_relations" title="Russia–United States relations">Russia–United States relations</a>, <a href="/wiki/Peace_negotiations_in_the_Russian_invasion_of_Ukraine" title="Peace negotiations in the Russian invasion of Ukraine">Peace negotiations in the Russian invasion of Ukraine</a>
				<ul>
					<li>
						<a href="/wiki/U.S._Secretary_of_State" class="mw-redirect" title="U.S. Secretary of State">U.S. Secretary of State</a>
						<a href="/wiki/Marco_Rubio" title="Marco Rubio">Marco Rubio</a> leads a U.S. delegation, along with <a href="/wiki/United_States_National_Security_Advisor" class="mw-redirect" title="United States National Security Advisor">National Security Advisor</a>
						<a href="/wiki/Michael_Waltz" title="Michael Waltz">Michael Waltz</a> and <a href="/wiki/Ambassadors_of_the_United_States" title="Ambassadors of the United States">Special Envoy</a>
						<a href="/wiki/Steve_Witkoff" title="Steve Witkoff">Steve Witkoff</a>, to <a href="/wiki/Riyadh" title="Riyadh">Riyadh</a>, <a href="/wiki/Saudi_Arabia" title="Saudi Arabia">Saudi Arabia</a>, for initial talks with Russia. A Russian source reports that the meeting will occur on 18 February, and that the Russian delegation is expected to include <a href="/wiki/Minister_of_Foreign_Affairs_(Russia)" title="Minister of Foreign Affairs (Russia)">Foreign Minister</a>
						<a href="/wiki/Sergey_Lavrov" title="Sergey Lavrov">Sergey Lavrov</a>, <a href="/wiki/Presidential_Administration_of_Russia" title="Presidential Administration of Russia">Presidential Aide</a>
						<a href="/wiki/Yuri_Ushakov" title="Yuri Ushakov">Yuri Ushakov</a>, and <a href="/wiki/Director_of_the_Foreign_Intelligence_Service" title="Director of the Foreign Intelligence Service">SVR Director</a>
						<a href="/wiki/Sergey_Naryshkin" title="Sergey Naryshkin">Sergey Naryshkin</a>. <a rel="nofollow" class="external text" href="https://apnews.com/article/russia-ukraine-war-trump-talks-negotiations-saudi-51b77cdf699f13ad16cb00bbf371b840">(AP)</a>
						<a rel="nofollow" class="external text" href="https://www.kommersant.ru/doc/7513890?from=top_main_1">(<i>Kommersant</i>) </a>
					</li>
				</ul>
			</li>
		</ul>
	</div>
</div>"""

soup = BeautifulSoup(html, "html.parser")

for e in soup.select("div.current-events-main.vevent li"):
   for li in e.find_all("li"):
      print(li.get_text().replace("\n",""))
      print(li.find("a", {"class": "external text"}).get("href"))
      print("-"*24)


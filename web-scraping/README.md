# Fandom Wikis and Web Scraping Homework

## Chosen Wiki
For this assignment, I chose the Cookie Clicker Wiki and focused on the Achievements page.

## Why I Chose This Topic
For this assignment initially I was seeking to scrape a fandom Wiki for Cookie Run: Kingdom as it was a game that I have briefly played and liked in the past years.  When I reviewed the robots.txt,  it appeared  that scraping was allowed unless a page specifically cited that it was not. however when I attempted to scrape I found that I was being blocked and I was not able to extract any data.  That is why I pivoted this assignment to scrape Cookie Clicker as its policies allowed for scraping more broadly. I like that it was a game that I'm still quite familiar with given its popularity during primary and secondary education. And that it followed the theme of cookies. 

## What I Scraped
I scraped the Cookie Clicker Wiki Achievements page and collected data realted to the achievements into a CSV and JSON file.

The fields I collected include:
- category
- achievement name
- description
- id
- source page

## Why This Data Could Be Useful to Researchers
I believe these scraped achievements, numbering nearly 700 in total, show that players can display remarkable persistence when given a structured system of rewards and milestones. Researchers interested in understanding the elements of a game that drive popularity and engagement could benefit from examining the achievement structure alongside additional data, such as how many players reached each achievement level, especially since many of the achievements follow a progression series rather than existing as isolated milestones. This game is particularly interesting for researchers because it is an idle game, meaning that it requires minimal user input as progression increasingly becomes automated through features like automatic clickers. That makes it relevant not only for game studies researchers, but also for those interested in understanding why users are drawn to systems that require little activity yet still sustain attention and investment despite offering no tangible real-world reward.

Example question that can be researched in part with the scraped data: 

How do structured achievement systems in idle games like Cookie Clicker sustain player engagement despite requiring minimal ongoing user input?

## robots.txt / Policy Check
I checked the site's robots.txt before scraping.

The robots.txt does not block scraping and only had some restrictions for technical pathway access. My scripts kept to these permissions by requesting from only public article pages where all the relevant information was regardless of restriction. 

## Tools Used
- Python
- cloudscraper
- BeautifulSoup
- csv
- json

## Output Files
- fandom_wiki_scraping.py
- cookie_clicker_achievements.csv
- cookie_clicker_achievements.json

## How to Run
Install dependencies:

```bash
pip3 install cloudscraper beautifulsoup4
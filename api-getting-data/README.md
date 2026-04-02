# API Getting Data Homework Overview

For this assingment, I used APIs from the Library of Congress and Europena to pull connected cultural materials (media and records) related to the women's suffrage protests in the United States from the two archives.  

I chose this topic because the women's suffrage movement gave way for great participation in politics for women in the United States. Much of the progress made in this movement was through strategic protests which made me chose it as my narrower choice. 

My script:
- makes a request to the Library of Congress API
- prints out the response
- selects one returned record related to suffrage protest materials
- uses that item’s information to search Europeana for a related record
- prints out the Europeana response
- saves cleaned item data from both APIs into a JSON file

## Files
- `getting_culture.py` – main Python script
- `loc_api_culture_data.json` – saved cleaned data
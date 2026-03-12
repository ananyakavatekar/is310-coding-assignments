Welcome! This script is intended to allow users like you to enter and aggregate data about influencial women that impacted politics in the United States!

## Fields of information we are gathering
- name
- time_period
- political_role_or_influence
- major_contribution

## Requirements 
- Python (3) 
- rich

### How to install Rich
In computer terminal enter: pip install rich
(you may need to try alternative variations)

### How to enter data!
1. First run the script through the bash command: python3 cli_data_entry.py
2. In your terminal you will now see a colored datatable with the above fields including some examples of influencial women already populated
3. Below this table you will see that there are prompts asking you for the fields of data for any female political leader of your choice
 - the person's name
 - the time period they influenced 
 - the political role or influence they had
 - their major contribution to the world around them
4. Once you enter the information one by one, the script will print your entry back and ask if it is correct
5. If you type yes, the entry will be kept
5. If you type no, the script will ask you to re-enter that record
7. You will then be asked if you want to add another entry
8. When you are finished, the script will have saved all entries you have verified to a CSV file called women_politics_data.csv
9. If you want to check out the data enter cat women_politics_data.csv
 



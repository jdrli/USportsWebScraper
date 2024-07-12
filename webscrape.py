from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

# driver.get("https://universitysport.prestosports.com/sports/mvball/" + str(year-1) + "-" + str(year)[-2:] + "/teams")

# This function updates the full stats table with every team in it for the given year. 
def UpdateTeams(year):
    driver = webdriver.Chrome()
    driver.get("https://universitysport.prestosports.com/sports/mvball/2023-24/teams")
    statsdoc = BeautifulSoup(driver.page_source, 'html.parser')

    print(statsdoc.prettify())
    driver.quit

# UpdateTeams(2024)

def UpdatePlayers(year):
    url = "https://universitysport.prestosports.com/sports/mvball/" + str(year-1) + "-" + str(year)[-2:] + "/players?sort=&view=&pos=p&r=0"
    stats = requests.get(url)
    statsdoc = BeautifulSoup(stats.text, 'html.parser')

    tables = statsdoc.find_all('table')

    # atk_data = []
    # for table in tables:
    #     rows = table.find_all('tr')
    #     header_data = []
    #     for row in rows:
    #         cols = row.find_all(['td', 'th'])
    #         processed_cols = []
    #         for i, col in enumerate(cols):
    #             text = col.text.strip()
    #             if i == 1:  # Apply replace operations only on the first column
    #                 text = text.replace('  ', '').replace('\n', ' ').replace('\r', '')
    #             processed_cols.append(text)
    #         header_data.append(processed_cols)
    #     atk_data.append(header_data)
    atk_data = []
    for table in tables:
        rows = table.find_all('tr')
        header_data = []
        for row in rows:
            cols = row.find_all(['td', 'th'])
            cols = [col.text.strip() for col in cols]
            header_data.append(cols)
        atk_data.append(header_data)


    headers = atk_data[0][0]
    atk_df = pd.DataFrame(atk_data[0][1:], columns=headers)
    atk_df = atk_df.drop(columns = atk_df.columns[:1])

    atk_df.iloc[:, 0] = atk_df.iloc[:, 0].str.replace('  ', '').str.replace('\n', ' ').str.replace('\r', '').str.strip()

    print(atk_df)
    print("Player statistics updated for " + str(year-1) + "-" + str(year)[-2:] + "!")
    return(atk_df)

    print(df)

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', None)
UpdatePlayers(2024)

# def UpdateTeams(year):
#     url = "https://universitysport.prestosports.com/sports/mvball/" + str(year-1) + "-" + str(year)[-2:] + "/teams"
#     stats = requests.get(url)
#     statsdoc = BeautifulSoup(stats.text, 'html.parser')
#     table_rows = statsdoc.find_all('tr')
    
#     headers = [header.get_text() for header in table_rows[0].find_all('th')]

#     data = []
#     for row in table_rows[1:]:
#         team_data = []
#         cols = row.find_all(['td', 'th'])
#         cols = [col.text.strip() for col in cols]
#         team_data.append(cols)
#         cells = row.find_all('td')
#         if len(cells) > 0:
#             row_data = [cell.get_text(strip=True) for cell in cells]
#             data.append(row_data)

#     teams_df = pd.DataFrame(data, columns=headers)
    
#     # data = []
#     # for row in table_rows[1:]:  # Skip the header row
#     #     cells = row.find_all('td')
#     #     if len(cells) > 0:  # Ensure the row is not empty
#     #         row_data = [cell.get_text(strip=True) for cell in cells]
#     #         data.append(row_data)
    
#     # teams_df = pd.DataFrame(data, columns=headers)
#     print(teams_df)
    
    # print(table_rows)

    # print(statsdoc.prettify())
    # for table in tables:

# UpdateTeams(2024)

def UpdateOffensive(year):
    url = "https://universitysport.prestosports.com/sports/mvball/" + str(year-1) + "-" + str(year)[-2:] + "/teams"
    stats = requests.get(url)
    statsdoc = BeautifulSoup(stats.text, 'html.parser')
    tables = statsdoc.find_all('table')

    atk_data = []
    for table in tables:
        rows = table.find_all('tr')
        team_data = []
        for row in rows:
            cols = row.find_all(['td', 'th'])
            cols = [col.text.strip() for col in cols]
            team_data.append(cols)
        atk_data.append(team_data)

    headers = atk_data[0][0]
    atk_df = pd.DataFrame(atk_data[0][1:], columns=headers)
    atk_df = atk_df.drop(columns = atk_df.columns[:1])

    print(atk_df)
    print("Teams statistics updated for " + str(year-1) + "-" + str(year)[-2:] + "!")
    return(atk_df)

# UpdateOffensive(2024)
    
def UpdateDefensive(year):
    return year

# UpdateDefensive(2024)
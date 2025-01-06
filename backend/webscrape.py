from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

# driver.get("https://universitysport.prestosports.com/sports/mvball/" + str(year-1) + "-" + str(year)[-2:] + "/teams")

def PlayerUpdateAtk(year):
    url = "https://universitysport.prestosports.com/sports/mvball/" + str(year-1) + "-" + str(year)[-2:] + "/players?sort=&view=&pos=p&r=0"
    stats = requests.get(url)
    statsdoc = BeautifulSoup(stats.text, "html.parser")
    tables = statsdoc.find_all("table")

    atk_data = []
    for table in tables:
        rows = table.find_all("tr")
        header_data = []
        for row in rows:
            cols = row.find_all(["td", "th"])
            cols = [col.text.strip() for col in cols]
            header_data.append(cols)
        atk_data.append(header_data)

    headers = atk_data[0][0]
    atk_df = pd.DataFrame(atk_data[0][1:], columns=headers)
    atk_df = atk_df.drop(columns = atk_df.columns[:1])

    # Parsing the name column to remove inconsistent formatting on the website.
    atk_df.iloc[:, 0] = atk_df.iloc[:, 0].str.replace("  ", "").str.replace("\n", " ").str.replace("\r", "").str.strip()

    # print(atk_df)
    # print("Player statistics updated for " + str(year-1) + "-" + str(year)[-2:] + "!")
    return(atk_df)

# PlayerUpdateAtk(2024)

def TeamUpdateAtk(year):
    # url = "https://universitysport.prestosports.com/sports/mvball/" + str(year-1) + "-" + str(year)[-2:] + "/teams"
    url = "https://universitysport.prestosports.com/sports/mvball/2023-24/teams?sort=d&r=0&pos=df"
    stats = requests.get(url)
    time.sleep(3)
    statsdoc = BeautifulSoup(stats.text, "html.parser")
    tables = statsdoc.find_all("table")

    atk_data = []
    for table in tables:
        rows = table.find_all("tr")
        team_data = []
        for row in rows:
            cols = row.find_all(["td", "th"])
            cols = [col.text.strip() for col in cols]
            team_data.append(cols)
        atk_data.append(team_data)

    headers = atk_data[0][0]
    atk_df = pd.DataFrame(atk_data[0][1:], columns=headers)
    atk_df = atk_df.drop(columns = atk_df.columns[:1])

    # print(atk_df)
    # print("Team offensive statistics updated for " + str(year-1) + "-" + str(year)[-2:] + "!")
    return(atk_df)
    
TeamUpdateAtk(2024)

# def UpdateDefensive(year):
#     return year

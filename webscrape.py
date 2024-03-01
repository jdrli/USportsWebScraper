from bs4 import BeautifulSoup
import requests
import pandas as pd


# This function updates the stats 
def UpdateTeams(year):
    url = f"https://universitysport.prestosports.com/sports/mvball/{year}-{year+1}/teams"
    stats = requests.get(url)
    statsdoc = BeautifulSoup(stats.text, 'html.parser')

    tables = statsdoc.find_all('table')

    data = []
    for table in tables:
        rows = table.find_all('tr')
        team_data = []
        for row in rows:
            cols = row.find_all(['td', 'th'])
            cols = [col.text.strip() for col in cols]
            team_data.append(cols)
        data.append(team_data)

    headers = data[0][0]
    df = pd.DataFrame(data[0][1:], columns=headers)

    for team_data in data[1:]:
        df = pd.concat([df, pd.DataFrame(team_data[1:], columns=headers)], ignore_index=True)

    #print(df)
    print("Teams' statistics updated!")
    return(df)

def UpdatePlayers():
    url = "https://universitysport.prestosports.com/sports/mvball/2023-24/players?sort=&view=&pos=p&r=0"
    stats = requests.get(url)
    statsdoc = BeautifulSoup(stats.text, 'html.parser')

    tables = statsdoc.find_all('table')

    data = []
    for table in tables:
        rows = table.find_all('tr')
        team_data = []
        for row in rows:
            cols = row.find_all(['td', 'th'])
            cols = [col.text.strip() for col in cols]
            team_data.append(cols)
        data.append(team_data)

    headers = data[0][0]
    df = pd.DataFrame(data[0][1:], columns=headers)

    for team_data in data[1:]:
        df = pd.concat([df, pd.DataFrame(team_data[1:], columns=headers)], ignore_index=True)

    print(df)

UpdatePlayers()
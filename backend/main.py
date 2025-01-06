import webscrape
import time

def main():
    TeamStats = webscrape.TeamUpdateAtk(2024)
    PlayerStats = webscrape.PlayerUpdateAtk(2024)
    print(PlayerStats)
    print(TeamStats)


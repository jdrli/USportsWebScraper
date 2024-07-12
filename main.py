from webscrape import UpdateTeams
import time
TeamStats = []
yearnum = 2024
statscount = 1
# while yearnum > 2021:
#     TeamStats.append(UpdateTeams(yearnum))
#     yearnum -= 1
#     statscount += 1

TeamStats.append(UpdateTeams(yearnum))



time.sleep(1)
for stats in TeamStats:
    print(stats)
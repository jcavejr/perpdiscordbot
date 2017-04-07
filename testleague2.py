import os
from cassiopeia import riotapi

DEV_KEY = os.environ['DEV_KEY']
riotapi.set_region('NA')
riotapi.set_api_key(DEV_KEY)

playername = input('Enter your summoner name: ')
summoner = riotapi.get_summoner_by_name(playername)

match_history = riotapi.get_match_list(summoner, 5)

counter = 0
for match in match_history:
    if str(match.role) == 'Role.support':
        counter += 1
    if counter == 3:
        print('You are a support main')
        break


    

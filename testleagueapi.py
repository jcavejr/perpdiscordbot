#Write a program that asks for summoner name + region, determines
#if they're a support main, asks the user to change the name of a
#rune page, then checks to see if they changed the rune page name
import os
from cassiopeia import riotapi

DEV_KEY = os.environ['RIOT_DEV_KEY']
riotapi.set_region('NA')
riotapi.set_api_key(DEV_KEY)

#Function to use text file containing names of all supports to create a list of champion objects
def get_champ_list():
    file = open('supports.txt', 'r')
    champ_names = []
    for line in file:
        champ_names.append(line.rstrip())
    file.close()
    champ_list = []
    for item in champ_names:
        champ = riotapi.get_champion_by_name(item)
        champ_list.append(champ)
    return champ_list

#list of support champion objects
supports = get_champ_list()
#counter that will be used to calculate number of games played as support
counter = 0
#ask user for their summoner name. remove white space and make all characters lower case
tplayername = input('Enter your summoner name: ')
tplayername = tplayername.lower()
playername = ''
for ch in tplayername:
    if not ch == ' ':
        playername = playername + ch

#use playername to return a player object
summoner = riotapi.get_summoner_by_name(playername)
#ask user for region and set that region
region = input('Enter your region: ')
riotapi.set_region(region)
#get the last 10 (ranked) matches from that summoner. store as list of match IDs
match_history = riotapi.get_match_list(summoner, 10)
#iterate through each match in the list
for match in match_history:
    match_obj = riotapi.get_match(match)
    players = match_obj.participants
    for player in players:
        summonername = ''
        for ch in player.summoner_name:
            if not ch == ' ':
                summonername = summonername + ch
        summonername = summonername.lower()
        if summonername == playername:
            print(player.champion)
            if player.champion in supports:
                counter = counter + 1

print(counter)
if counter >= 5:
    print('You are a support')

#!/usr/bin/env python3.5
import discord, os
from cassiopeia import riotapi
#Start discord client
client = discord.Client()

#Fetch env variables
TOKEN = os.environ['DISCORD_BOT_KEY']
MY_USERID = os.environ['MY_DISCORD_ID']
DEV_KEY = os.environ['DEV_KEY']

#Start riot api
riotapi.set_region('na')
riotapi.set_api_key(DEV_KEY)

#Function that determines if the player entered is a support main.
def isSupport(summname, region):
    """Returns True if the summoner is a support main, False otherwise."""
    #initalize variables
    summoner = riotapi.get_summoner_by_name(summname)
    riotapi.set_region(region)
    match_history = riotapi.get_match_list(summoner, 5)
    counter = 0
    for match in match_history:
        if str(match.role) == 'Role.support':
            counter += 1
        if counter == 3:
            return True
    return False

def checkSupportList(userid):
    with open('supportmains.txt', 'r') as f:
        for line in f:
            if line[:-1] == userid:
                return True
    return False



@client.event
async def on_ready():
    print('logged in.')

@client.event
async def on_message(message):
    author = message.author #member (object)
    authorid = message.author.id #member id (string)
    content = message.content #content (string)
    #role_member = message.server.roles[3] #member role (object)
    if content.lower() == '!member':
        for role in message.server.roles:
            if role.name.lower() == 'member':
                role_member = role
        if checkSupportList(authorid):
            await client.add_roles(author, role_member)
            await client.send_message(message.channel, "You've been granted the role `member`.")
        else:
            await client.send_message(message.channel, "You're not on the list of support mains. Try the command `!checksupport <summoner name> <region>`")
    if content.lower().startswith('!checksupport'):
        summonerName = ' '.join(content.split()[1:-1])
        summonerRegion = content.split()[-1]
        if checkSupportList(authorid):
            await client.send_message(message.channel, "You're already on the list of support mains.")
        elif isSupport(summonerName, summonerRegion):
            with open('supportmains.txt', 'a') as f:
                f.write(authorid + '\n')
            await client.send_message(message.channel, "You've been added to the list of support mains.")
        else:
            await client.send_message(message.channel, summonerName + ' does not meet our criteria of beibg a support main.')
    if content.lower() == '!help':
        helpmessage = "`Sorry, this command is currently in development. Check back another time!`"
        await client.send_message(author, helpmessage)
    #kill bot if i say so
    if (content.lower() == '!kill') & (authorid == MY_USERID):
        await client.delete_message(message)
        await client.logout()

@client.event
async def on_member_join(member):
    message = "Welcome to the support mains discord server! Type `!checksupport <summoner name> <region>` in general chat to add yourself to the list of supportmains, then `!member` to be promoted to member and gain access to the rest of the server."
    await client.send_message(member, message)

print('logging in')
client.run(TOKEN)

import discord, os
client = discord.Client()

TOKEN = os.environ['DISCORD_BOT_KEY']
MY_USERID = os.environ['MY_DISCORD_ID']

@client.event
async def on_ready():
    print('logged in.')

@client.event
async def on_message(message):
    author = message.author #member (object)
    authorid = message.author.id #member id (string)
    content = message.content #content (string)
    role_member = message.server.roles[3] #member role (object)
    if content.lower() == '!member':
        await client.add_roles(author, role_member)
        await client.delete_message(message)
    #kill bot if i say so
    if (content.lower() == '!kill') & (authorid == MY_USERID):
        await client.delete_message(message)
        await client.logout()

@client.event
async def on_member_join(member):
    message = "Welcome to the support mains discord server! Type '!member' in general chat to be able to type in other text channels."
    await client.send_message(member, message)
        
print('logging in')
client.run(TOKEN)

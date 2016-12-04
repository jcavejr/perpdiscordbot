# perpdiscordbot
Bot created by jcavejr in python3.5 utilizing the discord.py library and the cassiopeia library. Bot is meant to add users to a member role if they are a support main in league of legends.



<strong>Current functionality:</strong>

  Command '!member' promotes user to a member.
  
  Command '!kill' kills the bot, is only usable by the owner of the bot.
  
  Anytime a new user enters the server, a message is sent to them from the bot with instructions on how to become a member.
  
  
  
<strong>Instructions:</strong>

  First you have to make a discord bot account. Google it if you don't know how.
  
  Once you have your bot account created, make sure the user account has 'Manage Server' permissions on the server you want the bot to join.
  
  Then, navigate to https://discordapp.com/oauth2/authorize?client_id=CLIENT_ID&scope=bot&permissions=0
  
    (Make sure to replace 'CLIENT_ID' with your bot's client id.)
    
  Create a riot dev account, google it.
  
  Next you'll have to create environment variables holding your bot token, riot api dev code, and your user discord id:
  
    If you're on Windows or Mac, google it. If you're on linux, do the following:
    
      Open terminal and enter 'vim ~/.bashrc'
      
      Go all the way to the bottom of the file, press 'i', and create the following 3 lines:
      
        export RIOT_DEV_KEY='yourdevkeyhere'
        
        export DISCORD_BOT_KEY='yourbottokenhere'
        
        export MY_DISCORD_ID='yourdiscorduseridhere'
        
      Press 'Esc' and then type ':wq', hit 'enter'.
      
      For these changes to come into effect, in terminal type 'source ~/.bashrc' and then close terminal.
      
    Open terminal and type 'python3 -m pip install -U discord.py'. (Refer to https://github.com/Rapptz/discord.py).
    
    Open terminal again and type 'idle-python3.5'. Press file -> open file (find the file and open it). Press f5 and watch your bot run.
    
    Keep in mind your bot has to have ADMIN PERMISSIONS. Without admin permissions, your bot won't work. You'll just get errors.
    
    
    
<strong>Upcoming features:</strong>

  Command '!member (summoner name) (region)' will promote the user to member if the summoner is a support main. Further edits    will require the user to renamee a rune page to a random key provided by the bot to verify that the user is indeed the      entered summoner.

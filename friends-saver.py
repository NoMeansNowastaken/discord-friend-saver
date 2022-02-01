import discord, json, os
from discord.errors import LoginFailure
from discord.ext import commands, tasks


with open ('config.json') as UserData:
    file = json.load(UserData)

token = file.get('token')
prefix = file.get('prefix')

os.system('title Program')

client = commands.Bot(description = "Discord Friends-List Saver", command_prefix = prefix, self_bot = True)
client.remove_command('help')

# after login print username
@client.event
async def on_ready():
    print(f"Logged in as: {client.user.name}#{client.user.discriminator}")
    savefriends()


def savefriends():
    
    print("Getting Friends List...")
    with open('friends.txt','r+',encoding='utf-8') as f:
        for user in client.user.friends:
            f.write(f'{user.name}#{user.discriminator}\n')
    print("Done!")
    client.close()
    exit()


try:
    client.run(token, bot = False, reconnect = True)
except LoginFailure or discord.errors.Forbidden or discord.errors.HTTPException:
    print("Improper Token Has Been Passed Please Check CFG File.")

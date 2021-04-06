import discord, json, ctypes
from discord.errors import LoginFailure
from discord.ext import commands, tasks


with open ('config.json') as UserData:
    file = json.load(UserData)

token = file.get('token')
prefix = file.get('prefix')

ctypes.windll.kernel32.SetConsoleTitleW('Back Up Your Discord FriendsList')

client = commands.Bot(description = "Discord Friends-List Saver", command_prefix = prefix, self_bot = True)
client.remove_command('help')

print("The command(s) To Save Your Friends Are: friends, savefriend, friendslist, friend, savelist, savefriends.\n")

@client.command(aliases=['friends','savefriend','friendslist','friend','savelist'])
async def savefriends(ctx):
    await ctx.message.delete()

    flist = open('list.txt','r+',encoding='utf-8')

    print("Getting Friends List...\n")
    for user in client.user.friends:
        friends = user.name+'#'+user.discriminator
        flist.write(str(friends)+"\n")
    print('\n')
    print("Done!")


try:
    client.run(token, bot = False, reconnect = True)
except LoginFailure and discord.errors.Forbidden:
    print("Improper Token Has Been Passed Please Check CFG File.")
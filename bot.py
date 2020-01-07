#bot.py
import os
import discord
import random
from discord.ext import commands
from random import randrange
from discord.ext.commands import Bot
import asyncio

client = discord.Client() #Instance called client, connection to discord
bot = commands.Bot(command_prefix='$', description='')

from dotenv import load_dotenv #allows me to get token from .env

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready(): #on log in print msg
    print('We have logged in as {0.user}'.format(client))
    members = 'Members are:'
    global memberlist
    memberlist = []
    for guild in client.guilds:
        for member in guild.members:
            if member.bot == False:
                members = members + '\n' + member.name
                memberlist.append(member)
        print(f'Guild Members:\n - {members}')
        break

    owners = []
    for guild in client.guilds:
        owners.append(str(guild.owner))
    getowners("save", owners)

@client.event
async def on_message(message):
    #   Vibe Help
    if message.content.startswith('$vibehelp'):
        embed=discord.Embed(title="Vibe Check Bot", description="#The ultimate guide to VCB", color=0x0000a0)
        embed.set_author(name="@ahola", icon_url="https://discordemoji.com/assets/emoji/2446_cursed_flushed.png")
        embed.set_thumbnail(url="https://ih0.redbubble.net/image.966319411.8151/flat,128x128,075,t-pad,128x128,f8f8f8.jpg")
        embed.add_field(name="Check Online Users", value="```$vibecheckonline```", inline=True)
        embed.add_field(name="Vibe Check Anyone", value="```$vibecheckrandom```", inline=True)
        embed.add_field(name="Vibe Check @user", value="```$vibecheck @user```", inline=False)
        embed.add_field(name="Vibe Check Self", value="```$selfvibecheck```", inline=True)
        embed.add_field(name="Kick(Needs Perms)", value="```$vibekick```", inline=True)
        embed.add_field(name="Check Percent", value="```$vibecheckpercent```", inline=False)
        embed.set_footer(text="This bot is always under development. If you have any suggestions tells me :)")
        await message.channel.send(embed=embed)
    #   Random Vibe Check
    if message.content.startswith('$vibecheckrandom'):
        await vibecheck(random.choice(memberlist), message.channel, 1, message.author) #    1 = random vibe check
    #   Random Vibe Check Online
    if message.content.startswith('$vibecheckonline'):
        onlinememberlist=[]
        for guild in client.guilds:
            for member in guild.members:
                if member.status == discord.Status.online:
                    onlinememberlist.append(member)
        await vibecheck(random.choice(onlinememberlist), message.channel, 1, message.author) #    1 = random vibe check
    #   Self Vibe Check
    if message.content.startswith('$selfvibecheck'):
        await vibecheck(message.author, message.channel, 0, message.author)
    #   Normal Vibe Check
    if message.content.startswith('$vibecheck '):
        if len(message.mentions) == 0:
            await message.channel.send('> There was an error with your command. Make sure you mention a __**user**__ to vibe check.')
        elif len(message.mentions) != 0:
            vibe = randrange(2) #   0 = failed , 1 = passed
            member = str(message.mentions[0])
            if vibe == 0:
                global savedowners
                savedowners = getowners("get", 0)
                await message.channel.send("> " + str(member.name) + " failed the vibe check.")
                if str(message.mentions[0]) in savedowners:
                    await message.channel.send('> There was an error concerning permissions. If you are the server owner, its not going to work on you because you are of higher position than the bot. To sum it up, Youre fucking retarded. ')
                elif str(message.mentions[0]) not in savedowners:
                    await message.mentions[0].edit(nick="failed the vibe check")
                else:
                    await message.channel.send("Error")
            elif vibe == 1:
                await message.channel.send(">" + str(member.name) + " passed the vibe check.")
            else:
                await message.channel.send('> There was an error concerning the code. I apologize.')
        else:
            await message.channel.send('> There was an error concerning the code. I apologize.')
    #   Random Vibe Check Online
    if message.content.startswith('$vibecheckpercent'):
        if len(message.mentions) == 0:
            await message.channel.send('> There was an error with your command. Make sure you mention a __**user**__ to vibe check.')
        elif len(message.mentions) != 0:
            member = message.mentions[0]
            vibe = randrange(101) #   0 - 100 vibe percent
            await message.channel.send('> ' + str(member.name) + " is " + str(vibe) + "% vibin.")
        else:
            await message.channel.send('> There was an error concerning the code. I apologize.')
    if message.content.startswith('$vibekick'):
        author = message.author
        if author.guild_permissions.kick_members:
            member = message.mentions[0]
            if member.status == discord.Status.online:
                vibe = randrange(2) #0 = failed , 1 =
                if vibe == 0:
                    savedowners = getowners("get", 0)
                    await message.channel.send("> " + str(member.name) + " failed the vibe check.")
                    if str(member) in savedowners:
                        await message.channel.send('> There was an error concerning permissions. If you are a server owner or administrator, its not going to work on you because you are of higher position than the bot. To sum it up, we cannot change your nickname, but you still failed the vibecheck :) How does it feel escaping death? ')
                    elif str(member) not in savedowners:
                        await member.edit(nick="failed the vibe check")
                        await member.kick(reason="none")
                    else:
                        await channel.send("> Error")
                elif vibe == 1:
                    await message.channel.send("> " + str(member.name) + " passed the vibe check.")
                else:
                    await message.channel.send('>' + 'There was an error concerning the code. I apologize.')
            else:
                await message.channel.send(">" + " We tried to vibe check " + str(member.name) + ". Unfortunately, " + str(member.name) + " is not online. Try again when there are more users online.")
        else:
            await message.channel.send("You are not an admin.")
#           functions
def getowners(action, owners):
    global savedowners
    if action == "save":
        savedowners = owners.copy()
        print(f'Guild Members:\n - {savedowners}')
    elif action == "get":
        return savedowners
    else:
        return
async def vibecheck(member, channel, random, author):
    memberid = member.id
    authorid = author.id
    if random == 1:
        randomtxt = "<@!" + str(authorid) + ">" + " initiated a random vibe check."
    else: randomtxt = ""
    if member.status == discord.Status.online:
        vibe = randrange(2) #0 = failed , 1 = passed
        if vibe == 0:
            savedowners = getowners("get", 0)
            await channel.send(" " + randomtxt + str(member.name) + " failed the vibe check.")
            if str(member) in savedowners:
                await channel.send('> There was an error concerning permissions. If you are a server owner or administrator, its not going to work on you because you are of higher position than the bot. To sum it up, we cannot change your nickname, but you still failed the vibecheck :) How does it feel escaping death? ')
            elif str(member) not in savedowners:
                await member.edit(nick="failed the vibe check")
            else:
                await channel.send("> Error")
        elif vibe == 1:
            await channel.send("> " + randomtxt + str(member.name) + " passed the vibe check.")
        else:
            await channel.send('>' + randomtxt + 'There was an error concerning the code. I apologize.')
    else:
        await channel.send(">" + randomtxt + " We tried to vibe check " + str(member.name) + ". Unfortunately, " + str(member.name) + " is not online. Try again when there are more users online.")

client.run(token)

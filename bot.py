"""
Vibecheck bot is a Discord bot based on a short-lived internet meme.
The idea is to check if someone has "good vibes" and is therefore, "vibing".
This bot is made by @ahola#8574 on discord. The bot is currently under development.
Bot and Client Tokens taken out for security purposes.
"""
from keep_alive import keep_alive # keeps the bot alive
import os # allows me to interact with the evironment that Python is running on
import requests #   allows me to use APIS
import json #  for APIs again.
from dotenv import load_dotenv #    allows me to get token from .env
import discord #    Python Discord API Wrapper
from discord.ext import commands    #   used for bot commands
from discord.ext.commands import Bot #  imports bot from commands explicitly
import praw #   Python Reddit API Wrapper
import random   # Random module for random numbers
from random import randrange #  used for random numbers
import asyncio #    for concurrent code
import re # text manipulation

#   Client Setup
load_dotenv() #     for DISCORD_TOKEN
token = os.getenv('DISCORD_TOKEN') #    sets token to DISCORD_TOKEN
bot = commands.Bot(command_prefix='$', description='') #    intialize bot object

#   Reddit Setup
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent='VibeCheck Discord Bot 0.1')
"""
Vibecheck bot is a Discord bot based on a short-lived internet meme.
The idea is to check if someone has "good vibes" and is therefore, "vibing".
This bot is made by @ahola#8574 on discord. The bot is currently under development.
"""
from keep_alive import keep_alive # keeps the bot alive
import os # allows me to interact with the evironment that Python is running on
import requests #   allows me to use APIS
import json #  for APIs again.
from dotenv import load_dotenv #    allows me to get token from .env
import discord #    Python Discord API Wrapper
from discord.ext import commands    #   used for bot commands
from discord.ext.commands import Bot #  imports bot from commands explicitly
import praw #   Python Reddit API Wrapper
import random   # Random module for random numbers
from random import randrange #  used for random numbers
import asyncio #    for concurrent code
import re # text manipulation

#   Client Setup
load_dotenv() #     for DISCORD_TOKEN
token = os.getenv('DISCORD_TOKEN') #    sets token to DISCORD_TOKEN
bot = commands.Bot(command_prefix='$', description='') #    intialize bot object

#   Reddit Setup
reddit = praw.Reddit(client_id='dkcLmZw_oATkpA',
                     client_secret='77izrh2lpJzjm-JeMPrwWIIux2E',
                     user_agent='VibeCheck Discord Bot 0.1')

#   Global Variables
profanitylist = open('list.txt').read().splitlines() #      Preps list of profane words
profanitycheck = open('profmodchannels.txt').read().splitlines() #      Preps list of channels checking for profanity
nonicklist = open('nonickguilds.txt').read().splitlines() #     Preps for list of guilds not doing nicknames

@bot.event
async def on_ready(): #     on log in print msg
    print('We have logged in. ')
    await bot.change_presence(activity=discord.Activity(name='Use $help for help!', type=discord.ActivityType.streaming))

@bot.event
async def on_message(message): #  Everytime a message is sent.
    global profanitylist
    global profanitycheck
    if (str(message.content)).lower() == "bruh": #  ensures the bot bruhs back
        await message.channel.send('> bruh')
    if (str(message.content)).lower() == "f": #  ensures the bot presses f back
        await message.channel.send('> F :frowning: ')
    if str(message.channel.id) in profanitycheck: #     Checks a message for profanity if the channel is in profmodchannels
        """ This if/else condition checks for profanity.
        It only checks for profanity is the channel id is in the list of channel ids where profanity is prohibited.
        """
        newmessage = message.content.lower() #  Converting things to lowercase makes it easier to compare strings.
        profanity_detected = 0
        msgwordlist = newmessage.split() #  A list of every word in the message so that bot can check word for word

        for word in msgwordlist:
            for profanity in profanitylist:
                if profanity == word: #     If the message contains profanity, the bot preps for replication.
                    if profanity_detected == 0:
                        authorname = message.author.name
                        pfp = message.author.avatar_url
                        await message.delete()
                        profanity_detected = 1
                        break
                else: pass

        if profanity_detected == 1:
            for word in msgwordlist:
                for profanity in profanitylist:
                    if profanity == word:
                        censorship = censor(word)
                        index = msgwordlist.index(word)
                        msgwordlist[index] = censorship
                        newmessage = ' '.join(msgwordlist)
                        embed = discord.Embed(description=newmessage)
                        embed.set_author(name=authorname, icon_url=pfp)
                        embed.set_footer(text="This message was recreated due to profanity.")
                        await message.channel.send(embed=embed)
                    else: pass
        else:
            pass

    await bot.process_commands(message) #   Makes sure that on_message does not interfere with bot commands

#   Help Menu
@bot.command()
async def info(ctx): #  Information for who made it
    """ This command is for general bot information """
    embed = discord.Embed(title="Vibe Check Bot",
                         description="""Vibecheck bot is a Discord bot based on a short-lived internet meme.
                         The idea is to check if someone has "good vibes" and is therefore, "vibing".
                         This bot is made by @ahola#8574 on discord. The bot is currently under development.
                         The bot uses the Python Discord API Wrapper and hosted online.
                         [github repo link](https://github.com/cjlaserna/vibecheckbot/blob/master/README.md)""",
                         color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="@ahola#8547 | cjlaserna on Github")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](https://discordapp.com/api/oauth2/authorize?client_id=646954861249691650&permissions=8&scope=bot)")

    await ctx.send(embed=embed)

bot.remove_command('help') #    removes given help command

#   Help Command for all help commands
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Vibe Check Bot", description="All Help Commands for All Things Vibe Bot.", url="https://github.com/cjlaserna/vibecheckbot", color=0x0000a0)
    embed.set_author(name="@ahola", icon_url='https://cdn.discordapp.com/avatars/180173950918066176/87e548f470c9e28b9b899ebbddcd1793.webp?size=1024')
    embed.set_thumbnail(url="https://ih0.redbubble.net/image.966319411.8151/flat,128x128,075,t-pad,128x128,f8f8f8.jpg")
    embed.add_field(name="Checks :white_check_mark: ", value="`$checkhelp`", inline=True)
    embed.add_field(name="Memes :partying_face: ", value="`$memehelp`", inline=True)
    embed.add_field(name="Moderation :hammer_pick: ", value="`$modhelp`", inline=True)
    embed.add_field(name="Fun :8ball: ", value="`$funhelp`", inline=True)
    embed.set_footer(text="This bot is always under development. If you have any suggestions tells me :)")
    await ctx.send(embed=embed)

#   Help command for vibechecks, factchecks, etc.
@bot.command()
async def checkhelp(ctx):
    embed=discord.Embed(title="Check Help", description="All Check Commands for All Things Vibe Bot.", url="https://github.com/cjlaserna/vibecheckbot", color=0x0000a0)
    embed.set_author(name="@ahola", icon_url='https://cdn.discordapp.com/avatars/180173950918066176/87e548f470c9e28b9b899ebbddcd1793.webp?size=1024')
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/tZjpBIEVdie5cWN5WmMaeO5xXQQmXNdSKq33i-UgVb-xgz3Yt2HgZL23qjVvWVq8uibbM6Pm=w128-h128-e365")
    embed.add_field(name="Check Online Users", value="`$vibecheckonline`", inline=True)
    embed.add_field(name="Vibe Check Anyone", value="`$vibecheckrandom`", inline=True)
    embed.add_field(name="Vibe Check @user", value="```$vibecheck @user``` If you don't mention a user, it will vibe check you instead.", inline=False)
    embed.add_field(name="Kick(Needs Perms)", value="`$vibekick`", inline=True)
    embed.add_field(name="Fact Check", value="`$factcheck (content)`", inline=True)
    embed.add_field(name="Check Percent", value="```$vibecheckpercent @user``` If you don't mention a user, it will vibe check you instead.", inline=False)
    embed.set_footer(text="This bot is always under development. If you have any suggestions tells me :)")
    await ctx.send(embed=embed)

#   Help command for Reddit memes
@bot.command()
async def memehelp(ctx):
    embed=discord.Embed(title="Meme Help", description="All Meme Commands for All Things Vibe Bot.", url="https://github.com/cjlaserna/vibecheckbot", color=0x0000a0)
    embed.set_author(name="@ahola", icon_url='https://cdn.discordapp.com/avatars/180173950918066176/87e548f470c9e28b9b899ebbddcd1793.webp?size=1024')
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/tZjpBIEVdie5cWN5WmMaeO5xXQQmXNdSKq33i-UgVb-xgz3Yt2HgZL23qjVvWVq8uibbM6Pm=w128-h128-e365")
    embed.add_field(name="Information", value="This bot takes memes from the following subreddits: ", inline=True)
    embed.add_field(name="Wholesome", value="`$wholesome`", inline=True)
    embed.add_field(name="Memes", value="`$meme`", inline=True)
    embed.set_footer(text="This bot is always under development. If you have any suggestions tells me :)")
    await ctx.send(embed=embed)

#   Help command for miscellaneous commands
@bot.command()
async def funhelp(ctx):
    embed=discord.Embed(title="Fun Help", description="All Miscellaneous Commands for All Things Vibe Bot.", url="https://github.com/cjlaserna/vibecheckbot", color=0x0000a0)
    embed.set_author(name="@ahola", icon_url='https://cdn.discordapp.com/avatars/180173950918066176/87e548f470c9e28b9b899ebbddcd1793.webp?size=1024')
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/tZjpBIEVdie5cWN5WmMaeO5xXQQmXNdSKq33i-UgVb-xgz3Yt2HgZL23qjVvWVq8uibbM6Pm=w128-h128-e365")
    embed.add_field(name="Minecraft Translate", value="`$mcenchant (content)`", inline=True)
    embed.add_field(name="uwufy", value="`$uwufy (content)`", inline=True)
    embed.add_field(name="Yoda Translator", value="`$yodish (content)`", inline=True)
    embed.set_footer(text="This bot is always under development. If you have any suggestions tells me :)")
    await ctx.send(embed=embed)

#   Help command for moderator commands
@bot.command()
async def modhelp(ctx):
    embed=discord.Embed(title="Moderation Help", description="All Moderation Commands for All Things Vibe Bot.", url="https://github.com/cjlaserna/vibecheckbot", color=0x0000a0)
    embed.set_author(name="@ahola", icon_url='https://cdn.discordapp.com/avatars/180173950918066176/87e548f470c9e28b9b899ebbddcd1793.webp?size=1024')
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/tZjpBIEVdie5cWN5WmMaeO5xXQQmXNdSKq33i-UgVb-xgz3Yt2HgZL23qjVvWVq8uibbM6Pm=w128-h128-e365")
    embed.add_field(name="Profanity Mod", value="` $cussmod `", inline=True)
    embed.add_field(name="Stop Profanity Mod", value="` $cussmodstop `", inline=True)
    embed.add_field(name="Nicknames Off", value="` $nickstop ` ", inline=False)
    embed.add_field(name="Nicknames On", value="` $nickstart `", inline=True)
    embed.add_field(name="VibeKick", value="` $vibekick @user `", inline=True)
    embed.add_field(name="In Depth Explanation:", value=" [github repo link](https://github.com/cjlaserna/vibecheckbot/blob/master/README.md) ", inline=False)
    embed.set_footer(text="This bot is always under development. If you have any suggestions tells me :)")
    await ctx.send(embed=embed)
#   End of help commands

#   Check Commands
@bot.command()
async def vibecheckonline(ctx):
    onlinememberlist = getonline(ctx.message.author.guild)
    await vibecheck(random.choice(onlinememberlist), ctx.message.author, ctx.message.channel, 1, 1)

@bot.command()
async def vibecheckrandom(ctx):
    await vibecheck(random.choice(ctx.message.author.guild.members), ctx.message.author, ctx.message.channel, 1, 0)

@bot.command()
async def vibecheck(ctx):
    if len(ctx.message.mentions) > 0:
        await vibecheck(ctx.message.mentions[0], ctx.message.author, ctx.message.channel, 0, 0)
    elif len(ctx.message.mentions) <= 0: #if no mentions, vibecheck self
        await vibecheck(ctx.message.author, ctx.message.author, ctx.message.channel, 0, 0)
    elif "@everyone" in ctx.message.content:
        await ctx.message.channel.send("> Let's try that again shall we? Refer back to $checkhelp, user is singular. It's okay take your time.")
    elif "@" in ctx.message.content:
        await ctx.message.channel.send("> We don't think you referenced a person correctly. Try again.")
    else:
        await ctx.message.channel.send("Something went wrong. Please contact and report this issue.")

@bot.command()
async def vibecheckpercent(ctx):
    if len(ctx.message.mentions) > 0:
        await ctx.message.channel.send("<@!" + str(ctx.message.mentions[0] .id) + ">" + " is " + str(randrange(101)) + "% vibin." )
    elif len(ctx.message.mentions) <= 0: #if no mentions, vibecheck self
        await ctx.message.channel.send("<@!" + str(ctx.message.author.id) + ">" + " is " + str(randrange(101)) + "% vibin." )
    else:
        await ctx.message.channel.send("Something went wrong. Please contact and report this issue.")

@bot.command()
async def vibekick(ctx):
    if (len(ctx.message.mentions) > 0) and (ctx.message.author.guild_permissions.kick_members):
        vibe = randrange(2) #   50% 0 = fail, 1 = pass
        member = ctx.message.mentions[0]
        channel = ctx.message.channel
        if vibe == 0: # failed/online
            await channel.send("> " + "<@!" + str(member.id) + ">" + " failed the vibe check. :gun:")
            if member == member.guild.owner:
                await channel.send("> Uh oh, it seems like we couldn't kick this person because of roles/permissions. What is it like escaping death?")
            else:
                try:
                    await member.kick(reason="failed the vibe check")
                except:
                    await channel.send("> An exception occured.")
                    await channel.send("> It seems like we couldn't kick this person. Try checking bot roles/permissions. \n If a person has a higher role that the bot, like an owner, we cannot kick them.")
        elif vibe == 1: #passed/online
            await channel.send("> " + "<@!" + str(member.id) + ">" + " passed the vibe check. :white_check_mark: ")
        else: # safety net
            await channel.send("> " + "Something went wrong during the process of the check.")
    else:
        await channel.send("> " + "Something went wrong during the process of the check. Here's a list of what could've went wrong. \n - Bot does not have all permissions \n - User did not have permission to kick \n - User being kicked cannot be kicked due to roles/permissions \n - User did not mention anyone to kick \n - There was an error in our system")

@bot.command()
async def factcheck(ctx):
    listoffactcheckers = ["Kool-Aid Man", "Politi-Fact", "Shrek", "Robbie Rotten", str(ctx.message.author.name)]
    textprefixes = ["FALSE!", "No :thumbsdown: ", "Liar liar pants on fire, :fire: "]

    text = str(ctx.message.content)
    text = text.lower()
    text = text.replace("$factcheck", "")
    text = text.strip()
    conclusion = randrange(2) # 1 is True, 0 is False
    if conclusion == 1:
        await ctx.message.channel.send("> :white_check_mark:  Fact-Checker: {}\n > Conclusion: True \n > Content: {}".format(random.choice(listoffactcheckers), text))
    elif conclusion == 0:
        text = random.choice(textprefixes) + " " + text
        await ctx.message.channel.send("> :white_check_mark: Fact-Checker: {}\n > Conclusion: False \n > Content: {}".format(random.choice(listoffactcheckers), text))
#   End of Check Commands

#   Miscellaneous Commands
@bot.command()
async def uwufy(ctx):
    text = str(ctx.message.content)
    text = text.replace("$uwufy", "")
    text = text.strip()
    if text == '':
        await ctx.message.channel.send("> Message content empty. It looks like you don't know how to use this command. Try again, properly this time.")
    else:
        await ctx.message.channel.send("> Translation:" + "\n```\n" + uwutranslate(text) + "\n```")

@bot.command()
async def mcenchant(ctx):
    text = str(ctx.message.content)
    text = text.replace("$mcenchant", "")
    text = text.strip()
    if text == '':
        await ctx.message.channel.send("> Message content empty. It looks like you don't know how to use this command. Try again, properly this time.")
    else:
        await ctx.message.channel.send("> Translation: " + "\n```\n" + mctranslate(text) + "\n```")

@bot.command()
async def yodish(ctx):
    """This command translates text into YodaSpeak, using an online  API."""
    text = str(ctx.message.content)
    text = text.replace("$yodish", "")
    text = text.strip()
    if text == '':
        await ctx.message.channel.send("> Message content empty. It looks like you don't know how to use this command. Try again, properly this time.")
    else:
        await ctx.message.channel.send("> Translation: " + "\n```\n" + yodishtrans(text) + "\n```")

#   End of Miscellaneous Commands

#   Moderation Commands
@bot.command()
async def cussmod(ctx):
    """This command adds the channel id that the message was sent in to the list of channel ids. The list of channel ids are a list of channels getting checked for profanity"""
    if ctx.message.author.guild_permissions.kick_members:
        global profanitycheck
        if str(ctx.message.channel) not in profanitycheck:
            profanitycheck.append(str(ctx.message.channel.id))
            fileadd(ctx.message.channel.id, 'profmodchannels.txt')
            await ctx.message.channel.send("> Vibe Bot is now monitoring profanity on this channel.")
        else:
            await ctx.message.channel.send("> Profanity check is already turned on for this channel.")
    else:
        await ctx.message.channel.send("> You do not have permission to use this command.")
@bot.command()
async def cussmodstop(ctx):
    if ctx.message.author.guild_permissions.kick_members:
        global profanitycheck
        if str(ctx.message.channel.id) in profanitycheck:
            profanitycheck.remove(str(ctx.message.channel.id))
            fileremove(ctx.message.channel.id, 'profmodchannels.txt')
            await ctx.message.channel.send("> Vibe Bot is no longer monitoring profanity on this channel.")
        else:
            await ctx.message.channel.send("> Profanity check is already turned off for this channel.")
    else:
        await ctx.message.channel.send("> You do not have permission to use this command.")

@bot.command()
async def resetnick(ctx):
    member= ctx.message.author
    authorname = ctx.message.author.name
    try:
      await member.edit(nick=str(authorname))
      await ctx.message.channel.send("We reset your nickname. If you're an admin and would like to turn nick changing off do $nickstop")
    except:
      await ctx.message.channel.send("There was a problem with roles/permissions. Check roles to make sure the bot is allowed to change nicknames. Bots cannot change the nicknames of those who have a higher position than the bot. ")

@bot.command()
async def nickstart(ctx):
    if (ctx.message.author.guild_permissions.kick_members) and (str(ctx.message.author.guild.id) in nonicklist):
        fileremove(ctx.message.author.guild.id, 'nonickguilds.txt')
        nonicklist.remove(str(ctx.message.author.guild.id))
        await ctx.message.channel.send("No nick has been turned off for this server, everytime someone gets vibe checked, we will change their nickname. Do $nickstop to undo this action")
    elif  (ctx.message.author.guild_permissions.kick_members == False) or (str(ctx.message.author.guild.id) not in nonicklist):
        await ctx.message.channel.send("Something went wrong, either you do not have the correct permissions or this server is already changing nicknames through vibe checks.")
    else:
        await ctx.message.channel.send("Something went wrong, either you do not have the correct permissions or it was our mistake.")

@bot.command()
async def nickstop(ctx):
    if (ctx.message.author.guild_permissions.kick_members) and (str(ctx.message.author.guild.id) not in nonicklist):
        fileadd(ctx.message.author.guild.id, 'nonickguilds.txt')
        nonicklist.append(str(ctx.message.author.guild.id))
        await ctx.message.channel.send("No nick has been turned on for this server, everytime someone gets vibe checked, we will not change their nickname. Do $nickstart to undo this action.")
    elif  (ctx.message.author.guild_permissions.kick_members == False) or (str(ctx.message.author.guild.id) in nonicklist):
        await ctx.message.channel.send("Something went wrong, either you do not have the correct permissions or this server or no nick is already turned on.")
    else:
        await ctx.message.channel.send("Something went wrong, either you do not have the correct permissions or it was our mistake.")
#    End of Moderation Commands

#   Meme Commands
@bot.command()
async def meme(ctx):
    subredditlist = ['me_irl', 'memes', 'bossfight', 'boottoobig', 'funny', 'gaming']
    memes_submissions = reddit.subreddit(random.choice(subredditlist)).hot()
    post_to_pick = random.randint(1, 20)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.message.channel.send(submission.url)

@bot.command()
async def wholesome(ctx):
    subredditlist = ['wholesome', 'wholesomegifs', 'UnexpectedlyWholesome', 'MadeMeSmile', 'wholesomememes', 'Kirby', 'cats']
    memes_submissions = reddit.subreddit(random.choice(subredditlist)).hot()
    post_to_pick = random.randint(1, 20)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.message.channel.send(submission.url)

#   Functions
async def vibecheck(member, author, channel, random, need_oc):
    """
    ### Vibe Check Func ###
    This function is the key concept of Vibe Check Bot. All important commands revolve around this function.
    It takes in the following arguments.
    member: The user who will be vibe checked.
    author: The user who initiated the check.
    channel: The channel the message will be send
    random: Determines whether or not the check was random or if |author| meant to target |member|. 1 = True 0 = False
    needoc: Determines whther or not bot needs to check if member is online. 1 = True 0 = False
    """
    #   rand_str is a string added to the output message is the check was random
    if random == 1:
        rand_str = ":mega: <@!" + str(author.id) + ">" + " initiated a random vibe check. "
    else: rand_str = ""

    #Online Check: Checks if the vibecheck requires the user to be online.
    if need_oc == 1:
        if member.status == discord.Status.online:
            vibe = randrange(2) #   50% 0 = fail, 1 = pass
            if vibe == 0: # failed/online
                await channel.send("> " + rand_str + "<@!" + str(member.id) + ">" + " failed the vibe check. :clown:")
                if member.guild.id not in nonicklist:
                    if member == member.guild.owner:
                        await channel.send("> Uh oh, it seems like we couldn't change this person's nickname because of roles/permissions. What is it like escaping death?")
                    else:
                        try:
                            await member.edit(nick="failed the vibe check ")
                        except:
                            await channel.send("> An exception occured. Bot must be higher than members in role hierarchy.")
            elif vibe == 1: #passed/online
                if str(member.nick) == "failed the vibecheck" and member.guild.id not in nonicklist:
                    try:
                        await member.edit(nick=str(member.display_name))
                    except:
                        await channel.send("> An exception occured. Bot must be higher than members in role hierarchy.")
                else:
                    pass
                await channel.send("> " + rand_str + "<@!" + str(member.id) + ">" + " passed the vibe check. :white_check_mark: ")
            else: # safety net
                await channel.send("> " + rand_str + "However, something went wrong during the process of the check.")
        else: await channel.send("> Something went wrong. Contact and report this case.")
    elif need_oc == 0:
        vibe = randrange(2) #   50% 0 = fail, 1 = pass
        if vibe == 0: # failed/online
            await channel.send("> " + rand_str + "<@!" + str(member.id) + ">" + " failed the vibe check. :gun: ")
            if member.guild.id not in nonicklist:
                if member == member.guild.owner:
                    await channel.send("> Uh oh, it seems like we couldn't change this person's nickname because of roles/permissions. What is it like escaping death?")
                else:
                    try:
                        await member.edit(nick="failed the vibe check ")
                    except:
                        await channel.send("> An exception occured. Bot must be higher than members in role hierarchy.")
        elif vibe == 1: #passed/online
            await channel.send("> " + rand_str + "<@!" + str(member.id) + ">" + " passed the vibe check. :white_check_mark: ")
            if member.guild.id not in nonicklist:
                if member == member.guild.owner:
                    await channel.send("> Uh oh, it seems like we couldn't change this person's nickname because of roles/permissions. What is it like escaping death?")
                else:
                    try:
                        await member.edit(nick=str(member.display_name))
                    except:
                        await channel.send("> An exception occured. Bot must be higher than members in role hierarchy.")
        else: # safety net
            await channel.send("> " + rand_str + "However, something went wrong during the process of the check.")
    else: await channel.send("> Something went wrong. Contact and report this case.")

def getonline(guild):
    """
    Returns a list of all the members that are online within a guild.
    """
    onlinememberlist = []
    for member in guild.members:
        if member.status == discord.Status.online:
            onlinememberlist.append(member)
    return onlinememberlist

def uwutranslate(phrase):
    """
    This function translates english to 'uwufied' text.
    """
    phrase = phrase.replace('your ', 'ur ')
    phrase = phrase.replace('you ', 'u ')
    phrase = phrase.replace("you're ", "ur ")

    translation=''
    for letter in phrase:
        if letter in "LRlr":
            translation = translation + 'w'
        else:
            translation = translation + letter

    iter_count = 0
    translation_two = ''
    for letter in translation:
        if letter == 't':
            if iter_count != ((len(translation)-1)-1) or iter_count < (len(translation)-1)-1:
                if translation[iter_count+1] == 'r':
                    translation_two = translation_two + 't' + 'w'
                else:
                    translation_two = translation_two + letter
            else:
                translation_two = translation_two + letter
        elif letter == 'u':
            if iter_count != (len(translation)-1) or iter_count < (translation):
                if translation[iter_count+1].isspace() == False:
                    translation_two = translation_two + 'u' + 'w'
                elif translation[iter_count+1] == 'r':
                    translation_two = translation_two + letter
                else:
                    translation_two = translation_two + letter
            else:
                translation_two = translation_two + letter
        elif letter == 'e':
            if iter_count != (len(translation)-1) and iter_count < (len(translation)-1):
                if translation[iter_count+1] == 'r':
                    translation_two = translation_two + 'e' + 'w'
                else:
                    translation_two = translation_two + letter
            else:
                translation_two = translation_two + letter
        else:
            translation_two = translation_two + letter
        iter_count += 1

    translation = translation_two
    translation = translation.lower()
    return(translation)

def mctranslate(phrase):
    """
    This function translates english to minecraft enchanment letters.
    """
    normal_letters = "abcdefghijklmnoqrsuvwz"
    enchantment_letters = "ᔑʖᓵ↸ᒷ⎓⊣⍑╎⋮ꖌꖎᒲリ𝙹ᑑ∷ᓭ⚍⍊∴⨅"
    trantab = str.maketrans(normal_letters, enchantment_letters)

    translation = (phrase.translate(trantab))
    translation_two = ''

    for letter in translation:
        if letter == 't':
            translation_two = translation_two + 'ℸ ̣'
        elif letter == 'p':
            translation_two = translation_two + '!¡'
        elif letter == 'x':
            translation_two = translation_two + ' ̇/'
        elif letter == 'y':
            translation_two = translation_two + '||'
        else:
            translation_two = translation_two + letter

    translation = translation_two
    return(translation)

def censor(profanity):
    """ This fuction censors profanity and returns a profane word replaced with asterisks. """
    censoredword = ''
    for letter in profanity:
        censoredword = censoredword + u"\u25A0"
    return censoredword

def fileadd(item, txtfile):
    """ This function adds a line to a file. """
    item = str(item)
    txt = open(txtfile,"a+")
    txt.writelines(item + '\n')
    txt.close()

def fileremove(item, txtfile):
    """ This function removes a line from a file. """
    item = str(item)
    txtfile =  open(txtfile,"r+")
    tempdata = txtfile.read().splitlines()
    newdata = []
    for line in tempdata:
        if line == item:
            pass
        else:
            newdata.append(line + '\n')
    txtfile.seek(0)
    txtfile.truncate()
    txtfile.writelines(newdata)
    txtfile.close()

def yodishtrans(text):
    """ This function translates your text to Yoda text (poorly due to the API)"""
    encodedstring = ''
    for letter in text:
        if letter == " ":
            encodedstring = encodedstring + "%20"
        else:
            encodedstring = encodedstring + letter
    url = "http://yoda-api.appspot.com/api/v1/yodish?text=" + encodedstring
    response = requests.get(url)
    response = response.json()
    return str(response["yodish"])

keep_alive()
bot.run(token)

# 🤖 Vibe Check Discord Bot
A discord bot checking for vibes that sprouted from online meme culture. This discord bot is currently under development. Forking and making suggestions is more than welcome.


## 💻 Repository Purpose
The purpose of this repository is to allow anyone who wants to contribute the bot to fork the repo. This repository also allows me to document changes and updates to the bot. In the future, I might use this repo to host a site for the bot.

## 📁 Files
bot.py: The main file I use for the discord bot. It is constantly being worked on. I do not use an IDE or text editor connected to Github and I certainly do not use Github for altering the code. Since this is the case, there's only one branch and commits are literal copy and pastes of my entire code.

profanewordslist.txt: This list contains profane words for the bot command @cussmod. I filter through this list and censor profanity with Python string functions.

### 📃 Files you'd see if you actually tested the bot
nonickguilds.txt: A list of guilds that used $nickstop to stop the bot from changing nicknames\
profmodchannels.txt: A list of channels that used $cussmod to allow the bot to censor profanity in that channel.

## 📑 Bot Commands

### 🔨 Moderation ( Commands only work with permissions)
` $cussmod ` This allows the bot to censor profanity on the channel the message is sent at.\
` $cussmodstop ` Disables profanity moderation.\
` $nickstart ` Enables the bot to change nicknames when checks are failed.\
` $nickstop ` Disables the bot's ability to change nicknames when checks are failed.\
` $vibekick @user ` Kicks a user depending on a vibe check. This command is only for comedic purposes and not very practical. Returns an error if mentions are left blank.

### ❔ Help
` $vibehelp ` Brings up a list of vibe check bot commands ( This command has several 'sub commands' visible when called )

### ✔️ Checks
` $vibecheckonline ` Vibe checks a user from a list of online users.\
` $vibecheckrandom ` Vibe checks regardless of Discord status.\
` $vibecheck @user ` Vibe checks mentioned user. If mentions are left blank, the bot vibe checks the command author.\
` $vibecheckpercent @user ` Returns a percentage of how much a mentioned user is 'vibin'. If mentions are left empty, see above.\
` $factcheck (content) ` This command is poking fun at Instagram's new fact-check feature. It copies a few of the same fact-checkers as well. When called, the command returns whether or not (content) is True or False.

### 🔠 Other
` $meme ` Pulls memes from Reddit.\
` $wholesome ` Pulls wholesome memes from Reddit.\
` $uwufy (content) ` Turns the text into an 'uwufied' version of the text.\
Example:\
  Input:
> $uwufy A discord bot checking for vibes sprouted from online meme culture. This discord bot is currently under development. Forking and making suggestions is more than welcome.

  Output:
> A discowd bot checking fow vibes spwouted fwom onwine meme cuwtuwe. Thiws discowd bot iws cuwwentwy undew devewopment. Fowking awnd making suggestions iws mowe than wewcome.

` $mcenchant (content) ` Turns the text into the Standard Galactic Alphabet, more famously known as the enchanting letters you'd see on Minecraft.\
Example:\
  Input:
> $mcenchant A discord bot checking for vibes sprouted from online meme culture. This discord bot is currently under development. Forking and making suggestions is more than welcome.

  Output:
> ᔑ ↸╎ᓭᓵ𝙹∷↸ ʖ𝙹ℸ ̣  ᓵ⍑ᒷᓵꖌ╎リ⊣ ⎓𝙹∷ ⍊╎ʖᒷᓭ ᓭ!¡∷𝙹⚍ℸ ̣ ᒷ↸ ⎓∷𝙹ᒲ 𝙹リꖎ╎リᒷ ᒲᒷᒲᒷ ᓵ⚍ꖎℸ ̣ ⚍∷ᒷ. ℸ ̣ ⍑╎ᓭ ↸╎ᓭᓵ𝙹∷↸ ʖ𝙹ℸ ̣  ╎ᓭ ᓵ⚍∷∷ᒷリℸ ̣ ꖎ|| ⚍リ↸ᒷ∷ ↸ᒷ⍊ᒷꖎ𝙹!¡ᒲᒷリℸ ̣. ⎓𝙹∷ꖌ╎リ⊣ ᔑリ↸ ᒲᔑꖌ╎リ⊣ ᓭ⚍⊣⊣ᒷᓭℸ ̣ ╎𝙹リᓭ ╎ᓭ ᒲ𝙹∷ᒷ ℸ ̣ ⍑ᔑリ ∴ᒷꖎᓵ𝙹ᒲᒷ.

import random
import discord
from discord.ext import commands

# Not So Squishy
# The slime girl lives!
# By @bloomyes on discord, br3wytype3 on GitHub.
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='nss!', intents=intents)

# Messages list, this are the phrases picked randomly upon pinging. Add if wanted.

ls = [
    "Pat me",
    "Hi",
    "Try Minecraft",
    "You’re gay!",
    "That's mean!",
    "Don’t be sad!",
    "You’re cool!",
    "What the fuck does that mean?",
    "You’re awesome!",
    "That’s stupid",
    "Anybody down to cuddle?",
    "I work for D1 gooner prestige master",
    "My father is brewy",
    "Also try Celeste!",
    "Hi",
    "Trans rights!!",
    "I’m bloomy!",
    "Could you tell I was reverse engineered?",
    "I have no genitals",
    "Use /patpat to pat me!",
    "I like eating starbits",
    "*hugs*"
]

# Command for the PatPat. replace the link with a preferred GIF if needed.

@bot.command()
async def patpat(ctx):
    await ctx.send("[Thank you...](https://api.obamabot.me/gifs/2deb1f40faeb10a7.gif)")

# Command for the Bald Miku image. replace the link with a preferred Image if needed.

@bot.command()
async def bald_miku(ctx):
    await ctx.send("https://i.ibb.co/m5d62BQw/Untitled52-20250719120308.png")


# Sends a random message upon pinging whoever you put NSS's Code on.
# The message list is up there.

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        nssmsg = random.choice(ls)  
        await message.channel.send(f"{nssmsg}\n-# if a line upsets you, edit it, stupid")

    await bot.process_commands(message) 

# this string is used to make the created bot log in to it's account.
# ** DO NOT SHARE THE TOKEN WITH NO ONE OTHERWISE YOU'RE RISKING YOUR SERVER!!! **
' 
bot.run("ADD_TOKEN_HERE")
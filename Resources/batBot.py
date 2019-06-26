import discord
from discord.ext import commands

import sys, traceback


# Set cogs reference
initial_extensions = [
    "cogs.occasionalBeep",
    "cogs.messageResponse"
    ]


# Set "client" and get token from file.
client = commands.Bot(command_prefix="$")
token = open("DiscordBot\\resources\\token.txt","r").readline()


# Load cogs, print status to console for each cogload.
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
            print(extension, "loaded")
        except Exception as e:
            print(extension, "not loaded")


# When ready, print confirmation to console and set presence status.
@client.event
async def on_ready():
    print("We are logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Game("smart"))


# Connect to discord client.
client.run(token, bot=True, reconnect=True)
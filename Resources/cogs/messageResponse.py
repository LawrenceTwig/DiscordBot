import discord
from discord.ext import commands


class BeepCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


# Respond to predefined messages
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content.lower() == "cerebro":
            await message.channel.send("Magneto")
        if message.content.lower() == "rock and roll all night":
            await message.channel.send("Yes, {}.\nAnd part of every day!".format(message.author.name))
        if message.content.lower() == "how are you?":
            await message.channel.send("I am a bot\n\n*beep boop*")


def setup(bot):
    bot.add_cog(BeepCog(bot))
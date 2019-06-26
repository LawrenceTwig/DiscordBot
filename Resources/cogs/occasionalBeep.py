import discord
from discord.ext import commands
import random


# Initiate trigger variables.
beepCountdown = 0
beepTarget = random.randrange(250, 500)


class BeepCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


# Send a random message with randomized frequency:
# add len(message) for messages from users to count 
# target number is randomly selected within range.
# When count exceeds target number, send a random message and reset.
    @commands.Cog.listener()
    async def on_message(self, message):
        global beepCountdown
        global beepTarget
        possible_responses = [
            "I am a bot\n\n*beep boop*",
            "Beep\nBeep"
            ]
        if message.author == self.bot.user:
            return
        if message.content.isalnum():
            beepCountdown += len(str(message.content))
            print("count increased by", len(str(message.content)), 
            "count is", beepCountdown, "target is", beepTarget)
        if beepCountdown >= beepTarget:
            print("before: count:", beepCountdown, "\ntarget: ", beepTarget)
            await message.channel.send(random.choice(possible_responses)) 
            beepCountdown = 0
            beepTarget = random.randrange(250, 500)
            print("after: count:", beepCountdown, "\ntarget: ", beepTarget)

# consider delay (https://docs.python.org/3.7/library/asyncio-task.html?highlight=await)


def setup(bot):
    bot.add_cog(BeepCog(bot))
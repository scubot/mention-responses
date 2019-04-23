import os
import random

import discord
from discord.ext import commands


class Mention(commands.Cog):
    def __init__(self, bot):
        self.version = "2.0.0"
        self.bot = bot
        self.responses = self.get_responses()

    @staticmethod
    def get_responses():
        file_dir = os.path.dirname(__file__)
        try:
            with open((os.path.join(file_dir, 'responses.txt'))) as file:
                responses = [line.strip() for line in file]
                return responses
        except FileExistsError:
            print("[WARN] File not found in Mention module.")
            raise discord.ext.commands.ExtensionFailed

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user.mentioned_in(message):
            await message.channel.send(message.author.mention + " " + random.choice(self.responses))


def setup(bot):
    bot.add_cog(Mention(bot))
import discord
from modules.botModule import *
import random
import os

class Mention(BotModule):
    name = 'mention'

    description = 'Adds some response text to when the bot is mentioned'

    help_text = 'This module has no callable functions.'

    trigger_string = ''

    trigger_on_mention = True

    @staticmethod
    def get_responses():
        file_dir = os.path.dirname(__file__)
        try:
            with open(os.path.join(file_dir, 'responses.txt')) as file:
                responses = [line.strip() for line in file]
                return responses
        except FileNotFoundError:
            print("Responses not found. Please fix.")
            quit()

    def __init__(self):
        super().__init__()
        self.responses = self.get_responses()

    async def on_mention(self, message, client):
        if client.user.mentioned_in(message):
            msg = message.author.mention + " " + random.choice(self.responses)
            await client.send_message(message.channel, msg)
        else:
            return 0

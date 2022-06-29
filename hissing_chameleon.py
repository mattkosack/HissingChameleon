import os
import re
from dotenv import load_dotenv
import discord
import requests

client = discord.Client()
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # if message.content.startswith('$hello'):
    #     await message.channel.send('Hello!')

    # if any(word in message.content for word in ['Luke', 'luke']):
    if re.search(r"[Ll]+[\ \t\r\n]*[Uu]+[\ \t\r\n]*[Kk]+[\ \t\r\n]*[Ee]+[\ \t\r\n]*", message.content):
        await message.channel.send('I miss Luke :\\(')


client.run(token)

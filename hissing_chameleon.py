import os
import re
from dotenv import load_dotenv
import discord
import requests

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if re.search(r"[Ll][^ -~]*[Uu][^ -~]*[Kk][^ -~]*[Ee]", message.content):
        await message.channel.send('I miss Luke :\\(')

    if message.content.startswith('%name'):
        await message.channel.send('https://audio.pronouncekiwi.com/enNEW1/sukapon')

if __name__=="__main__":
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    client.run(token)

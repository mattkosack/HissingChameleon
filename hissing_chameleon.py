import os
import re
from dotenv import load_dotenv
import discord
from discord.ext import commands
from utils import get_line
import requests

bot = commands.Bot(command_prefix='%')


@bot.event
async def on_ready():
    print(f'We have logged in as {bot}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if re.search(r"[Ll][^ -~]*[Uu][^ -~]*[Kk][^ -~]*[Ee]", message.content):
        await message.channel.send('I miss Luke :\\(')


@bot.command(name="name", help="Says bot name")
async def name(ctx):
    # await message.channel.send('https://audio.pronouncekiwi.com/enNEW1/sukapon')
    embed = discord.Embed(
        title="Say my name", url="https://audio.pronouncekiwi.com/enNEW1/sukapon", description="Say it.")
    await ctx.channel.send(embed=embed)


@bot.command(name="frakes", help="asks you a question")
async def frakes(ctx):
    print('getting line')
    await ctx.channel.send(get_line('frakes.txt'))


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    bot.run(token)

import os
import re
from dotenv import load_dotenv
import discord
from discord.ext import commands
from utils import get_line
import requests
from PIL import Image
import random
import io

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
    await bot.process_commands(message)

@bot.command(name='test')
async def ping(ctx):
    await ctx.send('pong')

@bot.command(name="name", help="Says bot name")
async def name(ctx):
    # await message.channel.send('https://audio.pronouncekiwi.com/enNEW1/sukapon')
    embed = discord.Embed(
        title="Say my name", url="https://audio.pronouncekiwi.com/enNEW1/sukapon", description="Say it.")
    print('saying name')
    await ctx.channel.send(embed=embed)


@bot.command(name="frakes", help="asks you a question")
async def frakes(ctx):
    print('getting line')
    await ctx.channel.send(get_line('frakes.txt'))

@bot.command(name="color", help="Shows the color")
async def color(ctx, color=None):
    if color is None:
        color = random.choice(["red", "green", "blue"])
    img = Image.new("RGB", (256, 256), color)
    # buf = io.BytesIO()
    # img.save(buf, format="PNG")
    with BytesIO() as image_binary:
        img.save(image_binary, 'PNG')
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename='image.png')) 
    # await ctx.channel.send(discord.File(buf, "color.png"))

if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    bot.run(token)

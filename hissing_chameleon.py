import os
import re
from dotenv import load_dotenv
import discord
from discord.ext import commands
from utils import get_line, gen_from_pil, gen_from_xkcd, gen_from_rand
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
    if message.author.bot:
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

@bot.command(name="roll", help="rolls dice num d sides")
async def roll(ctx, dice: str):
    if not dice or not re.match(r"\d[dD]\d", dice):
        await ctx.channel.send(random.randint(1, 6))
    else:
        num, sides = dice.split('d')
        results = [random.randint(1, int(sides)) for _ in range(int(num))]
        await ctx.channel.send(results)

@bot.command(name="color", help="Shows the color")
async def color(ctx, color=None):
    # Not sure how to write this better, I know it's ugly.
    message = None
    if color is not None:
        img = gen_from_pil(color)
        if img is None:
            img = gen_from_xkcd(color)
            if img is None:
                message = 'Could not find color, here is a random one'
                img = gen_from_rand()
    else:
        img = gen_from_rand()

    with io.BytesIO() as image_binary:
        img.save(image_binary, 'PNG')
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename=f'{color}.png'), content=message)


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    bot.run(token)

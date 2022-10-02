import os
import re
from dotenv import load_dotenv
import discord
from discord.ext import commands
from utils import get_line, gen_from_pil, gen_from_xkcd, gen_from_rand, send_input, get_color_and_mode, rgb2hex, rgba2hex
import random
import io
import asyncio
import time


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="%", intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot}")


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.guild.id == 891496433881055272:
        return

    if re.search(r"[Ll][^ -~]*[Uu][^ -~]*[Kk][^ -~]*[Ee]", message.content):
        await message.channel.send("I miss Luke :sob:")
    await bot.process_commands(message)


@bot.command(name="ping", help="Test command")
async def ping(ctx):
    if ctx.message.author.bot:
        return
    await ctx.send("pong")


@bot.command(name="name", help="Says bot name")
async def name(ctx):
    if ctx.message.author.bot:
        return

    if ctx.message.author.voice is None:
        # url="https://audio.pronouncekiwi.com/enNEW1/sukapon" file="files/sukapon-sukapon.mp3"
        embed = discord.Embed(
            title="Say my name", url="https://audio.pronouncekiwi.com/enNEW1/sukapon", description="Say it.")
        await ctx.channel.send(embed=embed)
    else:
        # check if opus is installed
        # find_lib = ctypes.util.find_library('opus')
        # print(f"Find Opus: {find_lib}")
        # print("Loading Opus")
        # discord.opus.load_opus(find_lib)
        # print(f"Discord - Is loaded: {discord.opus.is_loaded()}")

        # TODO: Figure out a way to automatically find the file
        # discord.opus.load_opus('/opt/homebrew/Cellar/opus/1.3.1/lib/libopus.dylib')

        user_voice_channel = ctx.message.author.voice.channel
        voice_client = await user_voice_channel.connect()
        start = time.time()
        voice_client.play(discord.FFmpegPCMAudio(
            "https://audio.pronouncekiwi.com/enNEW1/sukapon"))
        while voice_client.is_playing():
            await asyncio.sleep(1)
        stop = time.time()
        print(f"Time: {stop-start}")
        await voice_client.disconnect()


@bot.command(name="leave", help="Makes the bot leave the voice channel")
async def leave(ctx):
    print("Disconnecting")
    await ctx.voice_client.disconnect()


@bot.command(name="frakes", help="asks you a question")
async def frakes(ctx):
    if ctx.message.author.bot:
        return

    print("getting line")
    await ctx.channel.send(get_line("files/frakes.txt"))


@bot.command(name="roll", help="rolls dice num d sides")
async def roll(ctx, dice=None):
    if ctx.message.author.bot:
        return

    if not dice or not re.match(r"\d+[dD]\d+", dice):
        await ctx.channel.send(random.randint(1, 6))
    else:
        num, sides = dice.split("d")
        results = [random.randint(1, int(sides)) for _ in range(int(num))]
        await ctx.channel.send(results)


@bot.command(name="color", help="Shows the color")
async def color(ctx, *, color=None):
    if ctx.message.author.bot:
        return

    # Not sure how to write this better, I know it's ugly.
    message = None
    mode = None
    if color is not None:
        print(f"Passed Color: {color}")
        color, mode = get_color_and_mode(color.strip())
        # TODO: Figure out how to retain HSV and other color modes
        if mode != "RGB" and mode != "RGBA":
            message = "Sorry, I can only show RGB and RGBA colors. Here's a random color."
            img, name = gen_from_rand()
        else:
            img, name = gen_from_pil(color, mode)
        if img is None:
            img = gen_from_xkcd(color)
            if img is None:
                message = "Could not find color, here is a random one"
                img, name = gen_from_rand()
    else:
        img, name = gen_from_rand()

    if mode == "RGB":
        r, g, b = color
        hex_name = rgb2hex(int(r), int(g), int(b))

    elif mode == "RGBA":
        r, g, b, a = color
        hex_name = rgba2hex(int(r), int(g), int(b), int(a))

    else:
        hex_name = name

    with io.BytesIO() as image_binary:
        img.save(image_binary, "PNG")
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename=f"{hex_name}.png"), content=message)


# @bot.command(name="game", help="Play the game")
async def game(ctx, command=None):
    if ctx.message.author.bot: 
        return

    if command is None:
        await ctx.channel.send("What do you want to do?")

    input_command = ""
    # TODO: change from match because raspberry pi is a pain in the ass to setup 
    # match command.strip().lower():
    #     case "up" | "u":
    #         input_command = "up"
    #     case "down" | "d":
    #         input_command = "down"
    #     case "left" | "l":
    #         input_command = "left"
    #     case "right" | "r":
    #         input_command = "right"
    #     case "a":
    #         input_command = "a"
    #     case "b":
    #         input_command = "b"
    #     case "start" | "st":
    #         input_command = "start"
    #     case "select" | "sel":
    #         input_command = "select"
    #     case _:
    #         await ctx.channel.send("Invalid command")

    if input_command != "":
        ip = os.getenv("IP")
        port = os.getenv("PORT")
        send_input(ip, port, input_command)


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    bot.run(token)

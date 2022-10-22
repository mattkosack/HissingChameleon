import os
import re
from dotenv import load_dotenv
import discord
from discord.ext import commands
from utils.utils import get_line, send_input, get_dict_from_csv, download_from_yt, shorten_clip, append_to_csv
from utils.utils_colors import gen_from_pil, gen_from_xkcd, gen_from_rand, get_color_and_mode, get_hex
import random
import io
import asyncio
from discord.ext import commands
from pretty_help import PrettyHelp

"""
TODO:
Refactor the help and documentation

TODO:
- Kalin clips
- Kalin quotes
- Schmaden
- Jinzo
- dasher on em
- kaiba funny
- I'm jack atlas
- paradox brothers joey clocks
- BLACK ROSE DRAGON
- kaiba show me the god card
- junk warrior poem (from two become one)
- yugi boy
- shadows and curtains
- Sayer duel, carly and jack married
- Jacky boi - dark signer carly
- sayer dying
- time to duel with a ghoul
- synchro what
- master of faster
- special sign
- piercing
- Yugioh poems
- riding duel
"""


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="%", intents=intents,
                   help_command=PrettyHelp())


@bot.event
async def on_ready():
    print(f"We have logged in as {bot}")


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if re.search(r"[Ll][^ -~]*[Uu][^ -~]*[Kk][^ -~]*[Ee]", message.content):
        if message.guild.id == 891496433881055272:
            return
        else:
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
    try:
        if ctx.message.author.voice is None:
            # url="https://audio.pronouncekiwi.com/enNEW1/sukapon" file="files/sukapon-sukapon.mp3"
            embed = discord.Embed(
                title="Say my name", url="https://audio.pronouncekiwi.com/enNEW1/sukapon", description="Say it.")
            await ctx.channel.send(embed=embed)
        else:
            play("sukapon", ctx)
    except Exception as e:
        print(e)


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
    # TODO:
    # Figure out how to retain HSV and other color modes
    # Find a better way to check color names (isinstance is kind of hacky here)
    # get hex if its a PIL supported color name
    if ctx.message.author.bot:
        return

    print(f"Passed Color: {color}")
    # Not sure how to write this better, I know it's ugly.
    message = None
    mode = None
    if color is not None:
        color, mode = get_color_and_mode(color.strip())
        if mode != "RGB" and mode != "RGBA":
            message = "Sorry, I can only show RGB and RGBA colors. Here's a random color."
            img, name = gen_from_rand()
        else:
            img, name = gen_from_pil(color, mode)

        if img is None:
            img, name = gen_from_xkcd(color)
            if img is None:
                message = "Could not find color, here is a random one"
                img, name = gen_from_rand()
    else:
        img, name = gen_from_rand()

    if isinstance(color, tuple):
        hex_name = get_hex(mode, color)
    else:
        hex_name = name

    with io.BytesIO() as image_binary:
        img.save(image_binary, "PNG")
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename=f"{hex_name}.png"), content=message)


@bot.command(name="play", help=f"Enter '%play <clip>' \nUse the %clips command to see a list of clips!")
async def play(ctx, clip=None):
    """
    Arguments:
        clip: The name of the clip to play
    """
    if ctx.message.author.bot:
        return

    user_voice_channel = ctx.message.author.voice.channel
    if user_voice_channel is None:
        await ctx.send("You are not in a voice channel")
        return

    clips = get_dict_from_csv('files/CLIPS.csv')

    file = "files/"
    if clip is not None:
        clip = clip.lower()
    if clip not in clips.keys() or clip is None:
        file += clips["sukapon"]
    else:
        file += clips[clip]
    try:
        voice_client = await user_voice_channel.connect()
        voice_client.play(discord.FFmpegPCMAudio(file))
        while voice_client.is_playing():
            await asyncio.sleep(1)
        await asyncio.sleep(1)
        await voice_client.disconnect()
    except Exception as e:
        print(e)


@bot.command(name="clips", help="Lists all the clips")
async def clips(ctx):
    if ctx.message.author.bot:
        return

    clips = get_dict_from_csv("files/CLIPS.csv")
    embed = discord.Embed(
        title="Clips", description="Here are all the clips I have")
    message = ""
    for i, key in enumerate(clips.keys()):
        if i == len(clips.keys()) - 1:
            message += key
        else:
            message += key + ", "
    embed.add_field(name="Names", value=message)
    await ctx.send(embed=embed)


@bot.command(name="add_clip")
async def add_clip(ctx, name, url, start, stop):
    """
    Adds a clip to the list of clips
    Arguments:
        name: Name of the clip
        url: URL of the clip
        start: Start time of the clip in HH:MM:SS format
        stop: Stop time of the clip in HH:MM:SS format
    """
    if ctx.message.author.bot:
        return

    if name in get_dict_from_csv("files/CLIPS.csv").keys():
        await ctx.send("Clip name already exists")
        return

    await ctx.send("Downloading clip. This step takes while.")
    try:
        download_from_yt(url, name)
    except Exception as e:
        print(e)
        await ctx.send("Error downloading clip")

    try:
        short_file = shorten_clip(name, start, stop)
    except Exception as e:
        print(e)
        await ctx.send("Error shortening clip")

    try:
        if short_file:
            append_to_csv("files/CLIPS.csv", name, short_file)
        else:
            await ctx.send("Error adding clip to list")
    except Exception as e:
        print(e)
        await ctx.send("Error adding clip to list")

    if name in get_dict_from_csv("files/CLIPS.csv").keys():
        await ctx.send("Clip added successfully")


##############################################################################################################
################################################# GAME INPUT #################################################
##############################################################################################################


# @bot.command(name="up", help="Press up in the game")
# async def up(ctx):
#     if ctx.message.author.bot:
#         return

#     send_input(GAME_IP, GAME_PORT, "up")


# @bot.command(name="down", help="Press down in the game")
# async def down(ctx):
#     if ctx.message.author.bot:
#         return

#     send_input(GAME_IP, GAME_PORT, "down")


# @bot.command(name="left", help="Press left in the game")
# async def left(ctx):
#     if ctx.message.author.bot:
#         return

#     send_input(GAME_IP, GAME_PORT, "left")


# @bot.command(name="right", help="Press right in the game")
# async def right(ctx):
#     if ctx.message.author.bot:
#         return

#     send_input(GAME_IP, GAME_PORT, "right")


# @bot.command(name="a", help="Press a in the game")
# async def a(ctx):
#     if ctx.message.author.bot:
#         return

#     send_input(GAME_IP, GAME_PORT, "a")


# @bot.command(name="b", help="Press b in the game")
# async def b(ctx):
#     if ctx.message.author.bot:
#         return

#     send_input(GAME_IP, GAME_PORT, "b")


# @bot.command(name="start", help="Press start in the game")
# async def start(ctx):
#     if ctx.message.author.bot:
#         return

#     send_input(GAME_IP, GAME_PORT, "start")


# @bot.command(name="select", help="Press select in the game")
# async def select(ctx):
#     if ctx.message.author.bot:
#         return

#     send_input(GAME_IP, GAME_PORT, "select")

##############################################################################################################
##############################################################################################################
##############################################################################################################


if __name__ == "__main__":
    load_dotenv()
    GAME_IP = os.getenv("IP")
    GAME_PORT = os.getenv("PORT")
    token = os.getenv("DISCORD_TOKEN")
    bot.run(token)

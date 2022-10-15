import os
import re
from dotenv import load_dotenv
import discord
from discord.ext import commands
from utils.utils import get_line, send_input
from utils.utils_colors import gen_from_pil, gen_from_xkcd, gen_from_rand, get_color_and_mode, get_hex
import random
import io
import asyncio

"""
TODO:
- Kalin clips
- Kalin quotes
- Schmaden
- Jinzo
- dasher on em
- kaiba funny
- I'm jack atlas
- SUPREME KING I CHALLENGE YOU
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

"""

CLIPS = {
    "how": "riddler_how.mp3",
    "peter": "peter.mp3",
    "hey": "hey.mp3",
    "sukapon": "sukapon.mp3",
    "what": "what.m4a",
    "dm": "DM.mp3",
    "dm-full": "DM-full.mp3",
    "gx": "GX.mp3",
    # "GX-full": "GX-full.mp3",
    "gx-jp": "GX-jp.mp3",
    "gx-jp-full": "GX-jp-full.mp3",
    "5ds": "5Ds.mp3",
    "hack": "kaiba-hack.mp3",
    "toon": "toon-theme.mp3",
    "ccapac-apu": "ccapac-apu.mp3",
    "beautiful1": "beautiful1.mp3",
    "beautiful2": "beautiful2.mp3",
    "ap": "ap.mp3",
    "booty": "booty.mp3",
    "chazzitup": "chazzitup.mp3",
    "challenge": "challenge.mp3"
}


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

    if ctx.message.author.voice is None:
        # url="https://audio.pronouncekiwi.com/enNEW1/sukapon" file="files/sukapon-sukapon.mp3"
        embed = discord.Embed(
            title="Say my name", url="https://audio.pronouncekiwi.com/enNEW1/sukapon", description="Say it.")
        await ctx.channel.send(embed=embed)
    else:
        play("sukapon", ctx)


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


@bot.command(name="play", help=f"Available clips: {', '.join(CLIPS.keys())}")
async def play(ctx, clip=None):
    if ctx.message.author.bot:
        return

    user_voice_channel = ctx.message.author.voice.channel
    if user_voice_channel is None:
        await ctx.send("You are not in a voice channel")
        return

    file = "files/"
    if clip is not None:
        clip = clip.lower()
    if clip not in CLIPS.keys() or clip is None:
        file += CLIPS["sukapon"]
    else:
        file += CLIPS[clip]

    voice_client = await user_voice_channel.connect()
    voice_client.play(discord.FFmpegPCMAudio(file))
    while voice_client.is_playing():
        await asyncio.sleep(1)
    await asyncio.sleep(1)
    await voice_client.disconnect()


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

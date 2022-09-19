import requests
import random
import re
from PIL import Image


def get_line(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    return random.choice(lines)


def gen_from_pil(phrase):
    """
    Generate an image from PIL defaults.
    """
    try:
        img = Image.new("RGB", (256, 256), phrase)
    except:
        return None
    return img


def gen_from_xkcd(phrase):
    """
    Generate an image from rgb.txt. (https://blog.xkcd.com/2010/05/03/color-survey-results/)
    Get the first color that matches the phrase.
    """
    with open('files/rgb.txt') as f:
        data = f.readlines()
        for line in data:
            desc = " ".join(line.split()[:-1])
            if phrase == desc:
                try:
                    img = Image.new("RGB", (256, 256), line.split()[-1])
                except:
                    return None
                return img


def gen_from_rand(phrase=None):
    """
    Generate an image from a random color.
    """
    print("Generating random color")
    return Image.new("RGB", (256, 256), "#%06x" % random.randint(0, 0xFFFFFF))

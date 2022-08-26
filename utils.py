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
    print("Using PIL defaults")
    return Image.new("RGB", (256, 256), phrase)

def gen_from_xkcd(phrase):
    """
    Generate an image from rgb.txt. (https://blog.xkcd.com/2010/05/03/color-survey-results/)
    Get the first color that matches the phrase.
    """
    with open('rgb.txt') as f:
        for line in f:
            line = f.readline()
            desc = " ".join(line.split()[:-1])
            if phrase == desc:
                print("Generating from XKCD")
                return Image.new("RGB", (256,256), line.split()[-1])


def gen_from_rand(phrase=None):
    """
    Generate an image from a random color.
    """
    print("Generating random color")
    return Image.new("RGB", (256,256), "#%06x" % random.randint(0, 0xFFFFFF))

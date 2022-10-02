import requests
import random
from PIL import Image
import ast

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def rgba2hex(r, g, b, a):
    return '#{:02x}{:02x}{:02x}{:02x}'.format(r, g, b, a)


def get_line(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    return random.choice(lines)


def get_color_and_mode(color):
    """
    Get the color and mode from the input.
    This could probably be done better.
    """
    # If it is a hex color and does not contain an alpha channel
    if len(color) == 7 and color[0] == "#":
        return color, "RGB"

    # If it is a hex color and contains an alpha channel
    if len(color) == 9 and color[0] == "#":
        return color, "RGBA"

    # If it contains these modes, need to evaluate it
    if "RGBA" in color.upper():
        mode = "RGBA"
    elif "RGB" in color.upper():
        mode = "RGB"
    elif "HSV" in color.upper():
        mode = "HSV"
    elif "LAB" in color.upper():
        mode = "LAB"
    else:
        mode = None

    if mode is None:
        return color, "RGB"
    else:
        color = ast.literal_eval(color.upper().replace(mode, ""))
        return color, mode


def gen_from_pil(phrase, mode):
    """
    Generate an image from PIL defaults.
    """
    try:
        img = Image.new(mode, (256, 256), phrase)
    except Exception as e:
        print(e)
        return None
    # TODO: color to hex
    # if mode == "RGB":
    #     r,g,b = img.load()[0,0]
    #     name = rgb2hex(r, g, b)
    # elif mode == "RGBA":
    #     r,g,b,a = img.load()[0,0]
    #     name = rgb2hex(r, g, b)
    return img, phrase


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
                except Exception as e:
                    print(e)
                    return None
                return img, line.split()[-1]
            return None, None


def gen_from_rand(phrase=None):
    """
    Generate an image from a random color.
    """
    print("Generating random color")
    choice = random.choice([0, 1])
    if choice == 0:
        mode = "RGB"
        name = "#%06x" % random.randint(0, 0xFFFFFF)
    else:
        mode = "RGBA"
        name = "#%08x" % random.randint(0, 0xFFFFFFFF)
    return Image.new(mode, (256, 256), name), name


def send_input(ip, port, data):
    url = f'http://{ip}:{port}/input'
    requests.post(url, data=data)

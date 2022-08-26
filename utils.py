import requests
import random
import re

def get_line(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    return random.choice(lines)

def get_color_from_text(phrase):
    """
    Get the first color that matches the phrase.
    TODO: The issue is this finds the first match, not the best match.
    """
    with open('rgb.txt') as f:
        for line in f:
            line = f.readline()
            desc = " ".join(line.split()[:-1])
            if phrase == desc:
                print(desc)
                return line.split()[-1]
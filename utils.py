import requests
import random

def get_line(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    return random.choice(lines)

def get_color_from_text(phrase):
    """Get the first color that matches the phrase"""
    with open('rgb.txt') as f:
        for line in f:
            line = f.readline()
            if phrase in line.split():
                return line.split()[-1]

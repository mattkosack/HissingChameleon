import requests
import random

def get_line(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    return random.choice(lines)


def send_input(ip, port, data):
    url = f'http://{ip}:{port}/input'
    requests.post(url, data=data)

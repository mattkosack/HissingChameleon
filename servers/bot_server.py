import requests
from dotenv import load_dotenv
import os

def send_input(ip, port, data):
    url = f'http://{ip}:{port}/input'
    requests.post(url, data=data)

if __name__ == '__main__':
    load_dotenv()
    ip = os.getenv('SERVER_IP')
    port = os.getenv('SERVER_PORT')
    data = {'input': 'start'}
    send_input(ip, port, data)

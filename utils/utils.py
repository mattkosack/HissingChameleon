import requests
import random
import csv
import youtube_dl
import os
import subprocess
# import ffmpeg


def get_line(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    return random.choice(lines)


def send_input(ip, port, data):
    url = f'http://{ip}:{port}/input'
    print(f"Sending {data} to: {url}")
    requests.post(url, data=data)


def get_dict_from_csv(filename):
    final_dict = {}
    with open(filename, 'r') as f:
        for line in csv.DictReader(f):
            final_dict[line['name']] = line['file']
    return final_dict


def append_to_csv(filename, name, file):
    with open(filename, 'a') as f:
        f.write(f'\n{name},{file}')


def download_from_yt(url, name):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'temporary_files/{name}_full.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'keepvideo': False,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def shorten_clip(name, start, stop):
    full_clip = f'temporary_files/{name}_full.mp3'
    short_clip = f'files/{name}.mp3'
    try:
        subprocess.call(['ffmpeg', '-i', full_clip, '-ss', start, '-to', stop, '-c', 'copy', short_clip])
    except Exception as e:
        print(e)
        return None

    os.remove(full_clip)
    return f'{name}.mp3'


import requests
import random
import csv
import os
import subprocess
import yt_dlp
# import ffmpeg
import logging

logging.basicConfig(filename='bot.log', encoding='utf-8', level=logging.ERROR)


def get_line(file_name):
    try:
        with open(file_name) as f:
            lines = f.readlines()
    except Exception as e:
        logging.error(e)
        return None
    return random.choice(lines)


def send_input(ip, port, data):
    url = f'http://{ip}:{port}/input'
    dict_data = {'input': data}
    requests.post(url, data=dict_data)


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
        'verbose': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        logging.error(e)
        return None


def shorten_clip(name, start, stop):
    full_clip = f'temporary_files/{name}_full.mp3'
    short_clip = f'files/{name}.mp3'
    try:
        subprocess.call(['ffmpeg', '-i', full_clip, '-ss', start, '-to', stop, '-c', 'copy', short_clip])
    except Exception as e:
        logging.error(e)
        os.remove(full_clip)
        return None

    os.remove(full_clip)
    return f'{name}.mp3'


def remove_name_from_csv(file_path, string_to_delete):
    with open(file_path, 'r') as file, open('temporary_files/temp.txt', 'w') as new_file:
        for line in file:
            # Line should exactly match this
            if f"{string_to_delete},{string_to_delete}.mp3\n" == line:
                continue
            new_file.write(line)
    file.close()
    new_file.close()

    os.replace('temporary_files/temp.txt', file_path)

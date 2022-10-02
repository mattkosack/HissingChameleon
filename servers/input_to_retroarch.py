from flask import Flask, request
from dotenv import load_dotenv
import os
from pyautogui import press, typewrite, hotkey

# press('a')
# typewrite('quick brown fox')
# hotkey('ctrl', 'w')


def create_server():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/input', methods=['POST'])
    def game_input():
        game_input = request.form['input']
        print('Recieved Input: ' + game_input)
        if game_input == 'up':
            press('up')
        elif game_input == 'down':
            press('down')
        elif game_input == 'left':
            press('left')
        elif game_input == 'right':
            press('right')
        elif game_input == 'a':
            press('a')
        elif game_input == 'b':
            press('b')
        elif game_input == 'start':
            press('enter')
        elif game_input == 'select':
            press('backspace')
        elif game_input == 'SAVE':
            press('f5')
        else:
            return 'Invalid Input'
        return 'OK'

    return app


if __name__ == '__main__':
    load_dotenv()
    server = create_server()
    server.run(host=os.getenv('SERVER_IP'), port=8080, debug=True)

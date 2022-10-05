from flask import Flask, request
from pyautogui import press

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
            press('u')
        elif game_input == 'down':
            press('d')
        elif game_input == 'left':
            press('l')
        elif game_input == 'right':
            press('r')
        elif game_input == 'a':
            press('a')
        elif game_input == 'b':
            press('b')
        elif game_input == 'start':
            press('s')
        elif game_input == 'select':
            press('d')            
        # elif game_input == 'SAVE':
        #     press('f5')
        else:
            return 'Invalid Input'
        return 'OK'

    return app


if __name__ == '__main__':
    server = create_server()
    server.run(host='0.0.0.0', port=8080, debug=False)

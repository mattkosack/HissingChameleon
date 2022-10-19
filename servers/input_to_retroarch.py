from flask import Flask, request
import time
import pyautogui
import pydirectinput


def create_server():
	app = Flask(__name__)

	@app.route('/')
	def hello_world():
		return 'Hello, World!'

	@app.route('/input', methods=['POST'])
	def game_input():
		"""
		These are mapped to retroarch bindings, 
		didn't use shift or ctrl because I didn't want 
		any weirdness with them.
		"""
		game_input = request.form['input']
		print('Recieved Input: ' + game_input)
		if game_input == 'up':
			time.sleep(1)
			pydirectinput.press('U')
		elif game_input == 'down':
			time.sleep(1)
			pydirectinput.press('D')
		elif game_input == 'left':
			time.sleep(1)
			pydirectinput.press('L')
		elif game_input == 'right':
			time.sleep(1)
			pydirectinput.press('R')
		elif game_input == 'a':
			time.sleep(1)
			pydirectinput.press('A')
		elif game_input == 'b':
			time.sleep(1)
			pydirectinput.press('B')
		elif game_input == 'start':
			time.sleep(1)
			pydirectinput.press('S')
		elif game_input == 'select':
			time.sleep(1)
			pydirectinput.press('D')

		else:
			return 'Invalid Input'
		return 'OK'

	return app


if __name__ == '__main__':
	server = create_server()
	server.run(host='0.0.0.0', port=8080, debug=False)

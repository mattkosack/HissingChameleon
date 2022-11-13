from flask import Flask, request
import time
from pyautogui import press



def create_server():
	app = Flask(__name__)

	@app.route('/')
	def hello_world():
		return 'Hello, World!'

	@app.route('/input', methods=['POST'])
	def game_input():
		game_input = request.form['input']
		print('Recieved Input: ' + game_input)

		# These inputs should work for 'Pokewild'
		if game_input == 'up':
			time.sleep(1)
			press("up")
		elif game_input == 'down':
			time.sleep(1)
			press("down")
		elif game_input == 'left':
			time.sleep(1)
			press("left")
		elif game_input == 'right':
			time.sleep(1)
			press("right")
		elif game_input == 'a':
			time.sleep(1)
			press("z")
		elif game_input == 'b':
			time.sleep(1)
			press("x")
		elif game_input == 'start':
			time.sleep(1)
			press("enter")
		elif game_input == 'select':
			time.sleep(1)
			press("c")
		else:
			return 'Invalid Input'
		return 'OK'

	return app


if __name__ == '__main__':
	server = create_server()
	server.run(host='0.0.0.0', port=8080, debug=False)



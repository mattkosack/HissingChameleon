from flask import Flask, request
from pyautogui import press, keyDown, keyUp


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
			keyDown('up')
			keyUp('up')

		elif game_input == 'down':
			keyDown("down")
			keyUp("down")


		elif game_input == 'left':
			keyDown("left")
			keyUp("left")

		elif game_input == 'right':
			keyDown("right")
			keyUp("right")

		elif game_input == 'a':
			keyDown("z")
			keyUp("z")

		elif game_input == 'b':
			keyDown("x")
			keyUp("x")

		elif game_input == 'start':
			keyDown("enter")
			keyUp("enter")

		elif game_input == 'select':
			keyDown("c")
			keyUp("c")
		else:
			return 'Invalid Input'
		return 'OK'

	return app


if __name__ == '__main__':
	server = create_server()
	server.run(host='0.0.0.0', port=8080, debug=False)



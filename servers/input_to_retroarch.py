from flask import Flask, request
import uinput
import time


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
		device = uinput.Device([
			uinput.KEY_U,
			uinput.KEY_D,
			uinput.KEY_L,
			uinput.KEY_R,
			uinput.KEY_A,
			uinput.KEY_B,
			uinput.KEY_S,
			uinput.KEY_D,
		])
		game_input = request.form['input']
		print('Recieved Input: ' + game_input)
		if game_input == 'up':
			time.sleep(1)
			device.emit_click(uinput.KEY_U)
		elif game_input == 'down':
			time.sleep(1)
			device.emit_click(uinput.KEY_D)
		elif game_input == 'left':
			time.sleep(1)
			device.emit_click(uinput.KEY_L)
		elif game_input == 'right':
			time.sleep(1)
			device.emit_click(uinput.KEY_R)
		elif game_input == 'a':
			time.sleep(1)
			device.emit_click(uinput.KEY_A)
		elif game_input == 'b':
			time.sleep(1)
			device.emit_click(uinput.KEY_B)
		elif game_input == 'start':
			time.sleep(1)
			device.emit_click(uinput.KEY_S)
		elif game_input == 'select':
			time.sleep(1)
			device.emit_click(uinput.KEY_D)
		else:
			return 'Invalid Input'
		return 'OK'

	return app


if __name__ == '__main__':
	server = create_server()
	server.run(host='0.0.0.0', port=8080, debug=False)

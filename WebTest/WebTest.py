# coding:utf-8
import os
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__, static_folder="./game", template_folder="./templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
	return redirect(url_for('index'))

@app.route('/game/<mark>', methods=['GET', 'POST'])
def game(mark):
	# print("mark = " + mark)
	if mark == "new":
		return render_template('new_game.html')
	elif mark == "save":
		# postData = request.form
		# print("postData = " + str(postData))
		# print(request.values)
		if request.method == "POST":
			value = request.values.get('data_for_game')
			# print(value)
			write_config(value)

			return render_template('game.html', get_game_info = get_game_info())
		elif request.method == "GET":
			value = request.values.get('game_index')
			if len(str(value)) == 0:
				return render_template('game.html', get_game_info = get_game_info())
			data = request.values.get('data_for_game')
			if len(str(data)) == 0:
				return render_template('game.html', get_game_info = get_game_info())

			modify_game("game" + str(value) + ".config", data)

			return render_template('game.html', get_game_info = get_game_info())

	elif mark == "cancel":
		return render_template('game.html', get_game_info = get_game_info())
	elif mark == "design":
		return render_template('game.html', get_game_info = get_game_info())
	elif mark == "get":
		if request.method == "GET":
			value = request.values.get('num')
			if len(str(value)) == 0:
				return render_template('game.html', get_game_info = get_game_info())

			data = get_one_game_info("game" + str(value) + ".config")
			# print(data)
		return data
	else:
		return redirect(url_for("index"))


def modify_game(file, data):
	current_path = os.path.dirname(os.path.realpath(__file__))
	config_path = current_path + "/config"
	new_data = data.replace('\r', '')
	try:
		with open(config_path + '/' + file, 'w') as game:
			game.write("[game]\n" + new_data)
	except :
		pass


def get_one_game_info(file):
	current_path = os.path.dirname(os.path.realpath(__file__))
	config_path = current_path + "/config"
	data = ""
	try:
		with open(config_path + '/' + file, 'r') as game:
			game.readline()
			for gi in game.readlines():
				print(len(gi))
				if len(gi) == 1:
					continue
				data = data + gi.replace('\n', '-')
	except :
		pass

	return data


def write_config(value):
	current_path = os.path.dirname(os.path.realpath(__file__))
	config_path = current_path + "/config"
	new_value = value.replace('\r', '')
	print(new_value)
	num = 1
	if os.path.exists(config_path):
		for rt, dirs, files in os.walk(config_path):
			for f in files:
				fname = os.path.splitext(f)
				if fname[1] == ".config":
					# print(f)
					num += 1
					# os.chdir(rt + s)
	else:
		os.makedirs(config_path)

	try:
		with open(config_path + './game' + str(num) + '.config', 'w') as game:
			game.write("[game]\n" + new_value)
	except :
		pass


def get_game_info():
	current_path = os.path.dirname(os.path.realpath(__file__))
	config_path = current_path + "/config"
	num = 0
	if os.path.exists(config_path):
		for rt, dirs, files in os.walk(config_path):
			for f in files:
				fname = os.path.splitext(f)
				if fname[1] == ".config":
					# print(f)
					num += 1
					# os.chdir(rt + s)
		return [(i+1, "第 {} 关".format(i+1)) for i in range(num)]			
	else:
		os.makedirs(config_path)

	

if __name__ == "__main__":
	app.jinja_env.auto_reload = True 
	app.run(debug=True, host='0.0.0.0', port=5000)

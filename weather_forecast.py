from flask import Flask, render_template, request
import json
import urllib.request


app = Flask(__name__)

@app.route('/', methods =['POST', 'GET'])
def weather_forecast():
	if request.method == 'POST':
		lat = request.form['lat']
		lon = request.form['lon']
	else:
		lat = 38.2527
		lon = 85.7585

	source = urllib.request.urlopen('https://api.weather.gov/points/'+lat+',-'+lon).read()
	list_of_data = json.loads(source)
	source2 = urllib.request.urlopen(str(list_of_data['properties']['forecast'])).read()
	list_of_data2 = json.loads(source2)
	result_list = []
	data1 = list_of_data2['properties']['periods']
	for period in data1:
		for key,value in period.items():
			if value=='Today' or value=='Tonight':
				print(period['temperature'])
				result_list.append(period['temperature'])

	data = {
		"temperature_for_today": result_list[0],
		"temperature_for_tonight": result_list[1],
	}

	print(data)
	return render_template('index.html', data = data)



if __name__ == '__main__':
	app.run(debug = True)

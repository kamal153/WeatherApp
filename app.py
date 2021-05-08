from flask import Flask, render_template, request
import requests

app = Flask(__name__)
flag = True;

@app.route('/', methods =['POST', 'GET'])
def weather():
	if request.method == 'POST':
		city = request.form['city'].lower()
	else:
		# for default name surat
		city = 'surat'

	# your API key will come here
	api = "78918dcf76e5d47e073f7716342f6cf8"

	# response contain data from api
	response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api)

	# data for variable list_of_data
	data = {}
	warning = ""
	if response.status_code == 200 :
		dict = response.json()
		data = {
			"country_code": dict['sys']['country'],
			"cityname": dict['name'],
			"coordinate": str(dict['coord']['lon']) + ' '
						  + str(dict['coord']['lat']),
			"temp": str(dict['main']['temp']) + ' K',
			"temp_cel": str(float("{:.2f}".format(dict['main']['temp'] - 273.15))) + ' °C',
			"pressure": str(dict['main']['pressure']),
			"humidity": str(dict['main']['humidity']),
			"weather_desc": str(dict['weather'][0]['description']),
			"wind_speed": str(dict['wind']['speed'])
		}
	else :
		warning = "Something goes wrong"
	return render_template('index.html', data =data , warning = warning)

@app.route("/searchByPosition", methods =['POST', 'GET'])
def tempratureByCoords():
	if request.method == 'POST':
		latitude = str(request.form['lat'])
		longitude = str(request.form['lon'])
	else:
		# for default name surat
		latitude = str(21.1667)
		longitude = str(72.8333)

	# your API key will come here
	api = "78918dcf76e5d47e073f7716342f6cf8"

	# response contain data from api
	response = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=' + latitude + '&lon=' + longitude + '&appid=' + api)

	# data for variable list_of_data
	data = {}
	warning = ""
	if response.status_code == 200 :
		dict = response.json()
		data = {
			"country_code": dict['sys']['country'],
			"cityname": dict['name'],
			"coordinate": str(dict['coord']['lon']) + ' '
						  + str(dict['coord']['lat']),
			"temp": str(dict['main']['temp']) + ' K',
			"temp_cel": str(float("{:.2f}".format(dict['main']['temp'] - 273.15))) + ' °C',
			"pressure": str(dict['main']['pressure']),
			"humidity": str(dict['main']['humidity']),
			"weather_desc": str(dict['weather'][0]['description']),
			"wind_speed": str(dict['wind']['speed'])
		}
	else :
		warning = "Something goes wrong"
	return render_template('searchByPosition.html', data =data , warning = warning)

if __name__ == '__main__':
    app.run(debug=True)

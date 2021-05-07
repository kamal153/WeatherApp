from flask import Flask, render_template, request

# requests to make a request to api
import requests

app = Flask(__name__)

@app.route('/', methods =['POST', 'GET'])
def weather():
	if request.method == 'POST':
		city = request.form['city']
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
			"cityname": city,
			"coordinate": str(dict['coord']['lon']) + ' '
						  + str(dict['coord']['lat']),
			"temp": str(dict['main']['temp']) + 'k',
			"pressure": str(dict['main']['pressure']),
			"humidity": str(dict['main']['humidity']),
		}
	else :
		warning = "Something goes wrong"
	return render_template('index.html', data =data , warning = warning)

if __name__ == '__main__':
    app.run(debug=True)
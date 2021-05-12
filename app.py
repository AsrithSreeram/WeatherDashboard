import requests
import configparser
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def weatherDashboard():
    return render_template('home.html')


@app.route('/results', methods=['POST'])

def renderResults():
    zipcode = request.form['zipcode']
    api_key = getApiKey()
    data = get_weather_results(zipcode, api_key)
    temp = "{0:.2f}".format(data["main"]["temp"])
    feelsLike = "{0:.2f}".format(data["main"]["feels_like"])
    tempMin = "{0:.2f}".format(data["main"]["temp_min"])
    tempMax = "{0:.2f}".format(data["main"]["temp_max"])
    weather = data["weather"][0]["main"]
    location = data["name"]



    return render_template('weatherResults.html', location=location, weather = weather, tempMax = tempMax, tempMin = tempMin, feelsLike = feelsLike, temp = temp)


def getApiKey():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather_results(zip_code, api_key):
    api_url = "http://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}".format(zip_code, api_key)
    req = requests.get(api_url)
    print(api_url)
    return req.json()


if __name__ == '__main__':
    app.run()





import requests

from proj.settings import OPEN_WEATHER_API_KEY


def get_weather_data(city):
    """
    Get weather data from openweathermap.org
    """
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': OPEN_WEATHER_API_KEY}
    try:
        response = requests.get(url, params=params, timeout=50)
    except requests.exceptions.Timeout:
        return None
    if response.status_code == 200:
        weather = response.json()
        data = weather['main']
        print(data)
        return {"current_temperature": f"{round(data['temp'] - 273.15, 2)}°C", "current_pressure": data["pressure"],
                "current_humidity": data["humidity"]}
    else:
        return None
# # base_url variable to store url
# base_url = "http://api.openweathermap.org/data/2.5/weather?"
#
# # Give city name
# city_name = "Chittagong"
#
# # complete_url variable to store
# # complete url address
# complete_url = base_url + "appid=" + api_key + "&q=" + city_name
#
# # get method of requests module
# # return response object
# response = requests.get(complete_url)
#
# # json method of response object
# # convert json format data into
# # python format data
# x = response.json()
#
# # Now x contains list of nested dictionaries
# # Check the value of "cod" key is equal to
# # "404", means city is found otherwise,
# # city is not found
# if x["cod"] != "404":
#
#     # store the value of "main"
#     # key in variable y
#     y = x["main"]
#
#     # store the value corresponding
#     # to the "temp" key of y
#     current_temperature = round(y["temp"] - 273.15, 2)
#
#     # store the value corresponding
#     # to the "pressure" key of y
#     current_pressure = y["pressure"]
#
#     # store the value corresponding
#     # to the "humidity" key of y
#     current_humidity = y["humidity"]
#
#     # store the value of "weather"
#     # key in variable z
#     z = x["weather"]
#
#     # store the value corresponding
#     # to the "description" key at
#     # the 0th index of z
#     weather_description = z[0]["description"]
#
#     # print following values
#     print(" Temperature (in kelvin unit) = " +
#           f'{current_temperature}°C' +
#           "\n atmospheric pressure (in hPa unit) = " +
#           str(current_pressure) +
#           "\n humidity (in percentage) = " +
#           str(current_humidity) +
#           "\n description = " +
#           str(weather_description))
#
# else:
#     print(" City Not Found ")
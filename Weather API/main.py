import requests

#import weather data
api_key = "42405309b8cf8efac9d437df5b4fbd4f"
endpoint = "https://api.openweathermap.org/data/2.5/forecast?"

param_dict = {"lon": -0.1276474,
              "lat": 51.5073219,
             "appid": api_key,
              }

response = requests.get(url=endpoint, params=param_dict)
response.raise_for_status()

#change data to json
data = response.json()

# get first 12 data points
next_12_hours_weather_data = data["list"][0:4]

weather_every_3_hours = [data_point["weather"][0]["main"] for data_point in next_12_hours_weather_data]
print(weather_every_3_hours)
if "Rain" in weather_every_3_hours:
    print("bring an umbrella")

#do with id instead
weather_id_every_3_hours = [data_point["weather"][0]["id"] for data_point in next_12_hours_weather_data]
print(weather_id_every_3_hours)

# if any id code less than 700 in the next 12 hours, it will rain
if any(id < 700 for id in weather_id_every_3_hours):
    print("bring an umbrella")



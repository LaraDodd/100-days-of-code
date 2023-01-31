import requests
from twilio.rest import Client

account_sid = "AC1528a805a7d8cd40e96df09d118bafad"
auth_token = "f1c976d15dd55641ef772c62cd01837e"
api_key = "42405309b8cf8efac9d437df5b4fbd4f"
endpoint = "https://api.openweathermap.org/data/2.5/forecast?"

param_dict = {"lon": -0.1276474,
              "lat": 51.5073219,
             "appid": api_key,
              }
#import weather data
response = requests.get(url=endpoint, params=param_dict)
response.raise_for_status()

#change data to json
data = response.json()

#find rain data with id
next_12_hours_weather_data = data["list"][0:4]
weather_id_every_3_hours = [data_point["weather"][0]["id"] for data_point in next_12_hours_weather_data]
print(weather_id_every_3_hours)

# if any id code less than 700 in the next 12 hours, it will rain
if any(id < 700 for id in weather_id_every_3_hours):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It is going to rain today. Remember to bring an umbrella!",
        from_="+14706467644",
        to="+447518361866"
    )

    print(message.status)





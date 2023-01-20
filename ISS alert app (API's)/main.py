import requests
import datetime as dt
import math
import time
import smtplib

# global positional coords
LAT = 51.50664381598544
LONG = -0.3170335540148875


def get_iss_data():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    response.raise_for_status()  # get specific response error message if there is one

    data = response.json()  # convert api response object into json data
    print(data)
    return data


def get_sunrise_sunset_data():
    # create parameter dict for sunrise/sunset API input
    params_dict = {"lat": LAT,
                   "lng": LONG,
                   "formatted": 0,
                   }

    # call the sunrise and sunset times
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=params_dict)

    response.raise_for_status()  # check that no errors

    data = response.json()
    return data


# bool function if dark
def is_night():
    # get sun data
    sun_data = get_sunrise_sunset_data()

    # pull out sunrise and sunset hours
    sunrise = int(sun_data["results"]["sunrise"][11:13])  # hour of sunrise
    sunset = int(sun_data["results"]["sunset"][11:13])  # hour of sunset

    # get time now (hour)
    now = dt.datetime.now()
    now_hour = now.hour

    if now_hour > sunrise and now_hour < sunset:
        return False
    else:
        return True


# if is is going over position and it is night, send an email

# bool function to check if is over position (+- 5 degs)
def is_over_position():
    iss_data = get_iss_data()
    iss_pos = (iss_data["iss_position"]["latitude"], iss_data["iss_position"]["longitude"])
    print(iss_pos)
    house_pos = (LAT, LONG)

    if math.dist(iss_pos, house_pos) <= 5:
        return True
    else:
        return False


def send_email(to_address: str) -> None:
    """Takes in email address as string and sends an email saying 'look up'

    Args: to_address - string denoting an email address"""

    my_email = "testdodd4@gmail.com"
    password = "ejkfnemvhvomgnfc"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # secures connection to email server to prevent risk of email hacking. tls = Transport
        # Layer Security
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_address,
            msg=f"LOOK UP! THE ISS IS OVER YOUR HOUSE!"
        )


# while both true, send email function, sleep 60 seconds
while is_over_position() and is_night():
    send_email("laradodd97@gmail.com")
    time.sleep(60)

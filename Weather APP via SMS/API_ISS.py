import requests
import datetime as dt
import time

MY_LAT = 40.778198
MY_LNG = -74.067863


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # print(response)
    # print(response.status_code)
    response.raise_for_status()
    data1 = response.json()
    latitude = float(response.json()["iss_position"]["latitude"])
    longitude = float(response.json()["iss_position"]["longitude"])
    # print(data1)
    # print(type(latitude))
    # print(longitude)
    iss_position = (latitude, longitude)
    # print(iss_position)
    if MY_LAT - 5.0 <= latitude <= MY_LAT + 5.0 and MY_LNG - 5 <= longitude <= MY_LNG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    response_sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()
    data = response_sun.json()
    # print(data)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # print(sunrise)
    # print(sunset)

    time_now = dt.datetime.utcnow().hour
    # print(time_now)
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        print("look ahead")
    else:
        print("iss not overhead")

# def get_quote():
#     # this function is for practice
#     response1 = requests.get(url="https://api.kanye.rest")
#     response1.raise_for_status()
#     data = response1.json()
#     #print(data)
#     quote = data["quote"]
#     print(quote)

# get_quote()


# """
# 1XX hold on
# 2XX here you go
# 3XX go away
# 4XX you screwed up
# 5XX Server screwed up
# """

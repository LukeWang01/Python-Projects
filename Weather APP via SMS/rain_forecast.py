import requests
import datetime as dt
import time

LON = -74.0553
LAT = 40.7967
API_KEY = "81139b246e19d2aaa6599a775b8047e3"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
LOC_PARAMS = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "units": "imperial",
    "exclude": "current,minutely,daily"
}
# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&exclude=&appid={
# API_KEY}")

response = requests.get(OWM_ENDPOINT, params=LOC_PARAMS)
response.raise_for_status()
data = response.json()
# print(type(data))
# print(type(data["hourly"]))
# print(type(data["hourly"][0]))
# print(data["hourly"][0]) # 48 hours data
# print(data["hourly"][0]["weather"][0])
# print(data["hourly"][0]["weather"][0]["id"])
hourly_data_list = data["hourly"][:12]  # we need data within 12 hours 0:11

umbrella_needed = False

for i_data in hourly_data_list:
    hourly_weather_id = i_data["weather"][0]["id"]
    # print(type(hourly_weather_id))
    # print(hourly_weather_id)
    if hourly_weather_id < 700:
        umbrella_needed = True

if umbrella_needed:
    print("Bring an umbrella")
else:
    print("Just go out and have fun")





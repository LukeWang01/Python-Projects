import os
from keys import *
import requests
from twilio.rest import Client
from dotenv import load_dotenv
import datetime as dt
import time

# load keys from .env file
load_dotenv(".env")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

LON = -74.0553
LAT = 40.7967
API_KEY = OPENWEATHER_API_KEY
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

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# My phone from twilio: +15735744021   signup number: +12016801401
account_sid = TWILIO_ACCOUNT_SID
print(account_sid)
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)
if umbrella_needed:
    message_body = "It will be raining today, don't forget to bring 🌂 ️"
else:
    message_body = "Nice Day, go out and have fun 🌄 "

message = client.messages \
    .create(
    body=message_body,
    from_='+15735744021',
    to='+12016801401'
    )

# print(message.status)
# print(message.body)
# print("Bring an umbrella")

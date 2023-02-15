import requests
from datetime import datetime

MY_LAT = 44.175865
MY_LONG = -76.398453

params = {
    "lat": MY_LAT
    ,"lng": MY_LONG
    ,"formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()

print(sunrise)

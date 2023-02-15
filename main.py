import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
FROM_EMAIL = "" #input your email
TO_EMAIL = "" #input your email
PASSWORD = "" #input your email account password

def issOverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if (MY_LAT -5 <= iss_latitude <= MY_LAT +5) or (MY_LONG -5 <= iss_longitude <= MY_LONG +5):
        return True


def isNight():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True

while True:
    time.sleep(60)
    if issOverhead() and isNight():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL
            ,to_addrs=TO_EMAIL
            ,msg="Subject: Lookup!\n\nThe ISS is above you in the sky!"
        )

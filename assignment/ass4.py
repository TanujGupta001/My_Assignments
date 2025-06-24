#ques1
import requests
from datetime import datetime

def weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=43fe088c5465643c59dcca433ec89adb&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temperature = data["main"]["temp"]
        humidity =  data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]
        min_temp = data["main"]["temp_min"]
        max_temp = data["main"]["temp_max"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"].capitalize()
        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M:%S')

        print(f"Temperature :{temperature} degree Celcius (Feels_like: {feels_like} degree Celcius)")
        print(f"Humidity : {humidity}%")
        print(f"Wind Speed      : {wind_speed} m/s")
        print(f" Sunrise         : {sunrise}")
        print(f" Sunset          : {sunset}")
        print(f" Description     : {description}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data : {e}")
city = input("Enter city name:")

weather(city)

#ques 2
import csv

data = [
    ["Name", "Address", "Mobile no.", "Email"],
    ["Rahul Sharma", "123 MG Road, Mumbai", "+91-9876543210", "rahul.sharma@example.com"],
    ["Ananya Verma", "45 Civil Lines, Delhi", "+91-9123456789", "ananya.verma@example.com"],
    ["Amit Mehta", "78 Park Street, Kolkata", "+91-9988776655", "amit.mehta@example.com"]
]

with open("address_book.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open ("address_book.csv","r")as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
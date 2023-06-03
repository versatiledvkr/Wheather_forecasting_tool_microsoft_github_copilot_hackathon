import requests
import json

def get_weather(city):
    api_key = "97e43531b3fe17c79a45f74e2ad1a5f0"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = json.loads(response.content)
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        print(f"Weather forecast for {city}:")
        print(f"Temperature: {temperature}°C") 
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print("Error fetching weather data.")

def main():
    city = input("Enter the name of a city: ")
    get_weather(city)

if __name__ == "__main__":
    main()

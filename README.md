# Wheather_forecasting_tool_microsoft_github_copilot_hackathon
This repository contains a weather forecasting tool that utilizes the OpenWeatherMap API to retrieve and display weather information for a given city.It is a Python script that prompts the user to enter the name of a city and then fetches the weather data for that city using the API. The weather data includes temperature, humidity, and a description of the weather conditions.

# Prerequisites
Python 3.9,
requests,json
# Installation
Clone the repository to your local machine or download the code as a zip file.
Make sure you have Python installed on your system.
Install the requests library by running the following command in your terminal:
pip install requests
# Usage
Open a terminal and navigate to the directory where the code is located.
Run the script using the following command:
python weather_forecast.py
The script will prompt you to enter the name of a city. Type the name of the city and press Enter.
The weather forecast for the specified city will be displayed, including the temperature in Celsius, humidity percentage, and a brief description of the weather conditions.
Note: Please make sure you have an active internet connection for the script to fetch the weather data from the API.

# API Key
To make requests to the OpenWeatherMap API, an API key is required. The API key used in this script is provided as a constant in the get_weather() function. If you encounter any issues with the API key, you may need to generate your own key by creating an account on the OpenWeatherMap website and replace the api_key variable with your own API key.

# Contribution
Contributions to this repository are welcome. If you find any bugs or have suggestions for improvement, please feel free to open an issue or submit a pull request.

# License
This project is licensed under the MIT License.

Enjoy using the weather forecasting tool!

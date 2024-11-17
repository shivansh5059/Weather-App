import requests
import json
import pyttsx3

# Prompt the user for the city name
print("Enter the name of the city:")
city = input()

# Build the API URL
url = f"https://api.weatherapi.com/v1/current.json?key=11faeb0cc50e460c997131702241711&q={city}"

# Fetch the weather data
response = requests.get(url)

# Parse the JSON response
weather_data = json.loads(response.text)

# Extract the temperature in Celsius
temperature = weather_data["current"]["temp_c"]

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Use the text-to-speech engine to announce the weather
engine.say(f"The current weather in {city} is {temperature} degrees")
engine.runAndWait()
"""
Week 10-2 Bonus: Live Weather API
CIS 3680
Optional, ungraded, no submission, nothing here is graded or quizzed.
Fill in the TODOs yourself before checking your work against the writeup.

Needs two extra installs plus internet access:
    python3 -m pip install requests matplotlib
If that doesn't work on your machine, ask about the Google Colab version
instead, no installs needed there.
"""

from datetime import datetime

import matplotlib.pyplot as plt
import requests

WEATHER_CODES = {
    0: ("Clear sky", "☀️"),
    1: ("Mainly clear", "\U0001f324️"),
    2: ("Partly cloudy", "⛅"),
    3: ("Overcast", "☁️"),
    61: ("Light rain", "\U0001f327️"),
    95: ("Thunderstorm", "⛈️"),
}


def search_locations(city_name):
    """Returns every matching place for a typed name, not just the first."""

    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city_name,
        "count": 5,
    }
    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    if "results" not in data or len(data["results"]) == 0:
        raise ValueError(f"No location found for '{city_name}'")
    else:
        return data["results"]


def choose_location(matches):
    """One match: use it. More than one: show name/state/country and ask."""

    if len(matches) == 1:
        return matches[0]

    print(f"Found {len(matches)} matches for '{city_name}':")
    for i, place in enumerate(matches, start=1):
        state = place.get("admin1", "")
        country = place.get("country", "")
        label = ",".join(part for part in [place["name"], state, country] if part)
        print(f" {i}. {label}")

    choice = input("Enter the number for corresponding choice: ")
    return choice

     

def safe_filename_part(text):
    """Turns a place name into something safe to use in a filename."""
    # TODO: lowercase the text and replace spaces with underscores
     

def get_current_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
        "temperature_unit": "fahrenheit"
    }

    response = requests.get(url, params=params, timeout=10)

    return response.json()["current_weather"]



def live_weather_lookup(city):

    search_locations(city_name)
    choose_location(choice)


    # TODO: pull latitude, longitude, name, and admin1 (the state) out of
    # that place dictionary, using .get("admin1", "") for the state since
    # not every result has one

    # TODO: GET "https://api.open-meteo.com/v1/forecast" with params
    # latitude, longitude, current_weather=True, temperature_unit="fahrenheit",
    # then pull ["current_weather"] out of the response

    # TODO: use WEATHER_CODES.get() with a default to turn the weathercode
    # into a (description, emoji) pair, then print something like
    # "<emoji> <city>, <state>: <description>, <temperature>F"

    # TODO: GET the same URL again with params latitude, longitude,
    # hourly="temperature_2m", forecast_days=1, temperature_unit="fahrenheit",
    # then pull "time" and "temperature_2m" out of response.json()["hourly"]

    # TODO: plot hours (x) vs temperatures (y) with matplotlib, same pattern
    # as the Week 1 Personal Budget Analyzer chart

    # TODO: build a filename using safe_filename_part(), the state, and
    # datetime.now().strftime("%Y%m%d_%H%M%S") so each run saves a new file
    # instead of overwriting the last one, then plt.savefig() it

    print("Nothing fetched yet, fill in the TODOs above.")
    print()


if __name__ == "__main__":
    # TODO: use input() to ask for a city name, then   it to live_weather_lookup()
     


# Real-Time Data Pipeline for MLB HR Prediction Engine

import requests
import pandas as pd

# --- MLB API Sample (Pitching and Statcast Events) ---
def get_mlb_statcast_data(game_date='2025-05-08'):
    url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={game_date}"
    schedule = requests.get(url).json()
    games = schedule['dates'][0]['games']

    all_games = []
    for game in games:
        game_pk = game['gamePk']
        game_data_url = f"https://statsapi.mlb.com/api/v1.1/game/{game_pk}/feed/live"
        game_data = requests.get(game_data_url).json()
        all_games.append(game_data)

    return all_games

# --- Weather API Sample (OpenWeatherMap or Meteostat) ---
def get_weather_data(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    full_url = base_url + f"q={city_name}&appid={api_key}&units=imperial"
    response = requests.get(full_url)
    return response.json()

# --- Park Factor Example ---
park_factors = {
    'Coors Field': 1.25,
    'Yankee Stadium': 1.18,
    'Dodger Stadium': 1.02,
    'Oracle Park': 0.85
    # Add full set of MLB ballparks with HR factors
}

# --- Usage ---
# mlb_data = get_mlb_statcast_data()
# weather = get_weather_data("Denver", "YOUR_OPENWEATHER_API_KEY")

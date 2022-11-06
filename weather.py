import requests
import json

##Idea: Build a weather app to show the current weather with description and a maximum of five days forward with a frontend


def __fetch_weather__():    
    weather_data = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Copenhagen?unitGroup=metric&key=AK8K8TCEDGVRRJ46XE5UE4W5N&contentType=json").text
    response_info = json.loads(weather_data)
    return response_info


def __show_weather_data__():
    weather_list = []

    response_info = __fetch_weather__()

    for weather_info in response_info['days']:
        weather_list.append([weather_info['datetime'],weather_info['feelslike'],weather_info['description']])
    
    print(weather_list)

__show_weather_data__()
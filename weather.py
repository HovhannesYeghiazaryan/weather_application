#!/usr/bin/python
import requests

# Batays latitude = 47.1667 longitude = 39.7333


def constructing_city_url(lat, lon, temp_indicator_unit="default", lang="us"):
    """
    lat = Latitude of choosen city
    lon = Longitude of choosen city
    temp_indicator_unit = Temperature Indicator default is Kelvin, imperial is Fahrenheit and metric is Celsius
    finall_url = Correct created url for API call
    """
    coordinates = f"lat={lat}&lon={lon}"
    base_url = "https://api.openweathermap.org/data/2.5/forecast?"
    API_KEY = "2deb525b60d195740520dbc646f03de1"
    correct_url = f"""{base_url}{coordinates}&units={temp_indicator_unit}&lang={lang}&appid={API_KEY}"""
    response = requests.get(correct_url)
    json = response.json()
    json_list = json["list"]
    city_name = json["city"]["name"]

    weather = open("weather.txt", "w+")
    weather.writelines(f"{city_name}\n")

    if temp_indicator_unit == "metric":
        temp_unit = "Celsius"
    elif temp_indicator_unit == "imperial":
        temp_unit = "Fahrenheit"
    else:
        temp_unit = "Kelvin"

    for index in range(len(json_list)):
        is_date_time_correct = json_list[index]["dt_txt"]

        if is_date_time_correct[11:] == "06:00:00":
            current_time = is_date_time_correct[:11]
            morning_temp = json_list[index]["main"]["temp"]
            max_temp = json_list[index]["main"]["temp_max"]
            min_temp = json_list[index]["main"]["temp_min"]

            weather.writelines(f"{current_time} Morning temperature is: {morning_temp} {temp_unit}\n")
            weather.writelines(f"{current_time} Maximum temperature is: {max_temp} {temp_unit}\n")
            weather.writelines(f"{current_time} Minimum temperature is: {min_temp} {temp_unit}\n")
    weather.close()


def main():
    constructing_city_url(47.1667, 39.7333, "metric", "ru")


if __name__ == "__main__":
    main()

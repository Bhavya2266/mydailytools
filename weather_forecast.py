import requests


def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C+%t+%w"
    response = requests.get(url)
    data = response.text.splitlines()

   
    weather_info = data[2:9]

    print(f"Weather forecast for {city}:")
    for day in weather_info:
        print(day)


cities = ["montpellier", "paris", "toulose", "marsielle", "Nantes"]
selected_city = input("Enter a city from the list (montpellier, paris, toulose, marsielle, Nantes): ")

if selected_city in cities:
    get_weather(selected_city)
else:
    print("Invalid city. Please choose from the provided list.")


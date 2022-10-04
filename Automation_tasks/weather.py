import requests # request for data from API

API_KEY = "0e67b4742dd5acea187149a9a76a6684"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# how to make an API call:
#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

city = input("Enter a city name: ") # over 2000 cities stored in database
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}" # an f string embeds into strings
response = requests.get(request_url)
# http requests: get, head, post, put, delete

if response.status_code == 200: # look up http status codes. 400 is not found.
    data = response.json()
    weather = data['weather'][0]["description"]
    temperature = round(data['main']['temp'] - 273.5, 2)
    print("Weather", weather)
    print("Temperature: ", temperature, "celsius")
    #print(data)
else: 
    print("An error occurred")
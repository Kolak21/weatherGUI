''' This program is to grab the weather information from OpenWeatherMap and create a city class 
containing the current weather conditions'''

import requests
from city import City

def Create_City(city):
    
    balloon = "854970312fe2a217178bc0a9afc5835d"  
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={balloon}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        name = data['name']
        temp = data['main']['temp']
        weather =  data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        userCity = City(name,temp,weather,humidity,wind)

        userCity.mpsToMph()  # Convert wind speed to mph for display
        userCity.CtoF()      # Convert temperature to Fahrenheit for display

        return userCity
        
        

    except requests.exceptions.HTTPError:
        print("❌ City not found or API error.")
    except Exception as e:
        print("❌ An error occurred:", e)

def main():
    while True:
        city = input("Enter city name (or 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        outputCity = Create_City(city)
        outputCity.weatherReport()

if __name__ == "__main__":
    main()

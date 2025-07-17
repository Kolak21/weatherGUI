# Makes a City object to store weather data for a city
# Contains methods to convert temperature and wind speed units

class City:
    def __init__(self,name,temp,weather,humidity, wind):
        self.name = str(name)
        self.temp = float(temp)
        self.weather = str(weather)
        self.humidity = float(humidity)
        self.wind = float(wind)
        self.isCelcius = True
        self.isMetric = True
    
    #Converts celcius to fahrenheight
    def CtoF(self):
        if self.isCelcius == True:
            self.temp = (self.temp * 1.8) + 32
            self.isCelcius = False
            return
        else:
            return
    
    #Coverts Fahrenheight to celcius
    def FtoC(self):
        if self.isCelcius == False:
            self.temp = (self.temp - 32) * (5/9)
            self.isCelcius == True
            return
        else:
            return
        
    #Conversion methods for wind speed
    def mpsToMph(self):
        if self.isMetric == True:
            self.wind = self.wind * 2.23694
            self.isMetric = False

    def mphToMps(self):
        if self.isMetric == False:
            self.wind = self.wind / 2.23694
            self.isMetric = True


    def getTemp(self):
        return self.temp

    def getWeather(self):
        return self.weather

    def getHumidity(self):
        return self.humidity

    def getWind(self):
        return self.wind

    def weatherReport(self):
        print(f"\nWeather in {self.name}:")

        if self.isCelcius:
            temp_unit = "°C"
        else:
            temp_unit = "°F"
        
        if self.isMetric:
            wind_unit = "m/s"
        else:
            wind_unit = "mph"

        print(f"Temperature: {self.temp} {temp_unit}")
        print(f"Weather: {self.weather}")
        print(f"Humidity: {self.humidity}%")
        print(f"Wind Speed: {self.wind} {wind_unit}\n")
    


# Main function for testing purposes
if __name__ == "__main__":
    city = City("Liliputia", 25.0, "Sunny", 60, 5.0)
    city.weatherReport()
    
    city.CtoF()
    print(f"Temperature in Fahrenheit: {city.getTemp()} °F")
    
    city.FtoC()
    print(f"Temperature back in Celsius: {city.getTemp()} °C")
    
    city.mpsToMph()
    print(f"Wind Speed in MPH: {city.getWind()} mph")
    
    city.mphToMps()
    print(f"Wind Speed back in m/s: {city.getWind()} m/s")

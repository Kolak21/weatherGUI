from tkinter import *
from tkinter import ttk 
from city import City
import wg

# initial screen on start up
def defaultScreen():
    print('GUI is on the way...')
    root = Tk()
    root.geometry("800x600")
    root.title("Weather App")

    # Configure root to allow center alignment
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Create and center the frame
    frm = ttk.Frame(root, padding=20)
    frm.grid(row=0, column=0)
    frm.grid_rowconfigure(0, weight=1)
    frm.grid_columnconfigure(0, weight=1)
    frm.grid_columnconfigure(1, weight=1)

    # Making the user menu at the top left
    userMenu = Menu(root)
    root.config(menu=userMenu)

    # Create an options menu to cascade under 'Options'
    OptionMenu = Menu(userMenu, tearoff=0)
    userMenu.add_cascade(label='Options', menu=OptionMenu)
    OptionMenu.add_command(label='Exit', command=root.quit)


    # Label and Entry in center
    text = Label(frm, text='Enter a city')
    text.grid(row=0, column=0, padx=10, pady=10)

    e1 = Entry(frm)
    e1.grid(row=0, column=1, padx=10, pady=10)

    # Submit Button
    subu = ttk.Button(frm, text='Submit', command=lambda: getWeather(root, frm, e1,))
    subu.grid(row=0, column=2, padx=10, pady=10)

    root.mainloop()

# takes inputted weather and displays a weather report
def getWeather(root, frm, e1):
    print('weather getter accessed')
    userInput = e1.get().strip()
    
    if not userInput:
        print("No input provided.")
        return

    e1.delete(0, END)  # Clear the entry field after submission

    try:
        print(f"Creating city for: {userInput}")
        userCity = wg.Create_City(userInput)
        print("City created successfully.")
        display(userCity, frm, root)
    except Exception as e:
        print(f"Error occurred: {e}")
        Label(frm, text="Could not retrieve weather data.", fg="red").grid(row=1, column=0, columnspan=3, pady=10)

# displays weather info to user and clears previous content
def display(city, frm, root):
    print(f"Displaying data for {city.name}")
    
    # Clear frame
    for widget in frm.winfo_children():
        widget.destroy()

    # Get weather data
    tempString = f"{float(str(city.getTemp())):.2f}"
    weatherString = str(city.getWeather())
    windString = f"{float(str(city.getWind())):.2f}"
    humidityString = str(city.getHumidity())

    print(f"Temperature: {tempString}")
    print(f"Weather: {weatherString}")
    print(f"Wind: {windString}")
    print(f"Humidity: {humidityString}")

    # Determine units
    temp_unit = "°C" if city.isCelcius else "°F"
    wind_unit = "m/s" if city.isMetric else "mph"

    # Weather display
    Label(frm, text='Weather Report in ' + city.name + ':', font=('Arial', 16)).grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    Label(frm, text='Temperature: ' + tempString + temp_unit).grid(row=1, column=0, padx=10, pady=10, sticky="w")
    Label(frm, text='Condition: ' + weatherString).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    Label(frm, text='Wind Speed: ' + windString + ' ' + wind_unit).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    Label(frm, text='Humidity: ' + humidityString + '%').grid(row=4, column=0, padx=10, pady=10, sticky="w")

    # Back button
    ttk.Button(frm, text='Back', command=lambda: resetUI(frm)).grid(row=5, column=0, pady=20)

# returns user to default screen
def resetUI(frm):
    print("Resetting to default input UI.")

    for widget in frm.winfo_children():
        widget.destroy()

    Label(frm, text='Enter a city').grid(row=0, column=0, padx=10, pady=10)

    e1 = Entry(frm)
    e1.grid(row=0, column=1, padx=10, pady=10)

    subu = ttk.Button(frm, text='Submit', command=lambda: getWeather(None, frm, e1))
    subu.grid(row=0, column=2, padx=10, pady=10)

# main function
def main():
    defaultScreen()

if __name__ == "__main__":
    main()

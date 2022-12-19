#This is a Weather App
import tkinter as tk
import requests

# My OpenWeatherMap API key
api_key = "9a970f5612d05e73f54741adb1a7e92f"
#Function to retrieve weather data from the OpenWeatherMap API
def get_weather(city):
  # The base URL for the OpenWeatherMap API
  base_url = "https://api.openweathermap.org/data/2.5/weather?q="

  # Had to make a GET request to the API
  response = requests.get(f"{base_url}{city}&units=imperial&appid={api_key}")


  if response.status_code == 200:
    # If the request is successful, extract the weather data
    data = response.json()
    weather_data = f"Temperature: {data['main']['temp']}°F\n"
    weather_data += f"Description: {data['weather'][0]['description']}\n"
    weather_data += f"Wind Speed: {data['wind']['speed']} mph"
    # Update the label with the weather data
    label.config(text=weather_data)
  else:
    # If the request is not successful, display an error message
    label.config(text=f"An error occurred: {response.status_code}")
# Function to initiate the search for weather data
def search():
  # Get the city from the entry field
  city = entry.get()
  # Retrieve the weather data for the given city
  get_weather(city)

# Window dimensions
HEIGHT = 500
WIDTH = 600
# Create the main window
root = tk.Tk()
# Create a canvas to hold the background image
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Load the background image and display it
background_image = tk.PhotoImage(file= "WEATHERREAL.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create a frame for the city entry and search button
frame = tk.Frame(root, bg="#6E8B3D", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

# Create a button to initiate the search
button = tk.Button(frame, text="Search", font=40, command=search)
button.place(relx=0.7, relwidth=0.3, relheight=1)

entry = tk.Entry(frame, font=40, text="37.7858,-122.401")
entry.place(relwidth=0.65, relheight=1)

# Create a text entry for the city
lower_frame = tk.Frame(root, bg="#6E8B3D", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

# Create a frame to hold the weather data
label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()


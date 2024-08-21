import tkinter as tk
# Main algorithm for the weather forecasting app Weather Forecasting App Features: Users can check the current
# weather and forecast for their location. You could also add severe weather alerts. Learning Aspects: API
# integration (like OpenWeatherMap). Data parsing and display. Implementing alerts and notifications. Timeframe: 2-3
# weeks.

# - - - - - - - - - - - - GUI weather app - - - - - - - - - - - - #
# Use an API to take a city and a country name and get coordinates for it (in long and lat)
screen = tk.Tk()
screen.title("Weather App")

main_image = tk.PhotoImage(file="icons/main_image.png")
# Get image dimensions
image_width = (main_image.width() // 3)
image_height = (main_image.height() // 3)
# create the image in the canvas
canvas = tk.Canvas(width=image_width, height=image_height)
canvas.create_image(image_width // 2, image_height // 2, image=main_image)

canvas.pack()

tk.mainloop()

# Step 1: Graphical User interface (functionality for the buttons and windows) (using tkinter) Step 2: Use an
# API to retrieve live global weather data (using OpenWeatherMap and pandas to format the information) Step 3: Alert
# and notifications opn weather updates using APIs and pandas (use plyer for cross-platform notifications)

# To use API libraries, download requests library to fetch weather data from the API
# To make the Graphical User interface, use the tkinter library 
# 

# Goals for tomorrow (Aug 18th)
# Learn about APIs, how they're used and integrated into python, and how to get live updates
# and getting comfortable with them
# Future goals:
# Learn how to manage pandas, use pandas to control the data retrieved from the weather API


from sense_hat import SenseHat
import csv
from datetime import datetime
import time


# Initialize Sense HAT
sense = SenseHat()

# Get sensor readings
temperature = sense.get_temperature()
humidity = sense.get_humidity()
pressure = sense.get_pressure()
orientation = sense.get_orientation_degrees()

# Convert temperature from Celsius to Fahrenheit
temperature = temperature * 9/5 + 32

# Store data in variables
data = {
    'Timestamp': datetime.now(),
    'Temperature (°C)': temperature,
    'Humidity (%)': humidity,
    'Pressure (mb)': pressure,
    'Pitch (degrees)': orientation['pitch'],
    'Roll (degrees)': orientation['roll'],
    'Yaw (degrees)': orientation['yaw']
}

# Write data to a CSV file
filename = 'sensor_data.csv'
with open(filename, 'a') as file:
    writer = csv.DictWriter(file, fieldnames=data.keys())
    if file.tell() == 0:  # Check if file is empty
        writer.writeheader()  # Write header if file is empty
    writer.writerow(data)

print("Sensor data collected and stored successfully.")

# Wait for one hour
time.sleep(3600) # 3600 seconds = 1 hour

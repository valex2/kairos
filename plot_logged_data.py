import csv
import matplotlib.pyplot as plt
import datetime
import argparse
import os


####################################################################
# This script reads a CSV file containing data from Kairos and plots it.
# Example usage:
# python3 plot_logged_data.py /path/to/data.csv
####################################################################

def plot_data(file_path):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"File '{file_path}' does not exist.")
        return

    # Load data from CSV file
    timestamps = []
    temperatures = []
    gases = []
    humidities = []
    pressures = []
    altitudes = []
    visible_lights = []
    ir_lights = []

    with open(file_path, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            timestamps.append(datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S"))
            temperatures.append(float(row[1]))
            gases.append(float(row[2]))
            humidities.append(float(row[3]))
            pressures.append(float(row[4]))
            altitudes.append(float(row[5]))
            visible_lights.append(float(row[6]))
            ir_lights.append(float(row[7]))

    # Plotting the data
    plt.figure()

    plt.subplot(2, 1, 1)
    plt.plot(timestamps, temperatures, label="Temperature (°C)")
    plt.plot(timestamps, humidities, label="Humidity (%)")
    plt.plot(timestamps, pressures, label="Pressure (hPa)")
    plt.xlabel("Time")
    plt.ylabel("Values")
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(timestamps, visible_lights, label="Visible Light (lux)")
    plt.plot(timestamps, ir_lights, label="IR Light (lux)")
    plt.xlabel("Time")
    plt.ylabel("Light Intensity (lux)")
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Set up argument parser to accept file path from command line
    parser = argparse.ArgumentParser(description="Plot sensor data from a CSV file.")
    parser.add_argument("file_path", type=str, help="Absolute path to the CSV data file.")
    
    args = parser.parse_args()

    # Call the plot function with the provided file path
    plot_data(args.file_path)

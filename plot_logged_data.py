import csv
import matplotlib.pyplot as plt
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
            timestamps.append(float(row[0]))
            temperatures.append(float(row[1]))
            gases.append(float(row[2]))
            humidities.append(float(row[3]))
            pressures.append(float(row[4]))
            altitudes.append(float(row[5]))
            visible_lights.append(float(row[6]))
            ir_lights.append(float(row[7]))

    # Create a single plot with multiple panels (subplots) in 2 columns and 3 rows
    fig, axs = plt.subplots(3, 2, figsize=(12, 10))

    # Plot temperature
    axs[0, 0].plot(timestamps, temperatures, label="Temperature (°C)", color="red")
    axs[0, 0].set_xlabel("Time (s)")
    axs[0, 0].set_ylabel("Temperature (°C)")
    axs[0, 0].legend()
    axs[0, 0].set_title("Temperature")

    # Plot humidity
    axs[0, 1].plot(timestamps, humidities, label="Humidity (%)", color="blue")
    axs[0, 1].set_xlabel("Time (s)")
    axs[0, 1].set_ylabel("Humidity (%)")
    axs[0, 1].legend()
    axs[0, 1].set_title("Humidity")

    # Plot pressure
    axs[1, 0].plot(timestamps, pressures, label="Pressure (hPa)", color="green")
    axs[1, 0].set_xlabel("Time (s)")
    axs[1, 0].set_ylabel("Pressure (hPa)")
    axs[1, 0].legend()
    axs[1, 0].set_title("Pressure")

    # Plot altitude
    axs[1, 1].plot(timestamps, altitudes, label="Altitude (m)", color="purple")
    axs[1, 1].set_xlabel("Time (s)")
    axs[1, 1].set_ylabel("Altitude (m)")
    axs[1, 1].legend()
    axs[1, 1].set_title("Altitude")

    # Plot visible light
    axs[2, 0].plot(timestamps, visible_lights, label="Visible Light (lux)", color="orange")
    axs[2, 0].set_xlabel("Time (s)")
    axs[2, 0].set_ylabel("Light Intensity (lux)")
    axs[2, 0].legend()
    axs[2, 0].set_title("Visible Light")

    # Plot IR light
    axs[2, 1].plot(timestamps, ir_lights, label="IR Light (lux)", color="brown")
    axs[2, 1].set_xlabel("Time (s)")
    axs[2, 1].set_ylabel("Light Intensity (lux)")
    axs[2, 1].legend()
    axs[2, 1].set_title("IR Light")

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Create the output filename based on the input filename
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_file_path = os.path.join("Plots", f"{base_name}.png")

    # Save the plot as a PNG file
    plt.savefig(output_file_path, dpi=300)

    # Display the plot
    plt.show()

if __name__ == "__main__":
    # Set up argument parser to accept file path from command line
    parser = argparse.ArgumentParser(description="Plot sensor data from a CSV file.")
    parser.add_argument("file_path", type=str, help="Absolute path to the CSV data file.")
    
    args = parser.parse_args()

    # Call the plot function with the provided file path
    plot_data(args.file_path)
import csv
import os
import time
from datetime import datetime

import RPi.GPIO as GPIO


# -----------------------------
# Configuration
# -----------------------------

SOIL_SENSOR_PIN = 17

DRY_THRESHOLD = 30
MOIST_THRESHOLD = 60

READ_INTERVAL = 5

DATA_DIRECTORY = "data"
LOG_FILE = os.path.join(DATA_DIRECTORY, "soil_readings.csv")


# -----------------------------
# GPIO Setup
# -----------------------------

def setup_gpio():
    """Configure the Raspberry Pi GPIO pins."""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SOIL_SENSOR_PIN, GPIO.IN)


# -----------------------------
# Soil Monitoring
# -----------------------------

def read_soil_sensor():
    """
    Read the digital soil moisture sensor.

    Returns:
        int: Sensor state returned by the GPIO pin.
    """
    return GPIO.input(SOIL_SENSOR_PIN)


def get_soil_status(sensor_value):
    """
    Convert the sensor state into a readable soil condition.

    Note:
        The exact interpretation depends on the sensor module.
    """
    if sensor_value == GPIO.LOW:
        return "DRY"

    return "MOIST"


def get_irrigation_status(soil_status):
    """
    Determine whether irrigation is recommended.
    """
    if soil_status == "DRY":
        return "RECOMMENDED"

    return "NOT REQUIRED"


# -----------------------------
# Data Logging
# -----------------------------

def initialize_log_file():
    """Create the CSV file and header if it does not exist."""
    os.makedirs(DATA_DIRECTORY, exist_ok=True)

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "timestamp",
                "sensor_value",
                "soil_status",
                "irrigation_status"
            ])


def log_reading(sensor_value, soil_status, irrigation_status):
    """Store a soil monitoring reading in the CSV file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            timestamp,
            sensor_value,
            soil_status,
            irrigation_status
        ])


# -----------------------------
# Display
# -----------------------------

def display_reading(sensor_value, soil_status, irrigation_status):
    """Display the latest soil monitoring information."""
    timestamp = datetime.now().strftime("%H:%M:%S")

    print(
        f"[{timestamp}] "
        f"Sensor: {sensor_value} | "
        f"Soil: {soil_status} | "
        f"Irrigation: {irrigation_status}"
    )


# -----------------------------
# Main Application
# -----------------------------

def main():
    """Run the soil monitoring system."""
    print("=" * 55)
    print("       RASPBERRY PI SOIL MONITORING SYSTEM")
    print("=" * 55)
    print("Monitoring soil conditions...")
    print("Press Ctrl+C to stop.\n")

    setup_gpio()
    initialize_log_file()

    try:
        while True:
            sensor_value = read_soil_sensor()

            soil_status = get_soil_status(sensor_value)

            irrigation_status = get_irrigation_status(
                soil_status
            )

            display_reading(
                sensor_value,
                soil_status,
                irrigation_status
            )

            log_reading(
                sensor_value,
                soil_status,
                irrigation_status
            )

            time.sleep(READ_INTERVAL)

    except KeyboardInterrupt:
        print("\n\nMonitoring stopped.")

    finally:
        GPIO.cleanup()
        print("GPIO resources released.")


if __name__ == "__main__":
    main()
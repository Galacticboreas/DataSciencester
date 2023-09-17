"""
OOP - every class and method must be open for extension (using
techniques like inheritance, composition and polymorphism), but
close for modification.
FP - every function must be open for extension (using techniques
like functional composition, higher-order function and currying),
but closed for modification.
"""

# Examples

# Let's create a robot to detect various objects using sensors,
# here is its OOP version:

# 1) Violation of the principle

def detect_object(sensor_type: str) -> None:
    if sensor_type == "temperature":
        print("Detecting objects using temperature sensor ...")
    elif sensor_type == "ultrasonic":
        print("Detecting object using ultrasonic sensor ...")
    elif sensor_type == "infrared":
        print("Detecting object using infrared sensor ...")

detect_object("infrared")
# Detecting object using infrared sensor ...

# The sensor is added to the operation of the robot detect_object
# by changing the existing code, that is, this approach does not
# apply the principle of openness/closeness.

# 2) Compliance with the principle

from typing import Callable

# We create a higher-order function that accepts various sensors.

def detect_with_sensor(*sensors: Callable) -> None:
    for i, sensor in enumerate(sensors):
        print(f'Sensor {i + 1}:')
        sensor()

# We designate sensors as functions.

def use_temperature_sensor() -> None:
    print("Detecting objects using temperature sensor ...")

def use_ultrasonic_sensor() -> None:
    print("Detecting objects using ultrasonic sensor ...")

def use_infrared_sensor() -> None:
    print("Detecting objects using infrared sensor ...")

# We detect objects using various sensors.

detect_with_sensor(use_ultrasonic_sensor, use_temperature_sensor)
# Sensor 1:
# Detecting objects using ultrasonic sensor ...
# Sensor 2:
# Detecting objects using temperature sensor ...

# 3) An example of a codebase extension.

# We are adding two new sensors to the robot -
# a sensor with a camera and a detection sensor.

def use_camera_sensor() -> None:
    print("Detecting objects using camera sensor ...")

def use_proximity_sensor() -> None:
    print("Detecting objects using proximity sensor ...")

# And add this to a higher-order function:

# We detect objects using various sensors
detect_with_sensor(use_ultrasonic_sensor,
        use_temperature_sensor,
        use_camera_sensor,     # new sensor with camera
        use_proximity_sensor   # new detection sensor
        )

# As a result , it turns out:

# Sensor 1:
# Detecting objects using ultrasonic sensor ...
# Sensor 2:
# Detecting objects using temperature sensor ...
# Sensor 3:
# Detecting objects using camera sensor ...
# Sensor 4:
# Detecting objects using proximity sensor ...

"""
OOP - every child class must be able to be substituted
for its parent class without unexpected behaviour occurring
in the program.
FP - every input argument should be able to be substituted
for another argument that shares the same subtype without
unexpected behaviour occurring in the program.
"""

# Examples

# Here is the OOP version of this principle:

# 1) Violation of the principle

from typing import Callable

def use_household_item(turn_on:              Callable[ [], None],
                       turn_off:             Callable[ [], None],
                       change_temperature:   Callable[ [], None]) -> None:
    turn_on()
    change_temperature()
    turn_off()

def turn_on_fridge() -> None:
    print("Refrigerator turned on.")

def turn_off_fridge() -> None:
    print("Refrigerator turned off.")

def change_temperature_fridge() -> None:
    print("Refrigerator temperature changed.")

def turn_on_laptop() -> None:
    print("Laptop turned on.")

def turn_off_laptop() -> None:
    print("Laptop turned off.")

use_household_item(turn_on_fridge, turn_off_fridge, change_temperature_fridge)

# The principle is violated here, since the temperature of the laptop 
# cannot be changed
use_household_item(turn_on_laptop, turn_off_laptop, change_temperature_fridge)

# Refrigerator turned on.
# Refrigerator temperature changed.
# Refrigerator turned off.
# Laptop turned on.
# Refrigerator temperature changed.
# Laptop turned off.

# The Liskov substitution principle is violated: to change the 
# temperature of the laptop, the change_temperature_fridge function
# is passed to the use_household_item function as the third argument.
# Although the temperature of laptops, unlike refrigerators, is not
# regulated. This is fraught with error, because the
# change_temperature_fridge function is not programmed to adjust the
# temperature of the laptop, the result is unexpected behavior.

# 2) Compliance with the principle

from typing import Callable

def use_temperature_controlled_item(turn_on:            Callable[ [], None],
                                    turne_off:          Callable[ [], None],
                                    change_temperature: Callable[ [], None]) -> None:
    turn_on()
    change_temperature()
    turne_off()

def turn_on_fridge() -> None:
    print("Refrigerator turned on.")

def turn_off_fridge() -> None:
    print("Refrigerator turned off.")

def change_temperature_fridge() -> None:
    print("Refrigerator temperature changed.")

use_temperature_controlled_item(turn_on_fridge, turn_off_fridge, change_temperature_fridge)

# 3) An example of a codebase extension.

# We add another element for temperature control without 
# touching the use_temperature_controlled_item function:

def turn_on_oven() -> None:
    print("Oven turned on.")

def turn_off_oven() -> None:
    print("Oven turned off.")

def change_temperature_oven() -> None:
    print("Oven temperature changed.")

use_temperature_controlled_item(turn_on_oven, turn_off_oven, change_temperature_oven)

# Refrigerator turned on.
# Refrigerator temperature changed.
# Refrigerator turned off.
# Oven turned on.
# Oven temperature changed.
# Oven turned off.

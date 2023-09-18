"""
OOP - no child class should depend on any methods from its
parent class it does not use.
FP - no functions should depend on functions or external
operations it does not need (from input arguments or 
global variables).
"""

# Examples

# An example of different animal behavior is indicative,
# here is its OOP version:

# 1) Violation of the principle

from typing import Callable

# Creating a higher-order function for interacting with animals
def interact_with_animal(make_sound: Callable[ [], None],
                         swim:       Callable[ [], None],
                         fly:        Callable[ [], None]) -> None:
    make_sound()
    swim()
    fly()

# 1. Creating a function for interacting with ducks
def make_duck_sound() -> None:
    print("Quack! Quack!")

def make_duck_swim() -> None:
    print("Duck is now swimming in the water... ")

def make_duck_fly() -> None:
    print("Duck is now flying in the air... ")

# 2. Creating a function for interacting with a cat
def make_cat_sound() -> None:
    print("Meow! Meow!")

def make_cat_swim() -> None:
    raise NotImplementedError("Cats do not swim!")

def make_cat_fly() -> None:
    raise NotImplementedError("Cats do not fly!")

# Interaction with animals
interact_with_animal(make_duck_sound, make_duck_swim, make_duck_fly)

# Here we make the cat swim and fly
interact_with_animal(make_cat_sound, make_cat_swim, make_cat_fly)

# Quack! Quack!
# Duck is now swimming in the water... 
# Duck is now flying in the air...
# Meow! Meow!
# Traceback (most recent call last):
#   File "<string>", line 50, in <module>
#   File "<string>", line 23, in interact_with_animal swim()
#   File "<string>", line 41, in make_cat_swim 
#   raise NotImplementedError("Cats do not swim!")
# NotImplementedError: Cats do not swim!

# In the example, the duck flies, swims, quacks. But the cat 
# has to perform unusual actions for him: swim or fly. We force 
# him to demonstrate unusual behavior and thereby violate the 
# principle of interface separation.

# 2) Compliance with the principle

from typing import Callable

# Creating a higher-order function for each behavior
def make_animal_sound(make_sound: Callable[ [], None]) -> None:
    make_sound()

def make_animal_swim(swim: Callable[ [], None]) -> None:
    swim()

def make_animal_fly(fly: Callable[ [], None]) -> None:
    fly()

# 1. Creating a function for interacting with ducks
def make_duck_sound() -> None:
    print("Quack! Quack!")

def make_duck_swim() -> None:
    print("Duck is now swimming in the water... ")

def make_duck_fly() -> None:
    print("Duck is now flying in the air... ")

# 2. Creating a function for interacting with a cat
def make_cat_sound() -> None:
    print("Meow! Meow!")

# Interaction with animals

# 1. Duck
make_animal_sound(make_duck_sound)
make_animal_swim(make_duck_swim)
make_animal_fly(make_duck_fly)

# 2. Cat
make_animal_sound(make_cat_sound)

# Now let's divide the interact_with_animal function 
# into three separate behaviors:

# make_animal_sound.
# make_animal_swim.
# make_animal_fly.

# We no longer make the cat fly or swim, but call the 
# make_animal_sound function: now the cat meows. This 
# ensures that the cat depends on unused interfaces, 
# while respecting the principle of interface separation.

# 3) An example of a codebase extension.

# Let's add a dog to the codebase:
def make_dog_sound() -> None:
    print("Woof! Woof!")

make_animal_sound(make_dog_sound)

# It turns out this code:

# Woof! Woof!

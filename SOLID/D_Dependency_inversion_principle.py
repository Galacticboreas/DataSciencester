"""
OOP - every class and method should depend on
abstractions, not concrete implementations.
FP - every function should depend on input
arguments only, not concrete operations.
"""

# According to this principle, all modules - regardless 
# of their levels - should depend not on specific 
# implementations, but on abstractions. Any dependence 
# on specific implementations is a direct violation of 
# the dependency inversion principle.

# In the context of functional programming:

# modules are the same as functions;
# abstractions are the same as input parameters; 
# concrete implementations are the same as global 
# variables and hard-coded values or operations 
# in any function.

# In this principle, in order to avoid strong 
# coupling with any modules or variables, emphasis 
# is placed on the use of dependency inversions, 
# thereby simplifying the management, expansion 
# and testing of code behavior in the future.

# Examples

# Here is the OOP version of this example:

# 1) Violation of the principle

# Setting the state of the player
music_player_state = False

# Output the state of the music player
def display_music_player_state() -> None:
    if music_player_state:
        print("ON: Music player switched on.")
    else:
        print("OFF: Music player switched off.")

# Creating a player switch
def press_music_player_switch() -> None:
    global music_player_state
    music_player_state = not music_player_state
    display_music_player_state()

# Click on the player switch
press_music_player_switch()
press_music_player_switch()
press_music_player_switch()

# As a result , it turns out:

# ON: Music player switched on.
# OFF: Music player switched off.
# ON: Music player switched on.

# In this code, display_music_player_state is a 
# specific implementation of turning the player on/off.

# Another specific implementation is the global 
# variable music_player_state with a logical value 
# of the current state of the player\

# The press_music_player_switch function depends
#  on both of these objects, being a direct violation
#  of the dependency inversion principle.

# 2) Compliance with the principle

from ast import Call
from multiprocessing.reduction import steal_handle
from typing import Callable

# Switching the state
def toggle_state(state: bool) -> bool:
    return not state

# Displaying the status
def display_state(state: bool) -> None:
    if state:
        print("ON: Music player switched on.")
    else:
        print("OFF: Music player switched off.")

# Processing the click of the switch
def press_switch(state:   bool,
                 toggle:  Callable[ [bool], bool],
                 display: Callable[ [bool], None]) -> bool:
    new_state = toggle(state)
    display(new_state)

    return new_state

# Setting the initial state
music_player_state = False

# Press the switch
# Here the principle of dependency inversion 
# is observed only depending on the implementation 
# of dependencies

music_player_state = press_switch(music_player_state,
    toggle_state,
    display_state
    )
music_player_state = press_switch(music_player_state,
    toggle_state,
    display_state
    )
music_player_state = press_switch(music_player_state,
    toggle_state,
    display_state
    )

# 3) An example of a codebase extension.

# To add the functionality of adjusting the volume 
# of the player, we will make the code more reliable, 
# and without changing what is already available.

# Here is the code added to the current player script:

from typing import Callable, Tuple

# Adding the functionality of changing the volume
def change_volume(volume: int, increment_counter: int) -> int:
    new_volume = volume + increment_counter

    if new_volume < 0:
        new_volume = 0
    elif new_volume > 100:
        new_volume = 100
    print(f'New volume: {new_volume} ')

    return new_volume

# Adding the functionality of using the player
def use_music_player(state: bool,
                     volume: int,
                     operations: Callable[ [bool, int], Tuple[bool, int]]) -> Tuple[bool, int]:
    new_state, new_volume = operations(state, volume)

    return new_state, new_volume

# Setting the initial constants
current_state = False
current_volume = 0

# Increasing the volume of the player
def increase_operations(state: bool, volume: int) -> Tuple[bool, int]:
    new_state = toggle_state(state)
    display_state(new_state)
    new_volume = change_volume(volume, 35)

    return new_state, new_volume

current_state, current_volume = use_music_player(
    current_state, 
    current_volume, 
    increase_operations
    )

# Turn down the volume of the player
def decrease_operations(state: bool, volume: int) -> Tuple[bool, int]:
    new_state = toggle_state(state)
    display_state(new_state)
    new_volume = change_volume(volume, -20)

    return new_state, new_volume

# Using the player
current_state, current_volume = use_music_player(
    current_state,
    current_volume,
    decrease_operations
)

# There's a lot of code, but it's simple:

# In change_volume, the volume changes from 0 to 100 depending
#  on the specified increment, then a new volume value is output. 
# The default volume value is 0 if a negative new_volume value 
# is returned. The same default value is 100 if a value greater 
# than 100 is returned.
# use_music_player is a higher—order function for using the player.
#  It also accepts three arguments, where the values of the current
#  state and volume are occupied by the first two parameters, 
# and the operations operations — to use the values of the current
#  state and volume to create the values of the new state and volume
#  — are passed to the third.
# In the increase_operations, the current volume increases, the 
# state of the player switches.
# In decrease_operations, the current volume decreases, the player
#  state switches.

# Implementing the use_music_player function with 
# the corresponding parameters, we get this output:

# ON: Music player switched on.
# New volume: 35
# OFF: Music player switched off.
# New volume: 15

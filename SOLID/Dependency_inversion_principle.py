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


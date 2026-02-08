"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """The remaining bake time"""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

    
    


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.

def preparation_time_in_minutes(number_of_layers):
    """Calculate the prep time based on the number of layers."""
    return number_of_layers * PREPARATION_TIME
    """The prep in minutes"""
    



#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total minutes spent cooking (prep + bake)."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    """The combination of time"""
    



# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)

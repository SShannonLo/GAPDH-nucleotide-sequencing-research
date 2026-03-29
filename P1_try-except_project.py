### CS 22B Project - P1 Pure function and Try-Except
### Group Name: <Team member names>

##### Project Assignment to Practice Try-Except Exceptions #####
## For this assignment, you will design and implement a small collection of 
# pure functions related to your team's project. 

## Requirements: Be sure that for each function that you meet the requirements  and include:
# - A clear function name
# - Includes at least one parameter
# - Include a docstring and a return statement
# - Is pure and has no side effects
# - For each function, provide at least 1 test cases (eg assert) to show that it works correctly.

##### Function 1: A decision-making function using conditionals #####
## Write a Python function that takes input data and returns a transformed version.

import pandas as pd

df = pd.read_csv("CS22B_GAPDH_AA.csv")

# Apply your function to filter humans
human_rows = df[df["Organism"].apply(is_human)]

print(human_rows)

def is_human(organism):
    """
    Check if the organism is Homo sapiens (Human).

    Parameters:
        organism (str): Organism name.

    Returns:
        bool: True if human, False otherwise.
    """
    return organism == "Homo sapiens (Human)"


# Test case
assert is_human("Homo sapiens (Human)") == True 

##### Function 2: Re-write Exception Handling #####
## Write a Python function that uses if, elif, and/or else to classify or evaluate something.


##### Function 3: A function that uses try-except #####
### Write a function that safely handles invalid input and returns a meaningful result without crashing.


##### Function 4: A function that works with a collection #####
### Write a function that processes a collection (list, tuple, set, or dictionary) and returns a result.


##### Function 5: A function of your own design #####
### Choose one additional useful function for your project.

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

# Applying a function to filter humans
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

def classify_similarity(percent_similarity):
    """
    Classify sequence similarity into conservation levels.
    Parameters:
        percent_similarity (float): Similarity percentage (0–100).
    Returns:
        str: Conservation category.
    """
    if percent_similarity >= 90:
        return "highly conserved"
    elif percent_similarity >= 70:
        return "moderately conserved"
    elif percent_similarity >= 50:
        return "low conserved"
    else:
        return "very low conservation"

# Test case
assert classify_similarity(95) == "highly conserved"

##### Function 3: A function that uses try-except #####
### Write a function that safely handles invalid input and returns a meaningful result without crashing.

def safe_gc_content(sequence):
    """
    Calculate GC content of a DNA sequence safely.
    Parameters:
        sequence (str): A nucleotide sequence.
    Returns:
        float or str: GC content percentage, or an error message if input is invalid.
    """
    try:
        if not isinstance(sequence, str):
            raise TypeError
        seq = sequence.upper().replace(" ", "")
        if len(seq) == 0:
            return "Sequence is empty"
        valid_bases = {"A", "T", "C", "G"}
        if any(base not in valid_bases for base in seq):
            return "Invalid sequence: contains non-DNA characters"
        gc_count = seq.count("G") + seq.count("C")
        return (gc_count / len(seq)) * 100
    except TypeError:
        return "Invalid input: sequence must be a string"

# Test cases
assert safe_gc_content("GCGC") == 100.0
assert safe_gc_content("") == "Sequence is empty"
assert safe_gc_content("ABC") == "Invalid sequence: contains non-DNA characters"
assert safe_gc_content(123) == "Invalid input: sequence must be a string"

##### Function 4: A function that works with a collection #####
### Write a function that processes a collection (list, tuple, set, or dictionary) and returns a result.

def average_gc_content(sequences):
    """
    Calculate the average GC content from a list of DNA sequences.
    Parameters:
        sequences (list): A list of DNA sequences (strings).
    Returns:
        float: Average GC content percentage.
    """
    if len(sequences) == 0:
        return 0.0

    total_gc = 0

    for seq in sequences:
        seq = seq.upper()
        gc_count = seq.count("G") + seq.count("C")
        total_gc += (gc_count / len(seq)) * 100

    return total_gc / len(sequences)

# Test case
assert average_gc_content(["GCGC", "ATAT"]) == 50.0

##### Function 5: A function of your own design #####
### Choose one additional useful function for your project.

def percent_similarity(seq1, seq2):
    """
    Calculate the percent similarity between two DNA sequences.

    Parameters:
        seq1 (str): First DNA sequence.
        seq2 (str): Second DNA sequence.
    Returns:
        float: Percentage of matching positions.
    """
    if len(seq1) != len(seq2):
        return "Sequences must be the same length"

    matches = 0

    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            matches += 1

    return (matches / len(seq1)) * 100

# Test case
assert percent_similarity("AAAA", "AAAT") == 75.0

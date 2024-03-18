#!/usr/bin/python3

import json
from difflib import get_close_matches


def load_dictionary():
    """Load dictionary data from a JSON file."""
    with open('data.json') as file:
        dictionary = json.load(file)
    return dictionary


def get_definition(word, dictionary):
    """
    Get the definition of a word from the dictionary.

    Args:
        word (str): The word to search for.
        dictionary (dict): The dictionary containing word definitions.

    Returns:
        str: The definition of the word, or a suggestion if a close match is found.
    """
    # Convert the word to lowercase for case-insensitive search
    word = word.lower()

    # Check if the exact word exists in the dictionary
    if word in dictionary:
        return dictionary[word]

    # Check for title case (e.g., if the user entered "Word" instead of "word")
    if word.title() in dictionary:
        return dictionary[word.title()]

    # Check for uppercase
    if word.upper() in dictionary:
        return dictionary[word.upper()]

    # If the word doesn't exist, suggest similar words using difflib's library
    close_matches = get_close_matches(word, dictionary.keys(), n=1)

    if close_matches:
        # If there are close matches, suggest the first one
        suggestion = close_matches[0]
        # Ask the user if they meant the suggested word
        confirm = input(f"Did you mean '{suggestion}' instead? Enter Y if yes, or N if no: ").lower()
        # Check the user's response
        if confirm == 'y':
            # If the user confirms, return the definition of the suggested word
            return dictionary[suggestion]
        elif confirm == 'n':
            # If the user denies, return a message indicating that the word doesn't exist
            return "The word doesn't exist. Please double check it."
        else:
            # If the user enters an invalid input, return a message asking them to enter 'Y' or 'N'
            return "Invalid input. Please enter 'Y' for yes or 'N' for no."

    return "The word doesn't exist. Please double check it."

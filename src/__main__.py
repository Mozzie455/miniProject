#!/usr/bin/python3

# Import load_dictionary and get_definition from dictionary.py
from src.dictionary import load_dictionary, get_definition


def main():
    # Load the dictionary data
    dictionary = load_dictionary()
    while True:
        word = input("Enter a word to search for its definition (or type 'exit' to quit): ")
        # If the user wants to exit
        if word.lower() == 'exit':
            break
        # Get definition of the word
        definition = get_definition(word, dictionary)
        # Print the results to the user
        print(definition)


# Execute the main function if the script is run directly
if __name__ == '__main__':
    main()

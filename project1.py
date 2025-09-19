'''
Language Python 3

IDE - vscode

Names- Ethan Hillebrand, Rashmika Srivastava

Date started: 9/10/2025
major revision dates: 9/11/2025, 9/12/2025, 9/16/2025 
submission date: 9/19/2025

CS 4500-001-10567, Fall 2025

What the program is designed to do:
File searching program. Gets a valid text file from user and allows user to search for legal
words in the file, then prints a summary of words searched for
Description:
# This program prompts the user to enter a valid `.txt` file from the current directory.
# It reads the file contents and extracts all valid words (alphabetic sequences with optional internal hyphens).
# The user is then allowed to repeatedly enter "LegalWords" (letters and hyphens only),
# and the program counts and displays how many times the word occurs in the file.
# When the user is done, a summary of all searched words and their frequencies is displayed.
#
# Central Data Structures:
# - list_of_words: A list that stores all valid words extracted from the input file, converted to lowercase.
# - searched_words: A dictionary mapping each LegalWord entered by the user to its count in the file.
#
# External Files Used:
# - A user-provided .txt file containing text to be analyzed. This file must be located in the same directory
#   as the script, and must have a `.txt` extension (case-insensitive).
#
# Outside Resources Used:
# 1. Stack Overflow – Regex for hyphenated words inside text
#    - https://stackoverflow.com/questions/61685026/regex-to-match-words-including-hyphenated-ones
#    - Helped develop the regular expression pattern used to match words with optional internal hyphens.
#
# 2. Python Docs – os.path.splitext and os.path.exists
#    - https://docs.python.org/3/library/os.path.html
#    - Used to validate file extensions and check for file existence.
#
# 3. Python Docs – re.findall
#    - https://docs.python.org/3/library/re.html#re.findall
#    - Used to extract all matching word patterns from each line of text.
#
# 4. Stack Overflow – Strip newline characters from text lines
#    - https://stackoverflow.com/questions/275018/how-can-i-remove-a-trailing-newline
#    - Helped refine line processing to properly handle line endings.
#
# 5. Stack Overflow – Detect and handle hyphenated line continuations
#    - https://stackoverflow.com/questions/1398986/reading-a-text-file-line-by-line-and-concatenating-lines-that-end-with-a-hyphe
#    - Inspired logic for joining
'''

import os
import re

# ----------------------------------------------------------------------------------------------
# Requirement 1: Print program introduction
print("This program asks you to enter a valid .txt file from the current directory.\n")

valid_name = False
valid_directory = False

# ----------------------------------------------------------------------------------------------
# Requirement 2: LOOP until a valid filename is entered
while not (valid_name and valid_directory):
    filename = input("Enter a text file: ")

    # 2.b IF filename does not end with ".txt"
    extension = os.path.splitext(filename)[1]
    if extension.lower() != ".txt":
        print("Error: filename must end with .txt")
        continue  # reprompt

    valid_name = True
    print("Valid file extension.")

    # 2.c IF file does not exist in current directory
    if os.path.exists(filename):
        valid_directory = True
        print("File exists.")
    else:
        print("Error: file not found in this directory.")
        valid_directory = False

# ----------------------------------------------------------------------------------------------
# Requirement 3: Initialize ListOfWords and process file
list_of_words = []

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    line = lines[i].rstrip("\n")

    # 4.a IF line ends with a hyphen (with no space before): join with next line
    if line.rstrip().endswith("-") and not line.rstrip().endswith(" -"):
        line = line.rstrip()
        line = line[:-1]  # remove trailing hyphen
        if i + 1 < len(lines):
            next_line = lines[i + 1].lstrip()
            combined_line = line + next_line
            lines[i + 1] = combined_line
    else:
        # 4.b + 4.c + 4.d Use regex to extract valid words (letters + internal hyphens only)
        words = re.findall(r"\b[a-zA-Z]+(?:-[a-zA-Z]+)*\b", line)
        for word in words:
            list_of_words.append(word.lower())
    i += 1

# ----------------------------------------------------------------------------------------------
# Requirement 5: Initialize WordCounts as empty dictionary
searched_words = {}

# ----------------------------------------------------------------------------------------------
# Requirement 6: LOOP user interaction
def is_legal_word(word):
    allowed_chars = set("abcdefghijklmnopqrstuvwxyz-")
    for index, char in enumerate(word.lower()):
        if char not in allowed_chars:
            return False, index, char
    return True, None, None

while True:
    # 6.a Prompt user to enter a word
    print("\nPlease enter a LegalWord (only letters and hyphens allowed, no spaces):")
    user_input = input("LegalWord: ").strip()

    # 6.b Validate user input
    legal, bad_index, bad_char = is_legal_word(user_input)
    if not legal:
        print(f"Error: Illegal character '{bad_char}' at position {bad_index + 1}. Please try again.")
        continue

    # 6.c Convert to lowercase and 6.d count in ListOfWords
    legal_word = user_input.lower()
    count = list_of_words.count(legal_word)

    # 6.e Display result
    print(f"\nThe word '{user_input}' appears {count} time(s) in the file.\n")

    # 6.f Store in WordCounts
    searched_words[user_input] = count

    # ------------------------------------------------------------------------------------------
    # 6.g Ask user if they want to continue
    while True:
        answer = input("Do you want to search for another word? (Yes/No): ").strip().lower()
        if answer in ["yes", "y"]:
            break  # continue outer loop
        elif answer in ["no", "n"]:
            # ----------------------------------------------------------------------------------
            # Requirement 7: Print summary of searched words
            print("\n--- Summary of Searched Words ---")
            for word, cnt in searched_words.items():
                print(f"{word} : {cnt}")

            # ----------------------------------------------------------------------------------
            # Requirement 8: Print exit message
            print("\nThank you for using SG0.")

            # Requirement 9: Wait for user to press ENTER
            input("Press ENTER to exit.")

            # Requirement 10: End program
            exit()
        else:
            print("Invalid input. Please enter Yes, No, Y, N, y, or n.")
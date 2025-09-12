
import os
import re

# Print program introduction
print("This program asks you to enter a valid .txt file from the current directory.\n")

valid_name = False
valid_directory = False

# Loop until both a valid name and directory are given
while not (valid_name and valid_directory):
    filename = input("Enter a text file: ")

    # Check valid file name
    extension = os.path.splitext(filename)[1]
    if extension.lower() != ".txt":
        print("Error: filename must end with .txt")
        continue  # reprompt

    valid_name = True
    print("Valid file extension.")

    # Check if file exists
    if os.path.exists(filename):
        valid_directory = True
        print("File exists.")
    else:
        print("Error: file not found in this directory.")
        valid_directory = False

# ----------------------------------------------------------------------------------------------
#  Requirement 2: Read file and extract words into list_of_words
list_of_words = []

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    line = lines[i].rstrip("\n")

    # If line ends with hyphen (no space before it), join with next line
    if line.rstrip().endswith("-") and not line.rstrip().endswith(" -"):
        line = line.rstrip()
        line = line[:-1]  # remove trailing hyphen
        if i + 1 < len(lines):
            next_line = lines[i + 1].lstrip()
            combined_line = line + next_line
            lines[i + 1] = combined_line
    else:
        # Use regex to find valid words with internal hyphens
        words = re.findall(r"\b[a-zA-Z]+(?:-[a-zA-Z]+)*\b", line)
        for word in words:
            list_of_words.append(word.lower())
    i += 1

# ----------------------------------------------------------------------------------------------
#  Requirement 3: Input and validate LegalWord
def is_legal_word(word):
    allowed_chars = set("abcdefghijklmnopqrstuvwxyz-")
    for index, char in enumerate(word.lower()):
        if char not in allowed_chars:
            return False, index, char
    return True, None, None

# Dictionary to store searched words and their counts
searched_words = {}

# Start user interaction loop
while True:
    print("\nPlease enter a LegalWord (only letters and hyphens allowed, no spaces):")
    user_input = input("LegalWord: ").strip()

    legal, bad_index, bad_char = is_legal_word(user_input)
    if not legal:
        print(f"Error: Illegal character '{bad_char}' at position {bad_index + 1}. Please try again.")
        continue

    legal_word = user_input.lower()
    count = list_of_words.count(legal_word)
    print(f"\nThe word '{user_input}' appears {count} time(s) in the file.\n")

    searched_words[user_input] = count

    # ------------------------------------------------------------------------------------------
    #  Requirement 4: Ask if the user wants to continue
    while True:
        answer = input("Do you want to search for another word? (Yes/No): ").strip().lower()
        if answer in ["yes", "y"]:
            break  # Continue outer loop
        elif answer in ["no", "n"]:
            # Print summary
            print("\n--- Summary of Searched Words ---")
            for word, cnt in searched_words.items():
                print(f"{word} : {cnt}")
            print("\nThank you for using SG0.")
            input("Press ENTER to exit.")
            exit()
        else:
            print("Invalid input. Please enter Yes, No, Y, N, y, or n.")

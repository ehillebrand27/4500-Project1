
import os
import re

#Print program introduction
print("This program asks you to enter a valid .txt file from the current directory.\n")

valid_name = False
valid_directory = False

#Loop until both a valid name and directory are given
while not (valid_name and valid_directory):
    filename = input("Enter a text file: ")

    #check valid file name
    extension = os.path.splitext(filename)[1]
    if extension.lower() != ".txt":
        print("Error: filename must end with .txt")
        continue  # reprompt

    valid_name = True
    print("Valid file extension.")

    #check if file exists
    if os.path.exists(filename):
        valid_directory = True
        print("File exists.")
    else:
        print("Error: file not found in this directory.")
        valid_directory = False
#----------------------------------------------------------------------------------------------
list_of_words = []

f = open(filename, "r")

#Loop over file, transform it, add valid words to list_of_words 
with open(filename, "r") as f:
    for line in f:
        #Remove punct
        cleaned = re.sub(r"[^a-zA-Z0-9\s-]", "", line)
        #split into words using space as separator
        #Convert to lowercase
        #Add to list_of_words
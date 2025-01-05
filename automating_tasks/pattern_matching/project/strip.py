#! python3
# strip.py - Take a string and does the same thing as the strip() method.

import re


# Write a function that takes a string and does the same thing as the strip() method.
# If no other arguments are passed other than the string to strip, then use whitespace.
# Otherwise the second argument to the function is used to strip from the string.
def stripImplementation(string, char=""):
    if char == "":
        return re.sub(r"^\s+|\s+$", "", string)
    else:
        char = re.escape(char)
        return re.sub(f"^{char}+|{char}$", "", string)


string = input("Enter string to strip: ")
char = input("Enter a char to strip in the string: ")
print(stripImplementation(string, char))

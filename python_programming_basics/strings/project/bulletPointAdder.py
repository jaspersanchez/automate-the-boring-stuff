#! python3
"""
bulletPointAdder.py - Adds Wikipedia bullet points to the start
of each line of text on the clipboard.
"""

import pyperclip

text = pyperclip.paste()

# Separate lines and at starts.
line = text.split("\n")
for i in range(len(line)):  # loop through all indexes in the "lines" list
    line[i] = "* " + line[i]  # add a star to each string in "lines" list
text = "\n".join(line)
pyperclip.copy(text)

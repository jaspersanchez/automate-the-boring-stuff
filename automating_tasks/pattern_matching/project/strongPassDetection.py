#! python3
"""
strongPassDetection.py - a program that uses regular expressions to make 
                         sure the password string it is passed is strong.
"""

import re

passRegex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$")


def strongPasswordDetection(password):
    isStrong = passRegex.match(password)
    if isStrong:
        print("The password you made is strong.")
    else:
        print("The password you made is weak.")


password = input("Enter desired password: ")
strongPasswordDetection(password)

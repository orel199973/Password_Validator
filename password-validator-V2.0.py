# !/usr/bin/python

# Attracting models that will help us build the script more easily.
import sys
import re
import colorama
from colorama import Fore

colorama.init()

# argv pulls the user input from the outside and puts it into the "pswd" e variable using the sys module.
pswd = sys.argv[1]
# This is a test condition if we use a flag. 
if pswd == "-f":
    pswd=open(sys.argv[2], 'r').read()
# Here we define our password policy using regular expressions using the re module.
reg = "^(?=.[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{10,}"
match_re = re.compile(reg)
res = re.search(match_re, pswd)

# These are the conditions that will check and print us the correct output.
if res:
    print(pswd)
    print(Fore.GREEN + "- Succeeded, The password is very strong(0)")
else:
    print(pswd)
    print(Fore.RED + "- Weak password, Be sure to follow this password policy:\n(enter 10+ characters, use special characters, numbers and uppercase and lowercase letters).(1)")

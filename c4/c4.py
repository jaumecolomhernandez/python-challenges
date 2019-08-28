#!/usr/bin/env python3

# # When we click the image it takes us to http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345 
# # and we see and the next nothing is 44827. Then if you replace 12345 for the 44827 you 
# # get a new page with a different number. So here clearly we have to keep going until we 
# # find no number...

from urllib.request import urlopen
import re

base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
next_num = 12345
while True:
    try:
        next_num = re.findall(r'[0-9]+', urlopen(base_url+str(next_num)).read().decode())[0]
    except:
        print(f"Current number: {next_num}")
        print(urlopen(base_url+str(next_num)).read())
        break

# # So we do as it says...
next_num = 16044//2
while True:
    try:
        next_num = re.findall(r'[0-9]+', urlopen(base_url+str(next_num)).read().decode())[0]
    except:
        print(f"Current number: {next_num}")
        print(urlopen(base_url+str(next_num)).read())
        break

# # So next go to none and see...
next_num = "none"
while True:
    try:
        next_num = re.findall(r'[0-9]+', urlopen(base_url+str(next_num)).read().decode())[0]
    except:
        print(f"Current number: {next_num}")
        print(urlopen(base_url+str(next_num)).read())
        break
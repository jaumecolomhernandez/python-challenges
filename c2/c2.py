#!/usr/bin/env python3

# # Inspecting the source code we see that there is a huge string of strange symbols 
# # and some letters. First step is to get that in a var.
from urllib.request import urlopen
import re

html=urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
# Since the string is surrounded by comment symbols we can regex that
input_string = re.findall(r'<!--[^-->]*-->',str(html))[0][5:-3]
# Two line sample
print(input_string[:160])

# # Then we keep only the letters and see what we get
sol=""
for ch in input_string:
    n = ord(ch)
    if (n>96) and (n<123):
        sol += ch
print("Solution: ")
print(sol)
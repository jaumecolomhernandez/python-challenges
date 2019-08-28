#!/usr/bin/env python3

# # Looking at see source code we see something similar to the previous challenge, 
# # a huge string in the comments. First step get that in a var.

from urllib.request import urlopen
import re

html=urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
# Since the string is surrounded by comment symbols we can regex that
input_string = re.findall(r'<!--[^-->]*-->',str(html))[0][5:-3]
# Two line sample
print(input_string[:160])

# # The next is to look for exactly what the hint says, look for a lower 
# # case letter surrounded by 3 upper case words.
import re
matches = re.findall(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', input_string)[:][4]
print([res[4] for res in matches])
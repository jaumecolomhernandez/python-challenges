#!/usr/bin/env python3

# # Here there are two tricks, the first is to realize that peak hell sounds like pickle 
# # and that's a python library used for object serialization.
# # The second is to check the source code and see that there's the line <peakhell src="banner.p"/>
# # which suggests going to banner.p and see what we get. In fact we get a file that we can 
# # open with the pickle library.
from urllib.request import urlopen
import pickle

con = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(con)

# # The result is a 95x23 matrix expressed in a run length enconding, 
# # we can try to print it and see what we get...
st = ""
for line in data:
    for char in line:
        st += char[0]*char[1]
    st += "\n"
print(st)
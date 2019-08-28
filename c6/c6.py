#!/usr/bin/env python3

# # The first idea is to change the url ending for .zip, so it downloads a zip.
import urllib.request 
urllib.request.urlretrieve("http://www.pythonchallenge.com/pc/def/channel.zip", "channel.zip")

# # There's a readme file:
from zipfile import ZipFile
# Load file and read readme
with ZipFile('channel.zip') as myzip:
    with myzip.open('readme.txt') as myfile:
        print(myfile.read().decode())

# # This is like the previous challenge where you have to keep going until 
# # you find the final url. So we do as before...
import re
# Recursive opening of files
with ZipFile('channel.zip') as myzip:
    file_name = "90052.txt"
    while True:
        myfile = myzip.open(file_name)
        file_content = myfile.read().decode()
        try:
            file_name = re.findall(r'[0-9]+', file_content)[0]+".txt"
        except:
            print(file_content)
            break

# # Reading about the zip standard you see that there is a header field for comments 
# # in every file compressed in a zip, so maybe reading them and printing in the 
# # order that the tell the files will get us the message...
import re
# Recursive opening of files
with ZipFile('channel.zip') as myzip:
    file_name = "90052.txt"
    while True:
        myfile = myzip.open(file_name)
        file_content = myfile.read().decode()
        try:
            file_name = re.findall(r'[0-9]+', file_content)[0]+".txt"
            print(myzip.getinfo(file_name).comment.decode(), end="")
        except:
            break

# # We are not done yet, when visiting hockey.html appears the next:
from urllib.request import urlopen
print(urlopen("http://www.pythonchallenge.com/pc/def/"+"hockey.html").read().decode())

# # So guessing a little, we get to oxygen.html
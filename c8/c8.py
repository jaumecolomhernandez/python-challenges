#!/usr/bin/env python3

# CHALLENGE 8 - WORKING HARD?
# Link -> http://www.pythonchallenge.com/pc/def/integrity.html

# # When clicking the bee in the photo a prompt appears asking for user and 
# # password. And reading the source we see a user and password in a weird format...

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

# # Reading around you learn that if a file starts with BZ it is compressed with 
# # bzip2. And Python has a module for it in the stl, so let's try
import bz2
print(bz2.decompress(un))
print(bz2.decompress(pw))

# When entering the user and password to the prompt it takes you to the next challenge.
#!/usr/bin/env python3

# CHALLENGE 12 - DEALING EVIL
# Link -> http://www.pythonchallenge.com/pc/return/evil.html

# # This is the hardest challenge in my opinion, the frustration level was hilarius, anyway
# # we got it done. 
# # The first trick is to realize that there are multiple photos, because the photo in the 
# # html page is `evil1.jpg` then there exists `evil2.jpg` and `evil3.jpg`.
# # The second photo suggests that the file format is wrong and that it is gfx. In effect, 
# # changing the ending provides us with a new file in an obscure format...
f = open('evil2.gfx','rb').read()
print(f[:600])

# # Then here it comes the difficult trick, you have to realize that it contains 5 
# # different files interspersed in the bytes of the .gfx. 
# # How did I realize this? by looking for what file format header matched the first 
# # pixels of the file, I got results for the PNG format. In this one the header looks
# # like this(hex) -> `89 50 4E 47` and the three latter bytes are `PNG` in ASCII. So 
# # trying to look for ASCII in the bytes of the .gfx you see that they are 5 bytes away.
# # Then you match this idea with the evil1.jpg photo, in the photo there appear 5 
# # decks so now you can infere that you have to sort the data in 5 new "decks"/files and 
# # see the new images.

ar = list()
for i in range(5):
    data = f[i::5]
    ar.append(data)
    open(f'{i}.jpg', 'wb').write(data)

# # In the images appears the word disproportional
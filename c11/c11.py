#!/usr/bin/env python3

# CHALLENGE 11 - ODD EVEN
# Link -> http://www.pythonchallenge.com/pc/return/5808.html

from PIL import Image
import numpy as np
im = Image.open('cave.jpg').convert('L')
mat = np.array(im)

Image.fromarray(mat[::2,::2], 'L')

# # And looking at the top right we see evil. If you don't see it download the image 
# # and max the brightness and there it will appear.
#!/usr/bin/env python3

from PIL import Image
import numpy as np
im = Image.open('cave.jpg').convert('L')
mat = np.array(im)

Image.fromarray(mat[::2,::2], 'L')

# # And looking at the top right we see evil. If you don't see it download the image 
# # and max the brightness and there it will appear.
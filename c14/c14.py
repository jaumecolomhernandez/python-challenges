#!/usr/bin/env python3

# CHALLENGE 14 - WAlk AROUND
# Link -> http://www.pythonchallenge.com/pc/return/italy.html

from PIL import Image
import numpy as np

im = Image.open('wire.png').convert('L')
mat = np.array(im)
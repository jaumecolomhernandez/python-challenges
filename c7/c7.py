#!/usr/bin/env python3

# # In this challenge the first that comes to mind is to read the grayscale values 
# # from the middle line and decode it as ascii and see what we get.
# # Doing a bit of analysis with any image processing software we see that the squares are
# # 7 pixels wide and that the line ends at the 610 pixel, se we select that range to 
# # analyze it.
from PIL import Image
import numpy as np

im = Image.open('oxygen.png').convert('L')
mat = np.array(im)

selected = mat[48][2:610:7]

for i in range(len(selected)):
    print(chr(selected[i]), end="")

# # So we decode the same way as before...
result = [105, 110, 116, 101, 103, 114, 105, 116, 121]

for ch in result:
    print(chr(ch), end="")
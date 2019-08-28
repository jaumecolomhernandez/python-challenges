#!/usr/bin/env python3

from PIL import Image
import numpy as np

im = Image.open('wire.png').convert('L')
mat = np.array(im)
#!/usr/bin/python

import sys
from io import BytesIO
import numpy as np
import cv2
from image_final_crop import return_cropped_image

def read_image(file):
    image_stream = BytesIO(file)
    image = cv2.imdecode(np.frombuffer(image_stream.read(), np.uint8), 1)
    return image

file = open(sys.argv[1], "rb")
image = read_image(file.read())
cropped = return_cropped_image(image)

cv2.imwrite(sys.argv[2], cropped)

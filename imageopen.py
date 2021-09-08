import cv2
import imageio
import numpy as np

filename = 'image.png'
im = cv2.imread(filename)
height, width, depth = im.shape
oim = im.copy()

while True:
    for i in range(100):
        r = np.random.randint(height)
        c = np.random.randint(width)

        oim[r, c, :] = 255 - im[r, c, :]

    cv2.imshow('winname', oim)
    if (cv2.waitKey(10) == 27):
        break

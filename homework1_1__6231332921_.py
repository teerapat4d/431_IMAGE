# import library here
import cv2
import numpy as np
import matplotlib.pyplot as plt


def piecewise(pix, r1, s1, r2, s2):
    #for i in range(pix.shape[0]):
        if 0 <= pix <= r1:
            filtered_image = (s1 / r1) * pix
        elif r1 < pix <= r2:
            filtered_image = ((s2 - s1) / (r2 - r1)) * pix + s1
        else:
            filtered_image = ((l - 1 - s2) / (l - 1 - r2)) * pix + s2
        return filtered_image


    # input -> image_grayscale - type -> np.ndarray, size of - (height, width)
    # output -> image_grayscale - type -> np.ndarray, size of - (height, width)
    # TO DO - Implement transformation based on the contrast stretching graph
path = 'E:/64/Semester_1/431_Image/pic_source/prayut.jpg'
image = cv2.imread(path)
image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
l = 256
s1 = 0.125 * l
s2 = 0.875 * l
r1 = 0.375 * l
r2 = 0.625 * l

pixelval_vec = np.vectorize(piecewise)
output = pixelval_vec(image_grayscale,r1,s1,r2,s2)
plt.imshow(output,cmap='gray')
plt.show()

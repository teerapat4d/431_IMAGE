# import library here
import cv2
import numpy as np
import matplotlib.pyplot as plt
# Open the image.
path = 'E:/64/Semester_1/431_Image/pic_source/prayut.jpg'
img = cv2.imread(path)
# Trying 4 gamma values.
gamma = 0.5
gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
plt.imshow(gamma_corrected)
plt.show()

# Subtract the img from max value(calculated from dtype)
img_neg = 255 - img
# Show the image
plt.imshow(img_neg)
plt.show()
# -*- coding: utf-8 -*-
"""HWCLOCK.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11EjWrLWm6OtMaV5jce5j9Ft9lXUB0Ht8

## LIBRARY IMPORT
"""

import cv2
import math
import numpy as np
import matplotlib.pyplot as plt

def L2_norm(x1, y1, x2, y2):
    print("L2_norm", np.sqrt((x1 - x2)**2 + (y1 - y2)**2))
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def maxim_distance(center, clock_hand):
    if L2_norm(center[0], center[1], clock_hand[0], clock_hand[1]) > L2_norm(center[0], center[1], clock_hand[2], clock_hand[3]):
        return clock_hand[0], clock_hand[1]
    else:
        return clock_hand[2], clock_hand[3]

def get_angle_between_points(x_orig, y_orig, x_hand, y_hand):
    delta_x = x_hand - x_orig
    delta_y = y_hand - y_orig
    return (math.atan2(delta_y, delta_x) * 180) / math.pi

def angle_to_hours(clock_center, point):
    angle = get_angle_between_points(clock_center[0], clock_center[1], point[0], point[1])
    if angle <= 0 and angle >= -90:
        angle = 90 + angle
    elif angle < -90 and angle >= -180:
        angle = 450 + angle
    elif angle > 0:
        angle = 90 + angle
    return angle

def minutes(angle):
    return (angle * 5) // 30

def hours(angle, min):
    h = angle / 30
    if (math.ceil(h) < h + 0.5) and min < 30:
        return math.ceil(h)
    else:
        return math.floor(h)

"""# ดฟแ

"""

img = cv2.imread("clock_4.png", 0)

w,h = img.shape

r_in = 12**2
r_out = 140**2

for x in range(w):
  for y in range(h):
    k = (x-w//2)**2+(y-h//2)**2
    if (k > r_out or k < r_in):
      img[x,y] = 255

plt.imshow(img, cmap='gray')
plt.show()

edges = cv2.Canny(img, 50, 150, apertureSize=3)


plt.imshow(edges, cmap='gray')
plt.show()

# lines = cv2.HoughLines(edges, 10, np.pi/180, 140)
min_line_length = 0
min_line_gap = 0
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 30, min_line_length, min_line_gap)
line_length = {}
number_of_line = 0

for line in lines:
  #print(line[0])
  x1, y1, x2, y2 = line[0]
  dist = L2_norm(x1, y1, x2, y2)
  line_length.update({number_of_line: dist})
  number_of_line += 1
  cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Sort lines ascending(by length)
sorted_line = sorted(line_length.items(), key=lambda item: item[1])
# Compute the mean for hour and minute hand
hour_hand   = (lines[sorted_line[0][0]][0] + lines[sorted_line[1][0]][0]) // 2
minute_hand = (lines[sorted_line[2][0]][0] + lines[sorted_line[3][0]][0]) // 2


center = [img.shape[0]/2,img.shape[1]/2]
# Get the farthest point on each clock hand
hour_hand_max = maxim_distance(center, hour_hand)
minute_hand_max = maxim_distance(center, minute_hand)

# Calculate minutes and hours
m = minutes(angle_to_hours(center, minute_hand_max))
h = hours(angle_to_hours(center, hour_hand_max), m)

print("Hour: {} minute: {}".format(h, m))
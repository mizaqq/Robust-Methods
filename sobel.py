# -*- coding: utf-8 -*-
import cv2
import numpy as np
# Load image in grayscale
img = cv2.imread('circle.jpg', cv2.IMREAD_GRAYSCALE)

# Define Sobel kernels
Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
Gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])



# Apply Sobel operator to image using NumPy
edge_x = np.abs(np.convolve(img.flatten(), Gx.flatten(), mode='same').reshape(img.shape))
edge_y = np.abs(np.convolve(img.flatten(), Gy.flatten(), mode='same').reshape(img.shape))


for x in range(0, 255):
    for y in range(0, 255):
        vgx = 0
        for j in range(-1, 2):
            for i in range(-1, 2):
                vgx += j * (x - i) * Gx[i, j]

# Rest of your code goes here (if applicable)

# Compute magnitude and direction of edges
mag = np.sqrt(edge_x ** 2 + edge_y ** 2)
angle = np.arctan2(edge_y, edge_x) * 180 / np.pi

# Display results
#cv2.imshow('img',img)
#cv2.waitKey(0)
#cv2.imshow('edge_x',edge_x)
#cv2.imshow('edge_y',edge_y)
#cv2.imshow('mag',mag)
#cv2.imshow('angle',angle)
#cv2.waitKey(0)

x_range = (0, img.shape[1])  # Range of x coordinates
y_range = (0, img.shape[0])  # Range of y coordinates
r_range = (500, 800)  # Range of radii
# Set the resolution for each parameter
x_resolution = 1
y_resolution = 1
r_resolution = 1
# Calculate the dimensions of the accumulator array
x_dim = int((x_range[1] - x_range[0]) / x_resolution) + 1
y_dim = int((y_range[1] - y_range[0]) / y_resolution) + 1
r_dim = int((r_range[1] - r_range[0]) / r_resolution) + 1

accumulator = np.zeros((x_dim, y_dim, r_dim), dtype=np.uint64)
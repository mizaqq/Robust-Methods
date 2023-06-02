import cv2
import numpy as np
import linesht as lht

img = cv2.imread('./pictures/line.jpg', cv2.IMREAD_GRAYSCALE)
Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
Gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

edge_x = np.abs(np.convolve(img.flatten(), Gx.flatten(), mode='same').reshape(img.shape))
edge_y = np.abs(np.convolve(img.flatten(), Gy.flatten(), mode='same').reshape(img.shape))

mag = np.sqrt(edge_x ** 2 + edge_y ** 2)

lines = lht.find_lines(img,mag,150,200)
lht.printlines(img,lines)

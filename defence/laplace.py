import numpy as np
import random
import cv2


def simple_laplace(x):
    return np.exp(-np.abs(x))


def get_random(x:int) -> int:
    now = random.uniform(-5, 5)
    return (simple_laplace(now)*100 + x) % 255



img = cv2.imread('pic.png', cv2.IMREAD_GRAYSCALE)
row, col = img.shape

for i in range(row):
    for j in range(col):
        # print(img[i,j], end=' ')
        img[i, j] = get_random(img[i, j])

cv2.imwrite('output.png', img)
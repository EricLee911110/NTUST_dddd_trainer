import numpy as np
import random
import cv2
from typing import Union


def laplace(random: int, delta: Union[float, int], epsilon: Union[float, int]):
    b = delta / epsilon
    # print(delta, epsilon, b)
    return 1 / (2*b) * np.exp(-np.abs(random)/b)


def add_noise(x: int):
    now = random.random()
    delta, epsilon = 1, 1
    return (now, laplace(now, delta, epsilon))
    # return (simple_laplace(now)*100 + x) % 255


# img = cv2.imread('pic.png', cv2.IMREAD_GRAYSCALE)
# row, col = img.shape

# for i in range(row):
#     for j in range(col):
#         img[i, j] = get_random(img[i, j])

# cv2.imwrite('dp_output.png', img)
for i in range(10):
    print(add_noise(i))


import numpy as np
import cv2
from pixelate import pixelate
from PIL import Image


def gaussian(filename: str, ksize: int) -> None:
    filename = 'pic.png'
    img = cv2.imread(filename)
    return cv2.GaussianBlur(img, (ksize, ksize), 0)    # kernel size i*i
    cv2.imwrite(f'{filename[:-4]}_blur_{i}x{i}.png', output1)


def pixelize(filename: str, pixel_size: int) -> Image:
    with Image.open(filename) as image:
        
        image = image.resize(
            (image.size[0] // pixel_size, image.size[1] // pixel_size),
            Image.NEAREST
        )
        image = image.resize(
            (image.size[0] * pixel_size, image.size[1] * pixel_size),
            Image.NEAREST
        )
        
        return image


def dp_pixelize(img: Image, ex: int):
    epsilon = pow(10, ex)
    b = img.width * img.height  # b * b grid cell
    m = b  # most m pixels can thus be protected
    sensitivity = 255*m/(b*b)
    for x in range(img.width):
        for y in range(img.height):
            new = tuple([int(value + np.random.laplace(0, sensitivity/epsilon))
                         for value in img.getpixel((x, y))])
            img.putpixel((x, y), new)
    return img


def dp_blur(img: cv2.Mat, ex: float):
    epsilon = 700
    m = 1  # most m pixels can thus be protected
    sensitivity = 255*m
    rows, cols, _ = img.shape
    for x in range(rows):
        for y in range(cols):
            img[x][y] = [min(255, int(value + np.random.laplace(0, sensitivity/epsilon)))
                         for value in img[x][y]]
            # new = [int(value + np.random.laplace(0, sensitivity/epsilon))
            #        for value in img[x][y]]
            # print(new)
    return img


if __name__ == '__main__':
    filename = 'pic.png'

    # DP-pixel
    ex = [-2, -3, -4, -5]
    for e in ex:
        pixel_size = [1,1,1]
        for i in pixel_size:
            img = pixelize(filename, i)
            img = dp_pixelize(img, e)
            img.save(f'dp-pixel {i}x{i}({e}).png')

    # DP-blur
    # ex = [5, 7, 9]
    # for e in ex:
    #     kernel_size = [3, 5, 7, 9]
    #     for i in kernel_size:
    #         img = gaussian(filename, i)    # kernel size i*i
    #         img = dp_blur(img, e)
    #         cv2.imwrite(f'dp-blur {i}x{i}({e}).png', img)
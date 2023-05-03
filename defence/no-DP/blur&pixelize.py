import cv2
from pixelate import pixelate


def gaussian(filename: str) -> None:
    filename = 'pic.png'
    img = cv2.imread(filename)
    kernel_size = [3, 5, 7, 9]
    for i in kernel_size:
        output1 = cv2.GaussianBlur(img, (i, i), 0)    # kernel size i*i
        cv2.imwrite(f'{filename[:-4]}_blur_{i}x{i}.png', output1)


def pixelize(filename: str) -> None:
    pixel_size = [2, 4, 8, 16]
    for i in pixel_size:
        pixelate(filename, f'{filename[:-4]}_pixelize_{i}x{i}.png', i)


if __name__ == '__main__':
    filename = 'pic.png'
    gaussian(filename)
    pixelize(filename)

import cv2
import numpy as np
from pixelate import pixelate
import os
from PIL import Image
from tqdm import tqdm

def gaussian(filename: str, dir) -> None:
    img = cv2.imread(f'{dir}/{filename}')
    kernel_size = [15, 45, 99]
    for i in kernel_size:
        try:
            output1 = cv2.GaussianBlur(img, (i, i), 0)    # kernel size i*i
            cv2.imwrite(f'ntust/B{i}x{i}_val/{filename}', output1)
        except:
            id = filename.split('_')[0]
            print(f'an error occurred in blur {i}x{i}: {id}')

def pixelize(filename: str, dir) -> None:
    pixel_size = [2,4,8]
    for i in pixel_size:
        try:
            pixelate(f'{dir}/{filename}', f'ntust/P{i}x{i}/{filename}', i)
        except:
            id = filename.split('_')[0]
            print(f'an error occurred in pixelize {i}x{i}: {id}')

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

if __name__ == '__main__':
    dir = 'ntust/ntust_val_10000'
    ex = [-2, -3, -4, -5]
    folders = ['dp-2', "dp-3", "dp-4", "dp-5"]
    for filename in tqdm(os.listdir(dir)):
        for i, e in enumerate(ex):
            file_path = f'{dir}/{filename}'
            with Image.open(file_path) as img:
                img = dp_pixelize(img, e)
                img.save(f'ntust/{folders[i]}_val/{filename}')
    
    """
    for filename in tqdm(os.listdir(dir)):
        gaussian(filename, dir)
        #pixelize(filename, dir)
        pass
    """
    
    """
    folders = ['B3x3','B5x5','B7x7','B9x9','P2x2','P4x4','P8x8']
    for folder in folders:
        os.mkdir(f'ntust/{folder}_val')
        os.mkdir(f'ntust/{folder}')
    """ 

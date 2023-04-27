import cv2
from pixelate import pixelate
import os
from tqdm import tqdm

def gaussian(filename: str, dir) -> None:
    img = cv2.imread(f'{dir}/{filename}')
    kernel_size = [3,5,7,9]
    for i in kernel_size:
        try:
            output1 = cv2.GaussianBlur(img, (i, i), 0)    # kernel size i*i
            cv2.imwrite(f'ntust/B{i}x{i}/{filename}', output1)
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

if __name__ == '__main__':
    dir = 'ntust/ntust_10000'
    for filename in tqdm(os.listdir(dir)):
        gaussian(filename, dir)
        pixelize(filename, dir)
        pass
    
    """
    folders = ['B3x3','B5x5','B7x7','B9x9','P2x2','P4x4','P8x8']
    for folder in folders:
        os.mkdir(f'ntust/{folder}_val')
        os.mkdir(f'ntust/{folder}')
    """ 

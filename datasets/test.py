import os
from tqdm import tqdm

arr = ['B3x3','B5x5','B7x7','B9x9','P2x2','P4x4','P8x8']

for folder in tqdm(arr):
    length = len(os.listdir(f'ntust/{folder}'))
    print(f'{folder} has {length} files')

    #for filename in os.listdir(f'ntust/{folder}'):
    #    os.remove(f'ntust/{folder}/{filename}')
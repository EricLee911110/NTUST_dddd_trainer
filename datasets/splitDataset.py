import os
from tqdm import tqdm
from PIL import Image


#folder_list = ['B3x3','B5x5','B7x7','B9x9','P2x2','P4x4','P8x8']
#folder_list = ['ntust_1200','ntust_1400','ntust_1600']
base_dir = 'ntust/ntust_10000'

file_count = 0
for folder in tqdm(folder_list):
    for filename in os.listdir(base_dir):
        source = f'{base_dir}/{filename}'
        destination = f'ntust/{folder}/{filename}'
        
        img = Image.open(source)
        img.save(destination)
        #print(source)
        #print(destination)
        file_count += 1
        if file_count >= int(folder.split('_')[1]):
            print(file_count)
            file_count = 0
            break

    #for filename in os.listdir(f'ntust/{folder}'):
    #    os.remove(f'ntust/{folder}/{filename}')
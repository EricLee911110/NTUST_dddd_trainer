import os
from PIL import Image
from tqdm import tqdm

source_dirs = ["B3x3", "B5x5", "B7x7", "B9x9", "B15x15", "B45x45", "dp-2", "dp-3", "P2x2"]
target_dir = "combined_datasets"

number_each_folder = 3000

for i, directory in enumerate(source_dirs):
    path = f'ntust/{directory}'
    for ii, file in enumerate(os.listdir(path)):
        try:
            img = Image.open(f'{path}/{file}')
            filename = file.split('.')[0]
            img.save(f'{target_dir}/{filename}_{source_dirs[i]}.png')
        except:
            print(file)
            
        if ii == number_each_folder:
            break
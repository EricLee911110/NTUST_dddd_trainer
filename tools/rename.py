# This python file will delete and rename files by the following rules
# 1. convert "o" to "0"
# 2. if filename contains english letter other than "o", will be deleted
# 3. if the charactor of a filename is less than 5, will be deleted

import os
import uuid

directory = 'Large_Captcha_Dataset'

a = ['g863E', '52953', 'o2441', 'o2dda', '(1123', '12491']
#for e in a:
#    print(e.isnumeric())

progress = 0
print_every = 200

large_captcha_dataset = False
if directory == "Large_Captcha_Dataset":
    large_captcha_dataset = True

o_count = 0
eng_count = 0
five_count = 0

print(f'Going to process {len(os.listdir(directory))} images, please hold')

files = os.listdir(directory)
for filename in files:
    old_file = os.path.join(directory, filename)

    old_predict = filename.split('_')[0].lower()
    new_predict = old_predict.replace('o', '0')
    if large_captcha_dataset:
        new_file = os.path.join(directory, filename)
        new_predict = filename.split('.')[0]
    else:
        id = filename.split('_')[1]
        new_file = os.path.join(directory, f'{new_predict}_{id}')
    
    # replace o to 0
    
    
    if not large_captcha_dataset:
        if "o" in old_predict:
            os.rename(old_file, new_file)
            o_count += 1
    
    # delete if contains not number
    if not new_predict.isnumeric():
        os.remove(new_file)
        eng_count += 1
    else:
        # delete if not contains 5 digits
        if len(new_predict) != 5:
            os.remove(new_file)
            five_count += 1

    if progress % print_every == 0:
        print(f'step: {progress}')
    progress += 1
 

print()
print(f'{o_count} files have renamed becasue of o')
print(f'{eng_count} files have deleted becasue of english letter')
print(f'{five_count} files have deleted becasue of not containing 5 digits')
print()


# Only preform this after you remove the files for once
"""
for i in range(len(files)):
    filename = files[i]
    first_name = filename.split('.')[0]

    old_filename = f'{directory}/{filename}'
    new_filename = f'{directory}/{first_name}_{i}.png'
    
    os.rename(old_filename, new_filename)
"""

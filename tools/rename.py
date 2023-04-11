# This python file will delete and rename files by the following rules
# 1. convert "o" to "0"
# 2. if filename contains english letter other than "o", will be deleted
# 3. if the charactor of a filename is less than 5, will be deleted

import os
import uuid

directory = 'correct_captcha_12000'

a = ['g863E', '52953', 'o2441', 'o2dda', '(1123', '12491']
#for e in a:
#    print(e.isnumeric())

progress = 0
print_every = 200

o_count = 0
eng_count = 0
five_count = 0

print(f'Going to process {len(os.listdir(directory))} images, please hold')

for filename in os.listdir(directory):
    old_file = os.path.join(directory, filename)

    old_predict = filename.split('_')[0].lower()
    new_predict = old_predict.replace('o', '0')
    id = filename.split('_')[1]
    
    # replace o to 0
    new_file = os.path.join(directory, f'{new_predict}_{id}')
    
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
# This python file will delete and rename files by the following rules
# 1. convert "o" to "0"
# 2. if filename contains english letter other than "o", will be deleted
# 3. if the charactor of a filename is less than 5, will be deleted

import os
import uuid

directory = 'correct_captcha_images'
#english_letters = [abcdefghijklmnopqrstuvwxyz]
a = 'g863E'
b = '52953'
c = 'o2441'
d = 'o2dda'

o_count = 0
eng_count = 0
five_count = 0

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
        

    # delete if contains other letter
    if new_predict.islower():
        os.remove(new_file)
        eng_count += 1
    
    if len(new_predict) != 5:
        os.remove(new_file)
        five_count += 1


        

print()
print(f'{o_count} files have renamed becasue of o')
print(f'{eng_count} files have deleted becasue of english letter')
print(f'{five_count} files have deleted becasue of not containing 5 digits')
print()
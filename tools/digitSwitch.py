import os
from PIL import Image
import subprocess

files = os.listdir('wrong_1000')
target_tokens = ['0', '6', '9']

filename = files[1]
number = filename.split('_')[0]
hash_id = filename[len(number) + 1:].split('.')[0]

print(f'origin: {number}')
positions_needs_switch = []
for i in range(len(number)):
    if number[i] in target_tokens:
        positions_needs_switch.append(i)

if len(number) == 5:
    img = Image.open(f'wrong_1000/{filename}')
    
    if len(positions_needs_switch) == 0:
        pass

    if len(positions_needs_switch) == 1:
        for token_a in range(3):
            number_list = list(number)
            number_list[positions_needs_switch[0]] = target_tokens[token_a]
            number = "".join(number_list)
            print(number)

    if len(positions_needs_switch) == 2:
        for token_a in range(3):
            for token_b in range(3):
                number_list = list(number)
                number_list[positions_needs_switch[0]] = target_tokens[token_a]
                number_list[positions_needs_switch[1]] = target_tokens[token_b]
                number = "".join(number_list)
                print(number)
                # feed to php
                result = subprocess.getstatusoutput(f'php spider2.php {hash_id} {number}')
                if result == "true":
                    new_filename = f'wrong_to_correct/{number}_{hash_id}.png'
                    img.save(new_filename)
                    break

    if len(positions_needs_switch) == 3:
        for token_a in range(3):
            for token_b in range(3):
                for token_c in range(3):
                    number_list = list(number)
                    number_list[positions_needs_switch[0]] = target_tokens[token_a]
                    number_list[positions_needs_switch[1]] = target_tokens[token_b]
                    number_list[positions_needs_switch[2]] = target_tokens[token_c]
                    number = "".join(number_list)
                    print(number)
                    result = subprocess.getstatusoutput(f'php spider2.php {hash_id} {number}')[1]
                    print(result)
                    if result == "true":
                        new_filename = f'wrong_to_correct/{number}_{hash_id}.png'
                        img.save(new_filename)
                        print('success!')
                        break

    if len(positions_needs_switch) == 4:
        for token_a in range(3):
            for token_b in range(3):
                for token_c in range(3):
                    for token_d in range(3):
                        number_list = list(number)
                        number_list[positions_needs_switch[0]] = target_tokens[token_a]
                        number_list[positions_needs_switch[1]] = target_tokens[token_b]
                        number_list[positions_needs_switch[2]] = target_tokens[token_c]
                        number_list[positions_needs_switch[3]] = target_tokens[token_d]
                        number = "".join(number_list)
                        print(number)

    if len(positions_needs_switch) == 5:
        for token_a in range(3):
            for token_b in range(3):
                for token_c in range(3):
                    for token_d in range(3):
                        for token_e in range(3):
                            number_list = list(number)
                            number_list[positions_needs_switch[0]] = target_tokens[token_a]
                            number_list[positions_needs_switch[1]] = target_tokens[token_b]
                            number_list[positions_needs_switch[2]] = target_tokens[token_c]
                            number_list[positions_needs_switch[3]] = target_tokens[token_d]
                            number_list[positions_needs_switch[4]] = target_tokens[token_e]
                            number = "".join(number_list)
                            print(number)
                


print(hash_id)
print(positions_needs_switch)
print(len(number))

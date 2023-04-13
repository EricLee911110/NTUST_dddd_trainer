import os 

directory = "ntust_validate_dataset"

# a counter for counting every digits
char_counter = {}

# a counter for counting starting digits
first_char_counter = {}

# a counter for counting duplicate digits in a prediction
different_counter = {}

# a counter for counting number of picture that contains 0,6,9
token = ['0','6','9']
special_counter = 0

for i in range(10):
    char_counter[str(i)] = 0
    first_char_counter[str(i)] = 0
    different_counter[str(i)] = 0


for filename in os.listdir(directory):
    predict = filename.split('_')[0]

    for char in predict:
        if char not in char_counter:
            char_counter[char] = 1
        else:
            char_counter[char] += 1
    
    first_char_counter[predict[0]] += 1

    different_counter[str(len(set(predict)))] += 1

    if token[0] in predict or token[1] in predict or token[2] in predict: 
        special_counter += 1
        print(predict)


    
print()
print("Total number of characters: ")
print(char_counter, end='\n\n')

print("Starting character: ")
print(first_char_counter, end='\n\n')

print("Total number of different character in a prediction")
print(different_counter, end='\n\n')

print(f'Total number of images that appears 069 is: {special_counter}')
print()
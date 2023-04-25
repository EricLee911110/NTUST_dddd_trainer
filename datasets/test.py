import os

delete_files = os.listdir('ntust/wrong_to_correct')
files = os.listdir('ntust/wrong')

print(len(files))
file_count = 0
for file in delete_files:
    hash = "_".join(file.split('_')[1:])
    #print(file)
    #print(hash)
    for file_b in files:
        if hash in file_b:
            file_count += 1
            os.remove(f'ntust/wrong/{file_b}')

files = os.listdir('ntust/wrong')
print(len(files))
print(file_count)



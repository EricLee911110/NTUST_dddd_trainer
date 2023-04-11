import os

a = []
b = []

directory1 = "Large_Captcha_Dataset"
directory2 = "correct_captcha_12000"

files1 = os.listdir(directory1)
files2 = os.listdir(directory2)

for i in range(len(files1)):
    filename = files1[i]
    first_name = filename.split('_')[0]
    a.append(first_name)

for i in range(len(files2)):
    filename = files2[i]
    first_name = filename.split('_')[0]

    if first_name in a:
        print(first_name)
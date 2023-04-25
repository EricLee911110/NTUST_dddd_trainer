import time
import subprocess
import os 

#time_get = time.time()
#hash_id = subprocess.getstatusoutput('php spider2.php')[1]
#print(f'time for get: {time.time() - time_get}')

a = 1
b = 1

"""
for i in range(5):
    if i == 2:
        if a == 1:
            if b == 1:
                for ii in range(5):
                    for iii in range(5):
                        print(i, ii, iii)
                        if ii == 2:
                            break

    print(i)   
"""

files = os.listdir('wrong_1000')
file = files[0]
print(file.split('_'))
predict = "_".join(file.split('_')[:-1])
print(predict)
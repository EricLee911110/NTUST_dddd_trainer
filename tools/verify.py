import os
import ddddocr
import subprocess
from PIL import Image
import time

ocr = ddddocr.DdddOcr(det=False, ocr=True, import_onnx_path="/content/NTUST_dddd_trainer/projects/ntust_mail/models/ntust_mail_para121755_dsunknown_acc1.0_ep4_step1150_2023-04-25-08-59-15.onnx", charsets_path="/content/NTUST_dddd_trainer/projects/ntust_mail/models/charsets.json")
target_tokens = ['0', '6', '9']

def find_correct(predict):
  positions_needs_switch = []
  for i in range(len(predict)):
    if predict[i] in target_tokens:
      positions_needs_switch.append(i)

  if len(predict) == 5:
    #img = Image.open(f'{dir_name}/{predict}_{hash_id}.png')
    if len(positions_needs_switch) == 1:
      for token_a in range(3):
        predict_list = list(predict)
        predict_list[positions_needs_switch[0]] = target_tokens[token_a]
        predict = "".join(predict_list)
        result = subprocess.getstatusoutput(f'php spider2.php {hash_id} {predict}')[1]
        print(predict, result)
        if result == "true":
          new_filename = f'wrong_to_correct/{predict}_{hash_id}.png'
          img.save(new_filename)
          return

    if len(positions_needs_switch) == 2:
      for token_a in range(3):
        for token_b in range(3):
          predict_list = list(predict)
          predict_list[positions_needs_switch[0]] = target_tokens[token_a]
          predict_list[positions_needs_switch[1]] = target_tokens[token_b]
          predict = "".join(predict_list)
          # feed to php
          result = subprocess.getstatusoutput(f'php spider2.php {hash_id} {predict}')[1]
          print(predict, result)
          if result == "true":
            new_filename = f'wrong_to_correct/{predict}_{hash_id}.png'
            img.save(new_filename)
            return

    if len(positions_needs_switch) == 3:
      for token_a in range(3):
        for token_b in range(3):
          for token_c in range(3):
            predict_list = list(predict)
            predict_list[positions_needs_switch[0]] = target_tokens[token_a]
            predict_list[positions_needs_switch[1]] = target_tokens[token_b]
            predict_list[positions_needs_switch[2]] = target_tokens[token_c]
            predict = "".join(predict_list)
            result = subprocess.getstatusoutput(f'php spider2.php {hash_id} {predict}')[1]
            print(predict, result)
            if result == "true":
              new_filename = f'wrong_to_correct/{predict}_{hash_id}.png'
              img.save(new_filename)
              #print('success!')
              return

    if len(positions_needs_switch) == 4:
      for token_a in range(3):
        for token_b in range(3):
          for token_c in range(3):
            for token_d in range(3):
              predict_list = list(predict)
              predict_list[positions_needs_switch[0]] = target_tokens[token_a]
              predict_list[positions_needs_switch[1]] = target_tokens[token_b]
              predict_list[positions_needs_switch[2]] = target_tokens[token_c]
              predict_list[positions_needs_switch[3]] = target_tokens[token_d]
              predict = "".join(predict_list)
              result = subprocess.getstatusoutput(f'php spider2.php {hash_id} {predict}')[1]
              print(predict, result)
              if result == "true":
                new_filename = f'wrong_to_correct/{predict}_{hash_id}.png'
                img.save(new_filename)
                return

    if len(positions_needs_switch) == 5:
      for token_a in range(3):
        for token_b in range(3):
          for token_c in range(3):
            for token_d in range(3):
              for token_e in range(3):
                predict_list = list(predict)
                predict_list[positions_needs_switch[0]] = target_tokens[token_a]
                predict_list[positions_needs_switch[1]] = target_tokens[token_b]
                predict_list[positions_needs_switch[2]] = target_tokens[token_c]
                predict_list[positions_needs_switch[3]] = target_tokens[token_d]
                predict_list[positions_needs_switch[4]] = target_tokens[token_e]
                predict = "".join(predict_list)
                result = subprocess.getstatusoutput(f'php spider2.php {hash_id} {predict}')[1]
                print(predict, result)
                if result == "true":
                  new_filename = f'wrong_to_correct/{predict}_{hash_id}.png'
                  img.save(new_filename)
                  return


correct_count = 0
total_count = 0

for i in range(8000):
  total_count += 1

  print(f'step: {i}')
  time_get = time.time()
  hash_id = subprocess.getstatusoutput('php spider2.php')[1]
  print(f'time for get: {time.time() - time_get}')
  file_name = f'{hash_id}.png'

  with open(file_name, 'rb') as f:
    img_bytes = f.read()

  time_predict = time.time()
  predict = ocr.classification(img_bytes)
  print(f'time for predict {time.time() - time_predict}')

  time_verify = time.time()
  correct_prediction = subprocess.getstatusoutput(f'php spider2.php {hash_id} {predict}')[1]
  print(f'time for verify: {time.time() - time_verify}')

  print(predict)
  print(correct_prediction)

  img = Image.open(file_name)
  if correct_prediction == 'true':
    correct_count += 1
    dir_name = "correct"
    img.save(f'{dir_name}/{predict}_{hash_id}.png')
  else:

    dir_name = "wrong"
    img.save(f'{dir_name}/{predict}_{hash_id}.png')

  os.remove(file_name)

  print(f'acc: {correct_count / total_count}')
  print()
  # make the wrong answer correct
  if dir_name == "wrong":
    print('\nTrying to make the wrong correct')
    find_correct(predict)
    
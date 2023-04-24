import os
import ddddocr
import subprocess
from PIL import Image

ocr = ddddocr.DdddOcr(det=False, ocr=True, import_onnx_path="/content/NTUST_dddd_trainer/projects/ntust_mail/old_models/ntust_mail_1.0_201_41200_2023-04-11-09-21-32.onnx", charsets_path="/content/NTUST_dddd_trainer/projects/ntust_mail/old_models/charsets.json")

for i in range(1000):
  hash_id = subprocess.getstatusoutput('php spider2.php')[1]
  file_name = f'{hash_id}.png'

  with open(file_name, 'rb') as f:
    img_bytes = f.read()

  predict = ocr.classification(img_bytes)

  correct_prediction = subprocess.getstatusoutput(f'php spider2.php {hash_id} {predict}')[1]

  print(predict)
  print(correct_prediction)

  img = Image.open(file_name)
  if correct_prediction == 'true':
    dir_name = "correct"
    img.save(f'{dir_name}/{predict}_{hash_id}.png')
  else:

    dir_name = "wrong"
    img.save(f'{dir_name}/{predict}_{hash_id}.png')

  os.remove(file_name)
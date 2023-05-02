import ddddocr
import os
from tqdm import tqdm

ocr = ddddocr.DdddOcr(det=False, ocr=True, import_onnx_path="/content/NTUST_dddd_trainer/projects/ntust_mail/models/model.onnx", charsets_path="/content/NTUST_dddd_trainer/projects/ntust_mail/models/charsets.json")
acc_list = []

list_dir = [
'/content/NTUST_dddd_trainer/datasets/ntust/ntust_val_10000',  
'/content/NTUST_dddd_trainer/datasets/ntust/P2x2_val',
'/content/NTUST_dddd_trainer/datasets/ntust/P4x4_val',
'/content/NTUST_dddd_trainer/datasets/ntust/P8x8_val',
'/content/NTUST_dddd_trainer/datasets/ntust/B3x3_val',
'/content/NTUST_dddd_trainer/datasets/ntust/B5x5_val',
'/content/NTUST_dddd_trainer/datasets/ntust/B7x7_val',
'/content/NTUST_dddd_trainer/datasets/ntust/B9x9_val',
'/content/NTUST_dddd_trainer/datasets/ntust/B15x15_val',
'/content/NTUST_dddd_trainer/datasets/ntust/B45x45_val',
'/content/NTUST_dddd_trainer/datasets/ntust/B99x99_val'
]


for directory in tqdm(list_dir):
  total_count = 0
  correct_count = 0

  for filename in os.listdir(directory):
    total_count += 1
    with open(f'{directory}/{filename}', 'rb') as f:
      image_bytes = f.read()

    res = ocr.classification(image_bytes)
    answer = filename.split('_')[0]

    #print(res)
    #print(answer)

    if res == answer:
      correct_count += 1
    if total_count >= 1000:
      break

  accuracy = correct_count / total_count
  acc_list.append(accuracy)
  print(accuracy)

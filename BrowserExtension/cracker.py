import ddddocr
import os

ocr = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False, import_onnx_path="./ntust_mail_1.0_201_41200_2023-04-11-09-21-32.onnx", charsets_path="./charsets.json")
# with open('./samples/71.png', 'rb') as f:
#     img_bytes = f.read()
# res = ocr.classification(img_bytes)
#
# print(res)
with open('./captcha.png', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)
print(res)

# for path in os.listdir("./samples"):
#     if ".png" in path:
#         # ocr = ddddocr.DdddOcr(show_ad=False, beta=True)
#         with open('./samples/' + path, 'rb') as f:
#             img_bytes = f.read()
#         res = ocr.classification(img_bytes)
#         print(res, path)

import ddddocr
import os

ocr = ddddocr.DdddOcr(show_ad=False, beta=True)
with open('./ref/sample/201.png', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)

print(res)


for path in os.listdir("./ref/sample_tagged"):
    if ".png" in path:
        ocr = ddddocr.DdddOcr(show_ad=False, beta=True)
        with open('./ref/sample/' + path, 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        print(res, path)

import cv2

img = cv2.imread('pic.png')
cv2.imshow('ori', img)

for i in range(3, 16, 2):
    output1 = cv2.medianBlur(img, i)     # kernel size i*i
    cv2.imshow(f'kernel size {i}*{i}', output1)
cv2.waitKey(0)
cv2.destroyAllWindows()

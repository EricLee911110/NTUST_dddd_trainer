import cv2

img = cv2.imread('pic.png')
cv2.imshow('ori', img)

for i in range(3, 36, 4):
    output1 = cv2.GaussianBlur(img, (i, i), 0)    # kernel size i*i
    cv2.imshow(f'kernel size {i}*{i}', output1)
cv2.waitKey(0)
cv2.destroyAllWindows()

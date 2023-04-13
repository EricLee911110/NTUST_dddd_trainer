import cv2

img = cv2.imread('pic.png')
cv2.imshow('ori', img)

for i in range(5, 25, 3):
    output1 = cv2.blur(img, (i, i))     # kernel size i*i
    cv2.imshow(f'kernel size {i}*{i}', output1)
cv2.waitKey(0)
cv2.destroyAllWindows()

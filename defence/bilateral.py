import cv2

img = cv2.imread('pic.png')
cv2.imshow('ori', img)

ksize = 23
sigma = 0
output1 = cv2.bilateralFilter(img, ksize, sigma, sigma)
cv2.imshow(f'kernel size {ksize}, sigma {sigma}', output1)
cv2.waitKey(0)
cv2.destroyAllWindows()

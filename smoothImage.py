import cv2

image = cv2.imread("noisy.png")
cv2.imshow("Noisy Image", image) 

output = cv2.GaussianBlur(image, (12,12), 1) 
cv2.imshow("Smoothed image", output)
cv2.waitKey(0)

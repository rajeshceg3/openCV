import cv2

image = cv2.imread("faces.png")
cv2.imshow("Original Image",image)

resized = cv2.resize(image, (200,200))
cv2.imshow("Resized Image",resized)
cv2.waitKey(0)

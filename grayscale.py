import cv2

image = cv2.imread("faces.png")
cv2.imshow("Original",image)

output = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",output)

cv2.waitKey(0)

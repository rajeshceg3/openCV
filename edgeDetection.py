import cv2

image = cv2.imread("coins.png")
cv2.imshow("Default", image)

# Canny takes image,lower and upper thresholds 
# as parameters

edg_detected = cv2.Canny(image, 200, 250) 
cv2.imshow("After Edge Detection", edg_detected)

cv2.waitKey(0)

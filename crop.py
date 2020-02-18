import cv2

image = cv2.imread("faces.png")
cv2.imshow("Without Crop", image)

image[ybegin:yend, xbegin:xend]
new_img = image[60:160, 300:380]
cv2.imshow("After Crop", new_img)
cv2.waitKey(0)

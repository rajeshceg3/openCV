import cv2

image = cv2.imread("faces.png")
final_img = image.copy()

cv2.rectangle(final_img, (320, 30), (480, 180), (0, 0, 255), 2)
cv2.imshow("Rectangular Image", final_img)
cv2.waitKey(0)

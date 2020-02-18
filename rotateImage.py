import cv2

image = cv2.imread("faces.png")
(h,w,d) = image.shape

center = (w//2,h//2)
rotMatrix = cv2.getRotationMatrix2D(center,-45, 1.0)
rotated_image = cv2.warpAffine(image,rotMatrix,(w,h))
cv2.imshow("Rotated Image",rotated_image)
cv2.waitKey(0)

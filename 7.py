import cv2
import matplotlib.pyplot as plt
image = cv2.imread('car.jpg')
gray_image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow('Gray image',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
img = cv2.GaussianBlur(gray_image,(3,3),0)

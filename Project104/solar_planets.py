import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "The Solar System", (290,65), cv2.FONT_HERSHEY_COMPLEX, 2.7, (255,255,255))
cv2.putText(img, "Sun", (75,400), cv2.FONT_HERSHEY_COMPLEX, 3, (0,0,255))
cv2.putText(img, "Mercury", (115,240), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Venus", (190,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Earth", (290,260), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Mars", (380,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Jupiter", (560,360), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Saturn", (760,135), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Uranus", (965,285), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Neptune", (1110,150), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.imshow("Output", img)
cv2.waitKey(0)


cv2.imwrite("Solar_systemwithname.jpg",img)